import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape data from the webpage
def scrape_data(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all div elements with class 'row justify-content-center'
    rows = soup.find_all('div', class_='row justify-content-center')
    
    # List to store scraped data
    scraped_data = []
    
    # Iterate through each row
    for row in rows:
        # Find all col-md-3 col-12 inside each row
        columns = row.find_all('div', class_='col-md-3 col-12')
        
        for column in columns:
            # Find the box-content div inside each column
            box_content = column.find('div', class_='box-content')
            
            if box_content:
                # Extract constituency name (h3 tag)
                h3 = box_content.find('h3')
                if h3:
                    constituency = h3.text.strip()
                else:
                    constituency = "N/A"
                
                # Extract state name (h4 tag)
                h4 = box_content.find('h4')
                if h4:
                    state = h4.text.strip()
                else:
                    state = "N/A"
                
                # Extract candidate name (h5 tag)
                h5 = box_content.find('h5')
                if h5:
                    candidate_name = h5.text.strip()
                else:
                    candidate_name = "N/A"
                
                # Extract party name (h6 tag)
                h6 = box_content.find('h6')
                if h6:
                    party_name = h6.text.strip()
                else:
                    party_name = "N/A"
                
                # Extract election result status (h2 tag with class 'won')
                h2 = box_content.find('h2', class_='won')
                if h2:
                    result_status = h2.text.strip()
                else:
                    result_status = "N/A"
                
                # Prepare a dictionary for the current entry
                entry = {
                    'Constituency': constituency,
                    'State': state,
                    'Candidate Name': candidate_name,
                    'Party Name': party_name,
                    'Result Status': result_status
                }
                
                # Append the dictionary to the list
                scraped_data.append(entry)
    
    return scraped_data

# Function to write data to CSV file
def write_to_csv(data, filename):
    # Define CSV fieldnames based on the keys of the dictionaries (columns)
    fieldnames = ['Constituency', 'State', 'Candidate Name', 'Party Name', 'Result Status']
    
    # Write data to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Write rows
        for row in data:
            writer.writerow(row)

# Example usage:
if __name__ == "__main__":
    # Replace with the actual URL you want to scrape
    url = 'https://results.eci.gov.in/AcResultByeJune2024/index.htm'
    
    # Scrape data from the URL
    scraped_data = scrape_data(url)
    
    # Specify the CSV filename
    csv_filename = 'bye_data.csv'
    
    # Write scraped data to CSV
    write_to_csv(scraped_data, csv_filename)
    
    print(f"Scraped data has been successfully written to '{csv_filename}'.")

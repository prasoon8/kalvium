import requests
from bs4 import BeautifulSoup
import csv

url = 'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S24.htm'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    
    if table:
        rows = table.find_all('tr')
        
        with open('up_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            
            for row in rows:
                cells = row.find_all(['th', 'td'])
                writer.writerow([cell.get_text(strip=True) for cell in cells])
            
        print("Table data has been successfully scraped and saved to table_data.csv")
    else:
        print("No table found on the page.")
else:
    print("Failed to retrieve the page.")

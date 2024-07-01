# Party Data Analysis

This repository contains a script to analyze and visualize the data from `party_data.csv`. The script uses Python libraries such as `pandas`, `matplotlib`, `seaborn`, and `numpy` to perform the analysis and generate plots.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Description](#data-description)
- [Visualizations](#visualizations)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/party-data-analysis.git
   cd party-data-analysis
   ```

2. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn numpy
   ```

## Usage

1. Place the `party_data.csv` file in the root directory of the repository.

2. Run the script to generate the visualizations:
   ```bash
   python analyze_party_data.py
   ```

3. The script will display the following visualizations:
   - Total seats won by each party (log scale)
   - Comparison of seats won by each party (log scale)
   - Distribution of seats won (log scale)

## Data Description

The `party_data.csv` file should have the following columns:
- `Party`: The name of the political party.
- `Total`: The total number of seats available.
- `Won`: The number of seats won by the party.

## Visualizations

1. **Total Seats Won by Each Party (Log Scale)**
   ![Total Seats Won](images/total_seats_won_log.png)

2. **Comparison of Seats Won by Each Party (Log Scale)**
   ![Comparison of Seats Won](images/comparison_seats_won_log.png)

3. **Distribution of Seats Won (Log Scale)**
   ![Distribution of Seats Won](images/distribution_seats_won_log.png)
<img width="1385" alt="Screenshot 2024-06-28 at 9 47 47 PM" src="https://github.com/prasoon8/kalvium/assets/156693039/82aa48a9-978b-4be5-8946-32a6a514464c">


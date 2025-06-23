# GDP
GDP Per Capita Analysis: Denmark vs Greece
This project analyzes and compares the Real GDP per capita and population changes of Denmark and Greece from 1995 to 2022.
📊 Project Overview

This script:

    Loads real GDP per capita data and population data from CSV files.

    Filters for Denmark and Greece.

    Calculates year-over-year differences in GDP and population.

    Computes the GDP per capita difference between the two countries.

    Outputs the processed data to a new CSV file: gdp_analysis_output.csv.

🧾 Files

    Real GDP per capita.csv: Contains GDP per capita data by country and year.

    population.csv: Contains population data (from World Bank or similar source).

    gdp_analysis_output.csv: Output file with combined and processed data.

    main.py: Python script for data processing (based on the code you wrote).

    README.md: This documentation file.

🧠 What You’ll Learn

    Data manipulation using pandas

    Merging datasets across multiple dimensions (country, year)

    Performing .diff() operations to compute changes over time

    Time-series alignment for comparative analysis

🛠 How to Run

    Install dependencies:

pip install pandas

Make sure the following files are in the same directory:

    Real GDP per capita.csv

    population.csv

Run the script:

    main.py

    Check gdp_analysis_output.csv for the results.

📈 Sample Output Columns
Year	EL: Greece	DK: Denmark	GDP Difference	Greece_diff	Denmark_diff	Greece_pop	Denmark_pop	...
🔍 Future Ideas

    Visualization using matplotlib or seaborn

    Add more countries or metrics (e.g., unemployment, inflation)

    Create an interactive dashboard (e.g., with Plotly or Streamlit)

📘 License

MIT License — feel free to use, modify, and share.

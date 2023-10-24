# Radio-Reference-AU Scraper

This Python script scrapes radio frequencies from the RadioReference website for Australian regions. It recursively retrieves data from multiple pages and stores the information in CSV files organized by state, region, category, and base name.

## How to Use

1. **Requirements**:
   - Python (3.6 or higher)
   - BeautifulSoup (for parsing HTML)
   - Requests (for making HTTP requests)

   You can install the required libraries using the following command:
   ```bash
   pip install beautifulsoup4 requests
   ```

2. **Running the Scraper**:
   - Ensure that you have the required libraries installed.
   - Run the `radio_reference_au_scraper.py` script.

   ```bash
   python radio_reference_au_scraper.py
   ```

   This will initiate the scraping process.

3. **Output**:
   - The script will create a `csv` directory (if not already present).
   - CSV files will be stored in the following format:
     - `csv/state/region/category/base_name.csv`

   The CSV files will have the following columns:
   - `category`
   - `group`
   - `frequency`
   - `license`
   - `type`
   - `tone`
   - `alpha tag`
   - `description`
   - `mode`
   - `tag`

## Example Entry in CSV

```
category,group,frequency,license,type,tone,alpha tag,description,mode,tag
Federal Agencies,Australian Federal Police - AFP,488.375,VL4AFP,RM,141 NAC,Cairns,Area Dispatch,P25,Federal
Federal Agencies,Australian Federal Police - AFP,489.550,VL4AFP,RM,141 NAC,Cairns,Airport Dispatch,P25,Fire Dispatch
General Frequencies,Cairns Airband,118.400,,BM,CSQ,APPROACH-DEP,APPROACH-DEPARTURES,AM,Aircraft
```

## Disclaimer

Please be aware that scraping websites may be subject to terms of use and may potentially violate the website's policies. Use this script responsibly and consider the legality and ethical implications of scraping data from websites.
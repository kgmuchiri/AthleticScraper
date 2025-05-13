import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib3

# Base URL with everything embedded
base_url = "https://worldathletics.org/records/all-time-toplists/road-running/marathon/all/men/senior?regionType=world&page={page}&bestResultsOnly=false&firstDay=1900-01-01&lastDay=2025-05-13&maxResultsByCountry=all&ageCategory=senior"

# Suppress SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

all_data = []

def scrape_marathon():
    page = 1
    while True:
        url = base_url.format(page=page)
        headers = {"User-Agent": "Mozilla/5.0"}
        print(f"Scraping page {page}...")
        response = requests.get(url, headers=headers, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='records-table')

        if not table:
            break

        rows = table.find('tbody').find_all('tr')
        if not rows:
            break

        for row in rows:
            cols = row.find_all('td')
            if not cols or len(cols) < 11:
                continue
            all_data.append({
                "Rank": cols[0].text.strip(),
                "Mark": cols[1].text.strip(),
                "Competitor": cols[3].text.strip(),
                "DOB": cols[4].text.strip(),
                "Nationality": cols[5].text.strip(),
                "Position": cols[6].text.strip(),
                "Venue": cols[8].text.strip(),
                "Date": cols[9].text.strip(),
                "Result Score": cols[10].text.strip()
            })

        page += 1
        time.sleep(1)

scrape_marathon()

# Save to CSV
df = pd.DataFrame(all_data)
df.to_csv("mens_marathon_all_time.csv", index=False)
print("✅ Data saved to mens_marathon_all_time.csv")

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Event groups by type
event_map = {
    "sprints": ["100-metres", "200-metres", "300-metres","400-metres"],
    "middlelong": ["800-metres", "1000-metres","1500-metres", "one-mile","2000-metres", "3000-metres", "5000-metres", "10000-metres","2000-metres-steeplechase", "3000-metres-steeplechase"],
    "road-running": ["half-marathon", "marathon"],
    "throws": ["javelin-throw", "shot-put", "discus-throw", "hammer-throw"],
    "jumps": ["pole-vault", "high-jump", "long-jump","triple-jump"],
    "hurdles":[]
}

# Parameters
genders = ["men", "women"]
age_categories = ["senior", "u20", "u18"]
base_url = "https://worldathletics.org/records/all-time-toplists/{event_type}/{discipline}/all/{gender}/{age_category}?regionType=world&page={page}&bestResultsOnly=false&firstDay=1900-01-01&lastDay=2025-05-13&maxResultsByCountry=all"

# Result container
all_data = []

def scrape_all_time_lists():
    for event_type, disciplines in event_map.items():
        for discipline in disciplines:
            for gender in genders:
                for age_category in age_categories:
                    scrape_event(event_type, discipline, gender, age_category)

def scrape_event(event_type, discipline, gender, age_category):
    page = 1
    while True:
        url = base_url.format(event_type=event_type, discipline=discipline, gender=gender, age_category=age_category, page=page)
        headers = {"User-Agent": "Mozilla/5.0"}
        print(f"🔍 Scraping: {event_type} | {discipline} | {gender} | {age_category} | Page {page}")
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
                "Event Type": event_type,
                "Discipline": discipline,
                "Gender": gender,
                "Age Category": age_category,
                "Rank": cols[0].text.strip(),
                "Mark": cols[1].text.strip(),
                "Wind": cols[2].text.strip(),
                "Competitor": cols[3].text.strip(),
                "DOB": cols[4].text.strip(),
                "Nationality": cols[5].text.strip(),
                "Position": cols[6].text.strip(),
                "Venue": cols[8].text.strip(),
                "Date": cols[9].text.strip(),
                "Result Score": cols[10].text.strip()
            })

        page += 1
        time.sleep(1)  # be respectful to the server

# Run the scraper
scrape_all_time_lists()

# Save to CSV
df = pd.DataFrame(all_data)
df.to_csv("./data/all_time_athletics_data_2025.csv", index=False)
print("Data saved to all_time_athletics_data_2025.csv")

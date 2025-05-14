import os
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# ─── Setup ─────────────────────────────────────────────────────────────

# Disable SSL warnings for testing
urllib3.disable_warnings(InsecureRequestWarning)

# Base URL format
BASE_URL = (
    "https://worldathletics.org/records/all-time-toplists/{type_slug}/{discipline_slug}/all/{gender}/{age_category}"
    "?regionType=world&page={page}&bestResultsOnly=false&firstDay=1900-01-01&lastDay=2025-05-13&maxResultsByCountry=all"
)

# Load discipline and type options from JSON
with open("options.json", "r") as f:
    options_data = json.load(f)

# ─── Extract Combinations ─────────────────────────────────────────────

discipline_mappings = {}
for entry in options_data:
    if entry.get("name") == "disciplineCode":
        for case in entry.get("cases", []):
            key = (case.get("gender"), case.get("ageCategory"))
            values = case.get("values", [])
            discipline_mappings[key] = [
                (v["disciplineNameUrlSlug"], v["typeNameUrlSlug"])
                for v in values
                if "disciplineNameUrlSlug" in v and "typeNameUrlSlug" in v
            ]

# ─── Scraper ──────────────────────────────────────────────────────────

def scrape_event(gender, age_category, discipline_slug, type_slug, output_dir):
    page = 1
    data = []

    while True:
        url = BASE_URL.format(
            type_slug=type_slug,
            discipline_slug=discipline_slug,
            gender=gender,
            age_category=age_category,
            page=page
        )
        print(f"🔍 Scraping {url}")
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find("table", class_="records-table")
        if not table:
            break

        rows = table.find("tbody").find_all("tr")
        if not rows:
            break

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 11:
                continue
            data.append({
                "Rank": cols[0].text.strip(),
                "Mark": cols[1].text.strip(),
                "Wind": cols[2].text.strip(),
                "Competitor": cols[3].text.strip(),
                "DOB": cols[4].text.strip(),
                "Nationality": cols[5].text.strip(),
                "Position": cols[6].text.strip(),
                "Venue": cols[8].text.strip(),
                "Date": cols[9].text.strip(),
                "Result Score": cols[10].text.strip(),
                "Type": type_slug,
                "Discipline": discipline_slug,
                "Gender": gender,
                "Age Category": age_category
            })

        page += 1
        time.sleep(1)

    # Save if data found
    if data:
        os.makedirs(output_dir, exist_ok=True)
        filename = f"{type_slug}_{discipline_slug}_{age_category}.csv".replace(" ", "_").replace("/", "-")
        filepath = os.path.join(output_dir, filename)
        pd.DataFrame(data).to_csv(filepath, index=False)
        print(f"✅ Saved {filepath}")

# Run Scrape ----------------------------------------------------------------------------------

for (gender, age_category), discipline_list in discipline_mappings.items():
    output_dir = os.path.join("output", gender)
    for discipline_slug, type_slug in discipline_list:
        scrape_event(gender, age_category, discipline_slug, type_slug, output_dir)

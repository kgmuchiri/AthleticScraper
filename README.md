# Python Scraper for World Athletics Database

## About
This is a python project that takes the large dataset that is the top athletic performance for the most common track and field events and turns it into a csv file for use in EDA, AI, ML or Data Visualisation.

When run it will take the current date as the end date and gather all the results for each discipline. 

Inspired by: https://github.com/thomascamminady/world-athletics-database/

Used the options.json file from that repo to help

Note: Datasets here are from 19-05-2025

### Repo Structure
 - Output: Folder for the csv files created as a result of scraping
 - Combined: a folder that takes the outputs and combines them on overall discipline e.g. Shot-put and Shot-put 6kg are of the shotput discpline however their records are maintained seperately one the World Athletics Page
 - Datasets: contains datasets split by type, individual events and relay events
 - Logs: For any errors that come up during
 - Notebooks: Jupyter notebooks for EDA
 - Scripts: Contains all the scripts necessary to generate the datasets

### To Run
- Install requirements from requirements.txt
- Run file "run.py"

# 🏃‍♀️ Athletics Performance Dataset Description

This dataset contains structured performance records from international athletics competitions. Each row corresponds to an athlete's performance in a single event.

## 📄 Columns

| Column Name           | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `Rank`                | Athlete’s placement within the event (1 = first place).                     |
| `Mark`                | Performance mark (in seconds for track or meters for field events).         |
| `Wind`                | Wind reading during the event (m/s); relevant for sprints and hurdles.      |
| `Competitor`          | Full name of the athlete.                                                   |
| `DOB`                 | Date of birth of the athlete (`YYYY-MM-DD`).                                |
| `Nationality`         | 3-letter IOC code representing the athlete’s country.                       |
| `Position`            | The athlete's position in the heat/final (if different from rank).          |
| `Venue`               | Full name of the event venue.                                               |
| `Date`                | Date of the event (`YYYY-MM-DD`).                                           |
| `Result Score`        | Scoring index from the event, if available. Created by WAA, max of 1400                   |
| `Discipline`          | Original discipline string, including implement or hurdle specs (e.g., `110m-hurdles-990cm`). |
| `Type`                | General classification of the event (e.g., `sprints`, `hurdles`, `throws`). |
| `Gender`              | Athlete's gender (`male` or `female`).                                      |
| `Age Category`        | Athlete's age classification (e.g., `u20`, `u18`, `senior`).                |
| `normalized_discpline`| Cleaned discipline name used for grouping (e.g., `110-metres-hurdles`).     |
| `track_field`         | Whether the event is a `track`, `field`, or `mixed` discipline.             |
| `mark_numeric`        | Parsed numeric value of the mark (in seconds or meters).                    |
| `venue_country_code`  | IOC 3-letter code extracted from the venue (e.g., `KEN`).                   |
| `age_at_event`        | Age of the athlete at the time of the event (in full years).                |
| `season`              | Year in which the event took place.                                         |
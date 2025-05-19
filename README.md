# Python Scraper for World Athletics

## About
This is a python project that takes the large dataset that is the top athletic performance for the most common track and field events and turns it into a csv file for use in EDA, AI, ML or Data Visualisation.

When run it will take the current date as the end date and gather all the results for each discipline. 

Inspired by:

Used the options.json file from that repo to help

### Repo Structure
 - Output: Folder for the csv files created as a result of scraping
 - Combined: a folder that takes the outputs and combines them on overall discipline e.g. Shot-put and Shot-put 6kg are of the shotput discpline however their records are maintained seperately one the World Athletics Page
 - Datasets: contains datasets split by type, individual events and relay events
 - Logs: For any errors that come up during
 - Notebooks: Jupyter notebooks for EDA
 - Scripts: Contains all the scripts necessary to generate the datasets
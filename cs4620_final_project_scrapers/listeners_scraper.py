import requests
from bs4 import BeautifulSoup

url = "https://kworb.net/spotify/listeners.html" # url of website to scrape
response = requests.get(url) 

# check for request success
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser') # make soup object, grab html from website
    table = soup.find('table') # get table containing listeners data
    # is table found?
    if table: 
        rows = table.find_all('tr')[1:] # get all rows in the table except the first one
        for row in rows:
            # grab artist name, listener count, daily trend, peak listeners position, and peak listeners count cells
            cell_parts = row.find_all('td')
            artist_name = cell_parts[0]
            listener_count = cell_parts[1]
            daily_trend = cell_parts[2]
            peak_listeners_position = cell_parts[3]
            peak_listeners_count = cell_parts[4]
            # pull text out of the cells, print recombined strings
            print(artist_name.text.strip() + '-' + listener_count.text.strip() + '-' + daily_trend.text.strip() + '-' + peak_listeners_position.text.strip() + '-' + peak_listeners_count.text.strip())
    else:
        print("Error: table not found in the page") # table not found error message
else:
    print("Error: failed to retrieve the webpage") # request failed error message
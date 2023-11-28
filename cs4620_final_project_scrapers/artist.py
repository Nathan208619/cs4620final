import requests
from bs4 import BeautifulSoup

url = "https://kworb.net/spotify/artists.html" # url of website to scrape
response = requests.get(url) 

# check for request success
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser') # make soup object, grab html from website
    table = soup.find('table') # get table containing album data
    # is table found?
    if table: 
        rows = table.find_all('tr')[1:] # get all rows in the table except the first one
        for row in rows:
            cell_parts = row.find_all('td')
            artist = cell_parts[0]
            stream_count = cell_parts[1]
            daily_trend = cell_parts[2]
            as_lead = cell_parts[3]
            solo = cell_parts[4]
            as_featured = cell_parts[5]
            # pull text out of the cells, print recombined strings
            print(artist.text.strip() + ' - ' + stream_count.text.strip() + ' - ' + daily_trend.text.strip() + ' - ' + as_lead.text.strip() + ' - ' + solo.text.strip() + ' - ' + as_featured.text.strip())
    else:
        print("Error: table not found in the page") # table not found error message
else:
    print("Error: failed to retrieve the webpage") # request failed error message
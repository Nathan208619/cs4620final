import requests
from bs4 import BeautifulSoup

url = "https://kworb.net/spotify/songs_2022.html"  # url of website to scrape

response = requests.get(url)# make request to website

# check for request success
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser') # make soup object, grab html from website
    table = soup.find('table')# get table containing song data
    # is table found?
    if table:
        rows = table.find_all('tr')[1:] # get all rows in the table except the first one
        # Extract and print the song titles
        for row in rows:
            # grab title-artist and stream count cells
            cell_parts = row.find_all('td')
            title_artist_cell = cell_parts[0]
            stream_cell = cell_parts[1]
            daily_trend = cell_parts[2]
            # pull text out of the cells, print recombined strings
            print(title_artist_cell.text.strip() + '-' + stream_cell.text.strip() + '-' + daily_trend.text.strip())
    else:
        print("Error: table: not found in the page") # table not found error message
else:
    print("Error: failed to retrieve the webpage") # request failed error message

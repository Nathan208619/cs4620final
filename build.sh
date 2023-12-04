rm music.db
python3 ./cs4620_final_project_scrapers/streams_scraper.py > ./data/most_streams.csv
python3 ./cs4620_final_project_scrapers/listeners_scraper.py > ./data/listeners.csv
python3 ./cs4620_final_project_scrapers/albums_scraper.py > ./data/albums.csv
python3 ./cs4620_final_project_scrapers/artists_scraper.py > ./data/artists.csv
python3 ./cs4620_final_project_scrapers/2020_streams.py > ./data/2020.csv
python3 ./cs4620_final_project_scrapers/2021_streams.py > ./data/2021.csv
python3 ./cs4620_final_project_scrapers/2022_streams.py > ./data/2022.csv
python3 ./cs4620_final_project_scrapers/2023_streams.py > ./data/2023.csv
python3 ./database_loader/create_db.py
python3 ./database_loader/load_db.py
cp music.db ./webpage
# python3 ./webpage/song_page_visuals.py
cd data
rm *.csv
cd ..
cd webpage
rm music.db
cd static
cd visualizations
rm *.png
cd artist_battle
rm *.png
cd ..
cd ..
cd ..
cd ..
cd cs4620_final_project_scrapers
python3 streams_scraper.py > ../data/most_streams.csv
python3 listeners_scraper.py > ../data/listeners.csv
python3 albums_scraper.py > ../data/albums.csv
python3 artists_scraper.py > ../data/artists.csv
python3 ./2020_streams.py > ../data/2020.csv
python3 ./2021_streams.py > ../data/2021.csv
python3 ./2022_streams.py > ../data/2022.csv
python3 ./2023_streams.py > ../data/2023.csv
cd ..
cd database_loader
rm music.db
python3 create_db.py
python3 load_db.py
cp music.db ../webpage
cd ..
cd webpage
python3 song_page_visuals.py
python3 artist_battle.py
python3 app.py
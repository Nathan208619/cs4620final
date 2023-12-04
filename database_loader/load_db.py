import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def get_data():
    most_streams = []
    file = open("./data/most_streams.csv", "r", encoding="utf-8")
    for line in file:
        front = line[:line.find("-") - 1]
        end = line[line.find("-") + 2:].replace("\n", "")
        most_streams.append(front + "-" + end)
    file.close()    
    return most_streams

def build_streams_table():
    conn = create_connection("music.db")
    streams = get_data()
    cur = conn.cursor()
    for entry in streams:
        parts = entry.split("-")
        if parts.__len__() != 4:
            continue
        artist = parts[0]
        title = parts[1]
        total_streams = parts[2].replace(",", "")
        daily_streams = parts[3]
        if len(daily_streams) < 1:
            daily_streams = '0'
        else:
            daily_streams = daily_streams.replace(",", "")
        # cur.execute("INSERT INTO most_streams (streams_id, title, artist, total_streams, daily_streams) VALUES (?, ?, ?, ?, ?)", (id, title, artist, total_streams, daily_streams))
        cur.execute("INSERT INTO most_streams (title, artist, total_streams, daily_streams) VALUES (?, ?, ?, ?)", (title, artist, total_streams, daily_streams))
        conn.commit()
    conn.close()

def build_listeners_table():
    file = open("./data/listeners.csv", "r", encoding="utf-8")
    conn = create_connection("music.db")
    cur = conn.cursor()
    for line in file:
        parts = line.split("-")
        if parts.__len__() != 5:
            continue
        artist = parts[0]
        listeners = parts[1].replace(",", "")
        daily_listeners = parts[2].replace(",", "")
        peak_listeners = parts[4].replace(",", "")
        peak_position = parts[3]
        cur.execute("INSERT INTO most_listeners (artist, listeners, daily_listeners, peak_listeners, peak_position) VALUES (?, ?, ?, ?, ?)", (artist, listeners, daily_listeners, peak_listeners, peak_position))
        conn.commit()
    conn.close()

def get_album_data():
    most_streams = []
    file = open("./data/albums.csv", "r", encoding="utf-8")
    for line in file:
        front = line[:line.find("-") - 1]
        end = line[line.find("-") + 2:].replace("\n", "")
        most_streams.append(front + "-" + end)
    file.close()
    return most_streams

def build_albums_table():
    albums_list = get_album_data()
    conn = create_connection("music.db")
    cur = conn.cursor()
    for entry in albums_list:
        parts = entry.split("-")
        if parts.__len__() != 4:
            continue
        artist = parts[1]
        album = parts[0]
        streams = parts[2].replace(",", "")
        daily_streams = parts[3].replace(",", "")
        cur.execute("INSERT INTO most_streamed_album (artist, album, streams, daily_streams) VALUES (?, ?, ?, ?)", (album, artist, streams, daily_streams))
        conn.commit()
    conn.close()

def build_artists_table():
    file = open("./data/artists.csv", "r", encoding="utf-8")
    conn = create_connection("music.db")
    cur = conn.cursor()
    for line in file:
        parts = line.replace("\n", "").split("-")
        if parts.__len__() != 6:
            continue
        artist = parts[0]
        streams = parts[1].replace(",", "")
        daily_streams = parts[2].replace(",", "")
        if len(daily_streams) < 1:
            daily_streams = 0
        stream_as_lead = parts[3].replace(",", "")
        if len(stream_as_lead) < 1:
            stream_as_lead = '0'
        stream_as_feature = parts[5].replace(",", "")
        if len(stream_as_feature) < 1:
            stream_as_feature = '0'
        streams_solo = parts[4].replace(",", "")
        if len(streams_solo) < 1:
            streams_solo = '0'
        cur.execute("INSERT INTO most_streamed_artist (artist, streams, daily_streams, stream_as_lead, stream_as_feature, streams_solo) VALUES (?, ?, ?, ?, ?, ?)", (artist, streams, daily_streams, stream_as_lead, stream_as_feature, streams_solo))
        conn.commit()
    file.close()
    conn.close()

def get_year_data(year):
    year_streams = []
    path = "./data/" + year + ".csv"
    file = open(path, "r", encoding="utf-8")
    for line in file:
        front = line[:line.find("-") - 1]
        end = line[line.find("-") + 2:].replace("\n", "")
        year_streams.append(front + "-" + end)
    file.close()
    return year_streams

def build_year_table(year):
    conn = create_connection("music.db")
    year_streams = get_year_data(year)
    cur = conn.cursor()
    for entry in year_streams:
        parts = entry.split("-")
        if parts.__len__() != 4:
            continue
        artist = parts[0]
        title = parts[1]
        total_streams = parts[2].replace(",", "")
        daily_streams = parts[3].replace(",", "")
        command = "INSERT INTO most_streams_of_" + year + " (title, artist, total_streams, daily_streams) VALUES (?, ?, ?, ?)"
        cur.execute(command, (title, artist, total_streams, daily_streams))
        # cur.execute("INSERT INTO most_streams_of_" + year + " (title, artist, total_streams, daily_streams) VALUES (?, ?, ?, ?)", (title, artist, total_streams, daily_streams))
        conn.commit()



build_streams_table()
build_listeners_table()
build_albums_table()
build_artists_table()
build_year_table("2020")
build_year_table("2021")
build_year_table("2022")
build_year_table("2023")
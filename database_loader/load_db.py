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
    file = open("../data/most_streams.csv", "r")
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
        total_streams = parts[2]
        daily_streams = parts[3]
        # cur.execute("INSERT INTO most_streams (streams_id, title, artist, total_streams, daily_streams) VALUES (?, ?, ?, ?, ?)", (id, title, artist, total_streams, daily_streams))
        cur.execute("INSERT INTO most_streams (title, artist, total_streams, daily_streams) VALUES (?, ?, ?, ?)", (title, artist, total_streams, daily_streams))
        conn.commit()
    conn.close()

def build_listeners_table():
    listeners_list = []
    file = open("../data/listeners.csv", "r")
    for line in file:
        listeners_list.append(line)
    file.close()
    conn = create_connection("music.db")
    cur = conn.cursor()
    for entry in listeners_list:
        parts = entry.split("-")
        if parts.__len__() != 5:
            continue
        artist = parts[0]
        listeners = parts[1]
        daily_listeners = parts[2]
        peak_listeners = parts[4]
        peak_position = parts[3]
        cur.execute("INSERT INTO most_listeners (artist, listeners, daily_listeners, peak_listeners, peak_position) VALUES (?, ?, ?, ?, ?)", (artist, listeners, daily_listeners, peak_listeners, peak_position))
        conn.commit()
    conn.close()


build_streams_table()
build_listeners_table()
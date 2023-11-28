import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def generate_database():
    database = "music.db"

    streams = """ CREATE TABLE IF NOT EXISTS most_streams (
                    streams_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                    title text NOT NULL,
                    artist text NOT NULL,
                    total_streams integer NOT NULL,
                    daily_streams integer
                                    ); """

    listeners = """CREATE TABLE IF NOT EXISTS most_listeners (
                    listeners_id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                    artist text NOT NULL,
                    listeners integer NOT NULL,
                    daily_listeners integer,
                    peak_listeners integer,
                    peak_position integer
                                );"""
    
    albums = """CREATE TABLE IF NOT EXISTS most_streamed_album (
                    album_id integer PRIMARY KEY NOT NULL,
                    album text NOT NULL,
                    artist text NOT NULL,
                    streams integer NOT NULL,
                    daily_streams integer
                                );"""
    
    artists = """CREATE TABLE IF NOT EXISTS most_streamed_artist (
                    artist_id integer PRIMARY KEY NOT NULL,
                    artist text NOT NULL,
                    streams integer NOT NULL,
                    daily_streams integer,
                    stream_as_lead integer,
                    stream_as_feature integer,
                    streams_solo integer
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create most_streams table
        create_table(conn, streams)

        # create most_listeners table
        create_table(conn, listeners)

        # create most_streamed_album table
        create_table(conn, albums)

        # create most_streamed_artist table
        create_table(conn, artists)
    else:
        print("Error: cannot create the database connection")

generate_database()
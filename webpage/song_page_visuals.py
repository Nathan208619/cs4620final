import sqlite3
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import matplotlib.cm as cm

def query_the_database(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)

def top_ten_most_streamed_songs():
    conn = sqlite3.connect("music.db")
    query = "SELECT title, total_streams FROM most_streams ORDER BY total_streams DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    titles, streams = zip(*data)

    # create bar chart
    plt.figure(figsize=(12, 8))
    plt.bar(titles, streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Titles', fontsize=18)
    plt.ylabel('Streams', fontsize=18)
    title = "Top 10 most streamed songs"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/most_streamed_songs.png')


def top_ten_least_streamed_songs():
    conn = sqlite3.connect("music.db")
    query = "SELECT title, total_streams FROM most_streams WHERE total_streams != 0 ORDER BY total_streams ASC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    titles, streams = zip(*data)

    # create scatter plot
    plt.figure(figsize=(12, 8))
    cmap = get_cmap("Set1")
    colors = cmap(range(len(titles)))
    plt.scatter(titles, streams, color=colors, edgecolor='black', s=250)
    plt.xlabel('Titles', fontsize=18)
    plt.ylabel('Streams', fontsize=18)
    title = "Top 10 least streamed songs"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/least_streamed_songs.png')

def top_ten_most_streamed_songs_of_year(year):
    conn = sqlite3.connect("music.db")
    query = "SELECT title, most_streams_of_year.total_streams FROM most_streams JOIN most_streams_of_year ON most_streams.streams_id = most_streams_of_year.song_id WHERE year=2020 ORDER BY most_streams_of_year.total_streams DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    titles, streams = zip(*data)

    # create bar chart
    plt.figure(figsize=(12, 8))
    plt.bar(titles, streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Titles', fontsize=18)
    plt.ylabel('Streams', fontsize=18)
    title = "Top 10 most streamed songs of 2023"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    file = "./static/visualizations/" + year + ".png"
    plt.savefig(file)

def artists_with_most_songs_top_2000():
    conn = sqlite3.connect("music.db")

    query = "SELECT artist, COUNT(title) FROM most_streams JOIN most_streamed_artist ON most_streams.artist_id = most_streamed_artist.artist_id GROUP BY artist ORDER BY COUNT(title) DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    artists, songs = zip(*data)
    # create pie chart
    plt.figure(figsize=(12, 8))
    plt.pie(songs, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, textprops={'fontsize': 14})
    plt.axis('equal')
    title = "Artists with most songs in the top 2000"
    plt.title(title, fontsize=20, y=1.05)
    plt.tight_layout()
    plt.savefig('./static/visualizations/most_songs_pie_chart.png')

    # bar chart
    plt.figure(figsize=(12, 8))
    plt.bar(artists, songs, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Artists', fontsize=18)
    plt.ylabel('Number of Songs', fontsize=18)
    title = "Artists with most songs in the top 2000"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/most_songs_bar_chart.png')

def top_ten_most_streamed_albums():
    conn = sqlite3.connect("music.db")
    query = "SELECT album, streams FROM most_streamed_album ORDER BY streams DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    albums, streams = zip(*data)
    # create bar chart
    plt.figure(figsize=(12, 8))
    plt.bar(albums, streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Albums', fontsize=18)
    plt.ylabel('Streams', fontsize=18)
    title = "Top 10 most streamed albums"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/most_streamed_albums.png')

def top_ten_least_streamed_albums():
    conn = sqlite3.connect("music.db")
    query = "SELECT album, streams FROM most_streamed_album ORDER BY streams ASC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    albums, streams = zip(*data)
    # create scatter plot
    plt.figure(figsize=(12, 8))
    cmap = get_cmap("Set1")
    colors = cmap(range(len(albums)))
    plt.scatter(albums, streams, color=colors, edgecolor='black', s=250)
    plt.xlabel('Albums', fontsize=18) 
    plt.ylabel('Streams', fontsize=18)
    title = "Top 10 least streamed albums among the top 200"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/least_streamed_albums.png')

def artist_with_the_most_albums_in_top_200():
    conn = sqlite3.connect("music.db")
    query = "SELECT artist, COUNT(album) FROM most_streamed_album JOIN most_streamed_artist ON most_streamed_album.artist_id = most_streamed_artist.artist_id GROUP BY artist ORDER BY COUNT(album) DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    artists, albums = zip(*data)
    # create pie chart
    plt.figure(figsize=(12, 8))
    plt.pie(albums, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors, textprops={'fontsize': 14})
    plt.axis('equal')
    title = "Artists with most albums in the top 200"
    plt.title(title, fontsize=20, y=1.05)
    plt.tight_layout()
    plt.savefig('./static/visualizations/most_albums_pie_chart.png')


    # bar chart
    plt.figure(figsize=(12, 8))
    plt.bar(artists, albums, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Artists', fontsize=18)
    plt.ylabel('Number of Albums', fontsize=18)
    title = "Artists with most albums in the top 200"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    plt.yticks(fontsize=18)
    plt.tight_layout()
    plt.savefig('./static/visualizations/most_albums_bar_chart.png')

top_ten_most_streamed_songs()
top_ten_least_streamed_songs()
top_ten_most_streamed_songs_of_year("2023")
top_ten_most_streamed_songs_of_year("2022")
top_ten_most_streamed_songs_of_year("2021")
top_ten_most_streamed_songs_of_year("2020")
artists_with_most_songs_top_2000()
top_ten_most_streamed_albums()
top_ten_least_streamed_albums()
artist_with_the_most_albums_in_top_200()
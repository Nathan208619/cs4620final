import sqlite3
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import matplotlib.cm as cm  # Import the colormap module

def query_the_database(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        # print(rows)
        return rows
    except sqlite3.Error as e:
        print(e)

def top_ten_most_streamed_songs():
    conn = sqlite3.connect("music.db")
    query = "SELECT title, total_streams FROM most_streams WHERE streams_id <= 10 ORDER BY total_streams DESC"
    data = query_the_database(conn, query)
    conn.close()
    titles, streams = zip(*data)

    # create bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(titles, streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Titles')
    plt.ylabel('Streams')
    title = f"Top 10 most streamed songs"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
    plt.tight_layout()
    plt.savefig('./static/visualizations/most_streamed_songs.png')


def top_ten_least_streamed_songs():
    conn = sqlite3.connect("music.db")
    query = "SELECT title, total_streams FROM most_streams ORDER BY total_streams ASC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    titles, streams = zip(*data)

    # create scatter plot
    plt.figure(figsize=(15, 10))
    cmap = get_cmap("Set1")
    colors = cmap(range(len(titles)))
    plt.scatter(titles, streams, color=colors, edgecolor='black', s=250)
    plt.xlabel('Titles')
    plt.ylabel('Streams')
    title = f"Top 10 least streamed songs"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
    plt.tight_layout()
    plt.savefig('./static/visualizations/least_streamed_songs.png')

def top_ten_most_streamed_songs_of_year(year):
    conn = sqlite3.connect("music.db")
    query = "SELECT title, total_streams FROM most_streams_of_" + year + " WHERE streams_id <= 10 ORDER BY total_streams DESC"
    data = query_the_database(conn, query)
    conn.close()
    titles, streams = zip(*data)

    # create bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(titles, streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Titles')
    plt.ylabel('Streams')
    title = f"Top 10 most streamed songs of 2023"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
    plt.tight_layout()
    file = "./static/visualizations/" + year + ".png"
    plt.savefig(file)

def artists_with_most_songs_top_2000():
    conn = sqlite3.connect("music.db")
    query = "SELECT artist, COUNT(title) FROM most_streams GROUP BY artist ORDER BY COUNT(title) DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    artists, songs = zip(*data)
    # create pie chart
    plt.figure(figsize=(15, 10))
    plt.pie(songs, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
    title = "Artists with most songs in the top 2000"
    plt.title(title, fontsize=20)
    plt.tight_layout()
    plt.savefig('./static/visualizations/most_songs_pie_chart.png')

    # bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(artists, songs, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Artists')
    plt.ylabel('Songs')
    title = "Artists with most songs in the top 2000"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
    plt.tight_layout()
    plt.savefig('./static/visualizations/most_songs_bar_chart.png')

def top_ten_most_streamed_albums():
    conn = sqlite3.connect("music.db")
    query = "SELECT album, streams FROM most_streamed_album ORDER BY streams DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    albums, streams = zip(*data)
    # create bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(albums, streams, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Albums')
    plt.ylabel('Streams')
    title = "Top 10 most streamed albums"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
    plt.tight_layout()
    plt.savefig('./static/visualizations/most_streamed_albums.png')

def top_ten_least_streamed_albums():
    conn = sqlite3.connect("music.db")
    query = "SELECT album, streams FROM most_streamed_album ORDER BY streams ASC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    albums, streams = zip(*data)
    # create scatter plot
    plt.figure(figsize=(15, 10))
    cmap = get_cmap("Set1")
    colors = cmap(range(len(albums)))
    plt.scatter(albums, streams, color=colors, edgecolor='black', s=250)
    plt.xlabel('Albums')
    plt.ylabel('Streams')
    title = "Top 10 least streamed albums among the top 200"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
    plt.tight_layout()
    plt.savefig('./static/visualizations/least_streamed_albums.png')

def artist_with_the_most_albums_in_top_200():
    conn = sqlite3.connect("music.db")
    query = "SELECT artist, COUNT(album) FROM most_streamed_album GROUP BY artist ORDER BY COUNT(album) DESC LIMIT 10"
    data = query_the_database(conn, query)
    conn.close()
    artists, albums = zip(*data)
    # create pie chart
    plt.figure(figsize=(15, 10))
    plt.pie(albums, labels=artists, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
    title = "Artists with most albums in the top 200"
    plt.title(title, fontsize=20)
    plt.tight_layout()
    plt.savefig('./static/visualizations/most_albums_pie_chart.png')


    # bar chart
    plt.figure(figsize=(15, 10))
    plt.bar(artists, albums, color=cm.Paired.colors, edgecolor='black')
    plt.xlabel('Artists')
    plt.ylabel('Albums')
    title = "Artists with most albums in the top 200"
    plt.title(title, fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
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
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap


def query_the_database(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        # print(rows)
        return rows
    except sqlite3.Error as e:
        print(e)

def plot_bar_chart(artist):
    # Query the albums_streams table
    conn = sqlite3.connect("music.db")
    query = "SELECT album, streams FROM most_streamed_album WHERE artist=" + "'" + artist + "'"
    data = query_the_database(conn, query)
    conn.close()
    titles, album_streams = zip(*data)
    
    # Create the bar chart
    plt.figure(figsize=(15, 10))
    cmap = get_cmap("Set1")
    colors = cmap(range(len(titles)))
    plt.bar(titles, album_streams, color=colors, edgecolor='black')
    plt.xlabel('Titles')
    plt.ylabel('Album Streams')
    title = f"{artist}'s most streamed albums among the most popular in the world"
    plt.title(title, fontsize=20)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=18)  # Adjust the rotation angle as needed
    plt.tight_layout()
    plt.savefig('test2.png')


def plot_pie_chart(artist):

    # Query the most_streams table
    conn = sqlite3.connect("music.db")
    query = "SELECT title, total_streams FROM most_streams WHERE artist=" + "'" + artist + "'"
    data = query_the_database(conn, query)
    conn.close()
    titles, daily_streams = zip(*data)

    # Craft the and save the figure
    plt.figure(figsize=(30, 20))
    plt.pie(daily_streams, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.legend(titles, title='Track Legend', bbox_to_anchor=(1, 0.5), loc="center", fontsize='small')

    plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
    chart_title = f"{artist}'s most streamed albums among the most popular in the world"
    plt.title(chart_title, y=1.05, fontsize=20)
    plt.savefig('test.png')

# Example usage:
# data = [("Title 1", 500), ("Title 2", 700), ("Title 3", 300), ("Title 4", 900), ("Title 5", 400)]
# plot_bar_chart(data)
# plot_pie_chart(data)


def main():
    # Plot a pie chart
    artist = "Drake"
    plot_pie_chart(artist)
    plot_bar_chart(artist)

if __name__ == "__main__":
    main()

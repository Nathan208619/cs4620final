import sqlite3
import matplotlib.pyplot as plt


def query_most_streams(conn):
    try:
        c = conn.cursor()
        query = "SELECT title, daily_streams FROM most_streams ORDER BY daily_streams DESC LIMIT 10"
        c.execute(query)
        rows = c.fetchall()

        return rows
    except sqlite3.Error as e:
        print(e)

# def plot_bar_chart(data):
    # titles, daily_streams = zip(*data)

    # plt.figure(figsize=(10, 6))
    # plt.bar(titles, daily_streams, color='skyblue')

    # plt.xlabel('Titles')
    # plt.ylabel('Daily Streams')
    # plt.title('Top 10 Tracks by Daily Streams')

    # # Rotate x-axis labels for better readability
    # plt.xticks(rotation=45, ha='right')  # Adjust the rotation angle as needed
    # plt.tight_layout()

def plot_pie_chart(data):
    titles, daily_streams = zip(*data)

    plt.figure(figsize=(8, 8))
    plt.pie(daily_streams, labels=titles, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

    plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
    plt.title('Top 10 Tracks by Daily Streams')

# Example usage:
data = [("Title 1", 500), ("Title 2", 700), ("Title 3", 300), ("Title 4", 900), ("Title 5", 400)]
plot_pie_chart(data)


def main():
    # Assuming you already have a connection to the database
    conn = sqlite3.connect("music.db")

    # Query the most_streams table
    most_streams_data = query_most_streams(conn)

    # Plot a bar chart
    # plot_bar_chart(most_streams_data)

    # Plot a pie chart
    plot_pie_chart(most_streams_data)

    # save the chart as a png file
    plt.savefig('top_10_tracks.png')

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()

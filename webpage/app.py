from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import plotly.io as pio

app = Flask(__name__)

def execute_query(query):
    try:
        conn = sqlite3.connect("../music.db")
        print(query)
        c = conn.cursor()
        c.execute(query)
        result = c.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:
        print(e)
        return []
    
def artists_most_streamed_songs_bar_chart(artist_name):
    query = "SELECT title, total_streams FROM most_streams WHERE artist=" + "'" + artist_name + "'"
    result = execute_query(query)

    labels = [row[0] for row in result]
    values = [row[1] for row in result]
    print(labels)
    print(values)

    df = pd.DataFrame ({
        'category': ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5', 'Song 6', 'Song 7', 'Song 8'],
        'count': [10, 25, 15, 30, 20, 35, 25, 40]
    })

    fig = px.bar(df, x='category', y='count', title='Bar Chart')

# Adjustments for better readability
    fig.update_layout(
        width=1200,       # Set the width of the chart
        height=600,       # Set the height of the chart
        margin=dict(l=100, r=100, b=100, t=100),  # Adjust margins for more space
        xaxis=dict(tickangle=45),  # Rotate x-axis labels for better readability
    )

    pio.write_image(fig, file='index.png')

    

    # fig, ax = plt.subplots()
    # ax.bar(labels, values)
    # ax.set_xlabel('Songs')
    # ax.set_ylabel('Streams')
    # ax.set_title('Bar Chart for {}'.format(artist_name))
    # plt.update_layout(
    # width=1200,       # Set the width of the chart
    # height=600,       # Set the height of the chart
    # margin=dict(l=100, r=100, b=100, t=100),  # Adjust margins for more space
    # xaxis=dict(tickangle=45),  # Rotate x-axis labels for better readability
    # showlegend=False,  # Hide the legend
    # )

    # plt.xticks(rotation=45, ha='right')  # Adjust the rotation angle as needed
    # plt.tight_layout()
    # plt.savefig("artist_bar_chart.png")
    
    
    
    # return figure.to_json()



@app.route('/')
def main():
    return render_template('main.html')

@app.route('/artists', methods=['GET', 'POST'])
def artist_page():
    if request.method == 'POST':
        artist_name = request.form['artist_name']
        print(artist_name)
        chart = artists_most_streamed_songs_bar_chart(artist_name)
        print(chart)

        return render_template('artists.html', artist_name=artist_name)
    return render_template('artists.html')

@app.route('/songs', methods=['GET', 'POST'])
def song_page():
    if request.method == 'POST':
        song_name = request.form['song_name']
        # Perform visualization based on song_name using execute_query function
        # Example: result = execute_query("SELECT * FROM songs WHERE title=?", (song_name,))
        # Add your visualization logic here
        return render_template('songs', song_name=song_name)
    return render_template('songs.html')

@app.route('/albums', methods=['GET', 'POST'])
def album_page():
    if request.method == 'POST':
        album_name = request.form['album_name']
        # Perform visualization based on album_name using execute_query function
        # Example: result = execute_query("SELECT * FROM albums WHERE title=?", (album_name,))
        # Add your visualization logic here
        return render_template('albums', album_name=album_name)
    return render_template('albums.html')

if __name__ == '__main__':
    app.run(debug=True)

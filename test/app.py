from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

# Sample data
data = {'X': [1, 2, 3, 4, 5], 'Y': [10, 11, 14, 13, 15]}
df = pd.DataFrame(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_chart/<chart_type>')
def generate_chart(chart_type):
    if chart_type == 'line':
        fig = px.line(df, x='X', y='Y', title='Line Chart')
    elif chart_type == 'bar':
        fig = px.bar(df, x='X', y='Y', title='Bar Chart')
    else:
        return "Invalid chart type"

    graph_json = fig.to_json()
    return graph_json

if __name__ == '__main__':
    app.run(debug=True)

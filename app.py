from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Load processed data
    df = pd.read_csv('processed_standings.csv', index_col='race')

    # Generate plot
    plt.figure(figsize=(10, 6))
    for column in df.columns:
        plt.plot(df.index, df[column], marker='o', label=column)
    plt.title('F1 Standings 2023')
    plt.xlabel('Race')
    plt.ylabel('Position')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    # Convert plot to base64 for embedding in HTML
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()

    # Render HTML template with plot
    return render_template('index.html', plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)
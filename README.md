# F1 Standings Web Scraper and Visualization
 This will webscrape the 2023 race and ouptut the standings in a graph

Link to website: https://nguyen-william.github.io/f1standings-webscaper/

This project consists of a web scraper for F1 standings and a web-based visualization tool using Chart.js. The scraper fetches the latest F1 standings data, and the visualization tool displays the data in an interactive chart.

## Project Structure

f1-standings-visualization/                                                                            
├── index.html                                                                                                  
├── script.js                                                                                                  
├── standings.json                                                                                                
├── styles.css                                                                                                
├── scraper/                                                                                                
│ ├── init.py                                                                                                
│ ├── items.py                                                                                                
│ ├── middlewares.py                                                                                                
│ ├── pipelines.py                                                                                                
│ ├── settings.py                                                                                                
│ └── spiders/                                                                                                
│ ├── init.py                                                                                                
│ └── f1standingspider.py                                                                                                
├── processed_standings.csv                                                                                                
└── README.md                                                                                                

## Features
- Scrapes driver standings
- Collects data on player position, wins, podiums, and moreand races
- Exports data to CSV and JSON formats

## Setup

### Prerequisites

- Python 3.x
- `scrapy` and `pandas` libraries for the scraper.
- A web browser to view the visualization.

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/f1-standings-visualization.git
    cd f1-standings-visualization
    ```

2. **Set Up a Virtual Environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Python Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Frontend Dependencies**
    No additional dependencies are required for the frontend, as it uses CDN links for Chart.js.

## Usage

### Running the Web Scraper

1. **Navigate to the Scraper Directory**
    ```bash
    cd scraper
    ```

2. **Run the Scraper**
    ```bash
    scrapy crawl f1standingspider -o ../standings.json
    ```

    This will fetch the standings and save them to `standings.json`.

3. **Process the Data**
   
   After the scraper finishes running, the processed data will be automatically saved to `processed_standings.csv`.

### Viewing the Visualization

1. **Open the `index.html` file in your web browser.**
2. **Interact with the Chart**
    - Use the buttons to switch between line and bar chart views.

### Files

- **`index.html`**: The main HTML file for the visualization.
- **`script.js`**: Contains JavaScript code to fetch data and create the chart.
- **`standings.json`**: Contains the scraped F1 standings data.
- **`processed_standings.csv`**: Contains the processed standings data for visualization.
- **`styles.css`**: Contains the CSS styles for the visualization page.
- **`scraper/spiders/f1standingspider.py`**: The Python script for scraping F1 standings data.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [Scrapy](https://scrapy.org/) for the web scraping framework.
- [Pandas](https://pandas.pydata.org/) for data manipulation and analysis.
- [Chart.js](https://www.chartjs.org/) for the charting library.


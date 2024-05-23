import scrapy
import pandas as pd 

class F1standingspiderSpider(scrapy.Spider):
    name = "f1standingspider"
    allowed_domains = ["www.formula1.com"]
    start_urls = ["https://www.formula1.com/en/results.html/2023/races.html"]


    

    def parse(self, response):
        # Extract data for each race standings
        race_name = response.css('h1.ResultsArchiveTitle::text').get().strip()
        clean_race_name = race_name.replace("\n         - RACE RESULT", "")

        driver_rows = response.css('.resultsarchive-table tbody tr')
        for driver in driver_rows:
            driver_first_name = driver.css('.dark .hide-for-tablet::text').get()
            driver_last_name = driver.css('.dark .hide-for-mobile::text').get()

            yield {
                'race': clean_race_name,
                'position': driver.css('.dark::text').get(),
                'driver_name': f"{driver_first_name} {driver_last_name}",

            }

            # Extract race links from the <select> element
        race_options = response.css('select.resultsarchive-filter-form-select[name="meetingKey"] option::attr(value)').getall()
        
        # Filter out the "All" option and construct full URLs for each race
        race_links = [f'/en/results.html/2023/races/{option}/race-result.html' for option in race_options if option]
        
        for link in race_links:
            full_url = response.urljoin(link)
            yield response.follow(full_url, callback=self.parse)

        
    def closed(self, reason):
        # Load the scraped data from JSON
        data = pd.read_json('standings.json')

        # Combine first and last names
        data['driver'] = data['driver_name'].str.strip()

        # Process the data to create a DataFrame suitable for graphing
        df = data.pivot(index='race', columns='driver', values='position')

        # Save processed data to CSV
        df.to_csv('processed_standings.csv', index=True)

       
    
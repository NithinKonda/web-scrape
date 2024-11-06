import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData, EventMetrics
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, OnSiteOrRemoteFilters, SalaryBaseFilters
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)

# List to store job data
job_data = []

# Event handlers
def on_data(data: EventData):
    job_data.append({
        'title': data.title,
        'company': data.company,
        'company_link': data.company_link,
        'date': data.date,
        'link': data.link,
        'insights': data.insights,
        'description_length': len(data.description)
    })
    print(f'[ON_DATA] {data.title} at {data.company}')

def on_metrics(metrics: EventMetrics):
    print(f'[ON_METRICS] Processed {metrics.processed} jobs with {metrics.errors} errors')

def on_error(error):
    print(f'[ON_ERROR] {error}')

def on_end():
    print('[ON_END] Scraping finished')

# Scraper configuration
scraper = LinkedinScraper(
    chrome_executable_path=None,  
    headless=True,
    max_workers=1,
    slow_mo=1.5,
    page_load_timeout=60
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

# Define search queries
queries = [
    Query(
        options=QueryOptions(
            limit=30  # Adjust limit as required
        )
    ),
    Query(
        query='Software Engineer',
        options=QueryOptions(
            locations=['India', 'Hyderabad'],
            apply_link=True,
            skip_promoted_jobs=True,
            page_offset=0,
            limit=10,
            filters=QueryFilters(
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                type=[TypeFilters.FULL_TIME],
                on_site_or_remote=[OnSiteOrRemoteFilters.REMOTE],
                experience=[ExperienceLevelFilters.MID_SENIOR],
                base_salary=SalaryBaseFilters.SALARY_100K
            )
        )
    ),
]

# Run the scraper with defined queries
scraper.run(queries)

# Save job data to CSV
if job_data:
    df = pd.DataFrame(job_data)
    df.to_csv('linkedin_jobs.csv', index=False, encoding='utf-8')
    print("Data saved to linkedin_jobs.csv")
else:
    print("No job data scraped.")

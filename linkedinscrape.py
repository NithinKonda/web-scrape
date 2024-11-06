# # import requests
# # from bs4 import BeautifulSoup
# # import math
# # import pandas as pd
# # l=[]
# # o={}
# # k=[]
# # headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
# # target_url=' https://www.linkedin.com/jobs/search/?currentJobId=3040897042&geoId=102713980&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true'
# # for i in range(0,math.ceil(117/25)):

# #     res = requests.get(target_url.format(i))
# #     soup=BeautifulSoup(res.text,'html.parser')
# #     alljobs_on_this_page=soup.find_all("li")
# #     print(len(alljobs_on_this_page))
# #     for x in range(0,len(alljobs_on_this_page)):
# #         jobid = alljobs_on_this_page[x].find("div",{"class":"base-card"}).get('data-entity-urn').split(":")[3]
# #         l.append(jobid)

# # target_url='https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
# # for j in range(0,len(l)):

# #     resp = requests.get(target_url.format(l[j]))
# #     soup=BeautifulSoup(resp.text,'html.parser')

# #     try:
# #         o["company"]=soup.find("div",{"class":"top-card-layout__card"}).find("a").find("img").get('alt')
# #     except:
# #         o["company"]=None

# #     try:
# #         o["job-title"]=soup.find("div",{"class":"top-card-layout__entity-info"}).find("a").text.strip()
# #     except:
# #         o["job-title"]=None

# #     try:
# #         o["level"]=soup.find("ul",{"class":"description__job-criteria-list"}).find("li").text.replace("Seniority level","").strip()
# #     except:
# #         o["level"]=None



# #     k.append(o)
# #     o={}

# # df = pd.DataFrame(k)
# # df.to_csv('linkedinjobs.csv', index=False, encoding='utf-8')
# # print(k)


import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData, EventMetrics
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, \
    OnSiteOrRemoteFilters, SalaryBaseFilters

# Change root logger level (default is WARN)
logging.basicConfig(level=logging.INFO)


# Fired once for each successfully processed job
def on_data(data: EventData):
    print('[ON_DATA]', data.title, data.company, data.company_link, data.date, data.link, data.insights,
          len(data.description))


# Fired once for each page (25 jobs)
def on_metrics(metrics: EventMetrics):
    print('[ON_METRICS]', str(metrics))


def on_error(error):
    print('[ON_ERROR]', error)


def on_end():
    print('[ON_END]')


scraper = LinkedinScraper(
    chrome_executable_path=None,  # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver)
    chrome_binary_location=None,  # Custom path to Chrome/Chromium binary (e.g. /foo/bar/chrome-mac/Chromium.app/Contents/MacOS/Chromium)
    chrome_options=None,  # Custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=0.5,  # Slow down the scraper to avoid 'Too many requests 429' errors (in seconds)
    page_load_timeout=100  # Page load timeout (in seconds)    
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

queries = [
    Query(
        options=QueryOptions(
            limit=27  # Limit the number of jobs to scrape.            
        )
    ),
    Query(
        query='Engineer',
        options=QueryOptions(
            locations=['India', 'Hyderabad'],
            apply_link=True,  # Try to extract apply link (easy applies are skipped). If set to True, scraping is slower because an additional page must be navigated. Default to False.
            skip_promoted_jobs=True,  # Skip promoted jobs. Default to False.
            page_offset=2,  # How many pages to skip
            limit=5,
            filters=QueryFilters(
                company_jobs_url='https://www.linkedin.com/jobs/search/?f_C=1441%2C17876832%2C791962%2C2374003%2C18950635%2C16140%2C10440912&geoId=102713980',  # Filter by companies.                
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                on_site_or_remote=[OnSiteOrRemoteFilters.REMOTE],
                experience=[ExperienceLevelFilters.MID_SENIOR],
                base_salary=SalaryBaseFilters.SALARY_100K
            )
        )
    ),
]

scraper.run(queries)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver (replace with the path to your WebDriver)
driver = webdriver.Chrome()

# URL to scrape
url = "https://www.linkedin.com/jobs/search?keywords=Data%20Science&location=Hyderabad&position=1&pageNum=0"
driver.get(url)

# Wait for the page to fully load by waiting for the job card to appear
try:
    # Wait for the first job card to appear on the page
    job_card_locator = (By.CLASS_NAME, "base-search-card__info")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(job_card_locator))
except Exception as e:
    print(f"Error while waiting for page load: {e}")
    driver.quit()

# Get page source and parse with BeautifulSoup
html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")

# Initialize a list to hold job details
jobs = []

# Extract job information
for job_entry in soup.find_all("div", class_="base-search-card__info"):
    title_element = job_entry.find("h3", class_="base-search-card__title")
    title = title_element.get_text(strip=True) if title_element else "N/A"
    
    company_element = job_entry.find("a", class_="hidden-nested-link")
    company = company_element.get_text(strip=True) if company_element else "N/A"
    
    location_element = job_entry.find("span", class_="job-search-card__location")
    location = location_element.get_text(strip=True) if location_element else "N/A"
    
    # Extract the job link
    job_link_element = job_entry.find("a", class_="base-card__full-link")
    job_link = job_link_element['href'] if job_link_element else "N/A"

    jobs.append({
        "Title": title,
        "Company": company,
        "Location": location,
        "Job Link": job_link
    })

# Close the WebDriver
driver.quit()

# Print job details
for job in jobs:
    print(f"Title: {job['Title']}")
    print(f"Company: {job['Company']}")
    print(f"Location: {job['Location']}")
    print(f"Job Link: {job['Job Link']}")
    print("-" * 40)


#retunring but login fail


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import time
# import random

# # Set up Chrome options for Selenium
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Comment this line to see the browser window
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# # Initialize the WebDriver
# driver = webdriver.Chrome(service=Service("/home/lenovo/Downloads/chromedriver-linux64/chromedriver"), options=chrome_options)

# try:
#     # Step 1: Log into LinkedIn
#     driver.get("https://www.linkedin.com/login")
#     time.sleep(2)

#     # Enter email and password
#     username = driver.find_element(By.ID, "username")
#     password = driver.find_element(By.ID, "password")
#     username.send_keys("nithinkonda142@gmail.com")
#     password.send_keys("makedinini_142")
#     password.send_keys(Keys.RETURN)
#     time.sleep(3)  # Wait for login to complete

#     # Step 2: Go to the jobs search page
#     driver.get("https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Hyderabad&position=1&pageNum=0")
#     time.sleep(3)  # Wait for the page to load

#     # Step 3: Parse the page content with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")

#     # Initialize a list to hold job details
#     jobs = []

#     # Step 4: Extract job information
#     for job_entry in soup.find_all("div", class_="base-search-card__info"):
#         try:
#             title = job_entry.find("h3", class_="base-search-card__title").get_text(strip=True)
#             company = job_entry.find("a", class_="hidden-nested-link").get_text(strip=True)
#             location = job_entry.find("span", class_="job-search-card__location").get_text(strip=True)

#             jobs.append({
#                 "Title": title,
#                 "Company": company,
#                 "Location": location
#             })

#         except AttributeError as e:
#             print(f"Error parsing job entry: {e}")
#             continue

#     # Step 5: Print out the job details
#     for job in jobs:
#         print(f"Title: {job['Title']}")
#         print(f"Company: {job['Company']}")
#         print(f"Location: {job['Location']}")
#         print("-" * 40)

# finally:
#     # Step 6: Quit the driver
#     driver.quit()



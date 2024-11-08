# import json

# # Load JSON data from a file
# with open("jobs.json", "r", encoding="utf-8") as file:
#     parsed_data = json.load(file)  # This reads and parses the JSON data

# # Extract and print the job title, organization name, and public URL
# for job in parsed_data["pageProps"]["jobs"]:
#     title = job["title"]
#     organization_name = job["organization"]["name"]
#     public_url = job["public_url"]

#     print(f"Title: {title}")
#     print(f"Organization: {organization_name}")
#     print(f"URL: {public_url}")
#     print("-" * 30)




# from bs4 import BeautifulSoup
# import json

# # Load HTML from a file or a string (replace 'internshala.html' with your HTML file name)
# with open("jobs.html", "r", encoding="utf-8") as file:    
#     html_content = file.read()

# # Parse the HTML with BeautifulSoup
# soup = BeautifulSoup(html_content, "html.parser")

# # Find the script tag with id="__NEXT_DATA__"
# script_tag = soup.find("script", id="__NEXT_DATA__")

# # Check if the script tag is found
# if script_tag:
#     # Load the JSON data from the script tag content
#     json_data = json.loads(script_tag.string)
    
#     # Now we can access job details as usual
#     for job in json_data["props"]["pageProps"]["jobs"]:
#         title = job["title"]
#         organization_name = job["organization"]["name"]
#         public_url = job["public_url"]

#         print(f"Title: {title}")
#         print(f"Organization: {organization_name}")
#         print(f"URL: {public_url}")
#         print("-" * 30)
# else:
#     print("Script tag with id '__NEXT_DATA__' not found.")

#//FROM ERHERHEHRHERHEHRHEHRHEH












# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import subprocess
# import json


# jobs = []
# # URL to fetch HTML content from
# url = "https://apna.co/jobs/dep_data_science_analytics-jobs"


# print("APNA")

# # Use curl to get the HTML content of the page
# curl_command = f"curl -s {url}"
# html_content = subprocess.check_output(curl_command, shell=True, text=True)

# # Parse the HTML with BeautifulSoup
# soup = BeautifulSoup(html_content, "html.parser")

# # Find the script tag with id="__NEXT_DATA__"
# script_tag = soup.find("script", id="__NEXT_DATA__")

# # Check if the script tag is found
# if script_tag:
#     # Load the JSON data from the script tag content
#     json_data = json.loads(script_tag.string)
    
#     # Now we can access job details as usual
#     for job in json_data["props"]["pageProps"]["jobs"]:
#         title = job["title"]
#         organization_name = job["organization"]["name"]
#         public_url = job["public_url"]



#         jobs.append({
#         "Title": title,
#         "Company": organization_name,
#         "Location": "None",
#         "Job Link": public_url
#     })
#         print(f"Title: {title}")
#         print(f"Organization: {organization_name}")
#         print(f"URL: {public_url}")
#         print("-" * 30)
# else:
#     print("Script tag with id '__NEXT_DATA__' not found.")






# driver = webdriver.Chrome()

# # URL to scrape
# url = "https://www.linkedin.com/jobs/search?keywords=Data%20Science&location=Hyderabad&position=1&pageNum=0"
# driver.get(url)

# # Wait for the page to fully load by waiting for the job card to appear
# try:
#     # Wait for the first job card to appear on the page
#     job_card_locator = (By.CLASS_NAME, "base-search-card__info")
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located(job_card_locator))
# except Exception as e:
#     print(f"Error while waiting for page load: {e}")
#     driver.quit()

# # Get page source and parse with BeautifulSoup
# html_content = driver.page_source
# soup = BeautifulSoup(html_content, "html.parser")

# # Initialize a list to hold job details


# # Extract job information
# for job_entry in soup.find_all("div", class_="base-search-card__info"):
#     title_element = job_entry.find("h3", class_="base-search-card__title")
#     title = title_element.get_text(strip=True) if title_element else "N/A"
    
#     company_element = job_entry.find("a", class_="hidden-nested-link")
#     company = company_element.get_text(strip=True) if company_element else "N/A"
    
#     location_element = job_entry.find("span", class_="job-search-card__location")
#     location = location_element.get_text(strip=True) if location_element else "N/A"
    
#     # Extract the job link
#     job_link_element = job_entry.find("a", class_="base-card__full-link")
#     job_link = job_link_element.get('href') if job_link_element else "N/A"

#     jobs.append({
#         "Title": title,
#         "Company": company,
#         "Location": location,
#         "Job Link": job_link
#     })

# # Close the WebDriver
# driver.quit()

# # Print job details
# for job in jobs:
#     print(f"Title: {job['Title']}")
#     print(f"Company: {job['Company']}")
#     print(f"Location: {job['Location']}")
#     print(f"Job Link: {job['Job Link']}")
#     print("-" * 40)





# print("\n\n\nINTERNSHALA")



# url = "https://internshala.com/jobs/data-science-jobs"

# # Use curl to get the HTML content of the page
# curl_command = f"curl -s {url}"  # The -s flag silences the progress output
# html_content = subprocess.check_output(curl_command, shell=True, text=True)

# # Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(html_content, "html.parser")

# # Initialize a list to hold job details
# jobs = []

# # Extract job information
# for job_entry in soup.find_all("div", class_="individual_internship"):
#     try:
#         title_element = job_entry.find("a", class_="job-title-href")
#         title = title_element.get_text(strip=True)
#         # Extract the href attribute
#         href = title_element.get('href')  # This gets the href attribute value
        
#         company = job_entry.find("p", class_="company-name").get_text(strip=True)
#         location = job_entry.find("p", class_="locations").get_text(strip=True).replace(" ", "")
#         pay = job_entry.find("span", class_="desktop").get_text(strip=True)
        
#         jobs.append({
#             "Title": title,
#             "Company": company,
#             "Location": location,
#             # "Pay": pay,
#             "Job Link": "https://internshala.com/"+href  # Add the href to the dictionary
            
#         })
#     except Exception as e:
#             print(f"Error processing job entry: {e}")
#     for job in jobs:
#             print(f"Title: {job['Title']}")
#             print(f"Company: {job['Company']}")
#             print(f"Location: {job['Location']}")
#             print(f"Pay: {job['Pay']}")
#             print(f"Link : {job['Job Link']}")
#             print("-" * 40)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import subprocess
import json

# List to store job details from all sources
jobs = []

# ---------- APNA ----------
url_apna = "https://apna.co/jobs/dep_data_science_analytics-jobs"
html_content_apna = subprocess.check_output(f"curl -s {url_apna}", shell=True, text=True)
soup_apna = BeautifulSoup(html_content_apna, "html.parser")

script_tag = soup_apna.find("script", id="__NEXT_DATA__")
if script_tag:
    json_data = json.loads(script_tag.string)
    for job in json_data["props"]["pageProps"]["jobs"]:
        jobs.append({
            "Title": job["title"],
            "Company": job["organization"]["name"],
            "Location": "N/A",  # Apna may not provide location
            "Job Link": job["public_url"]
        })

# ---------- LINKEDIN ----------
def scrape_linkedin_jobs():
    driver = webdriver.Chrome()
    url_linkedin = "https://www.linkedin.com/jobs/search?keywords=Data%20Science&location=Hyderabad&position=1&pageNum=0"
    driver.get(url_linkedin)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "base-search-card__info")))

    html_content_linkedin = driver.page_source
    soup_linkedin = BeautifulSoup(html_content_linkedin, "html.parser")

    for job_entry in soup_linkedin.find_all("div", class_="base-search-card__info"):
        job_link = job_entry.find("a", class_="base-card__full-link")
        if job_link:
            job_link = job_link.get('href')
        else:
            job_link = ""

        company_element = job_entry.find("a", class_="hidden-nested-link")
        if company_element:
            company = company_element.get_text(strip=True)
        else:
            company = "N/A"

        jobs.append({
            "Title": job_entry.find("h3", class_="base-search-card__title").get_text(strip=True),
            "Company": company,
            "Location": job_entry.find("span", class_="job-search-card__location").get_text(strip=True),
            "Job Link": job_link
        })

    driver.quit()

# ---------- INTERNSHALA ----------
url_internshala = "https://internshala.com/jobs/data-science-jobs"
html_content_internshala = subprocess.check_output(f"curl -s {url_internshala}", shell=True, text=True)
soup_internshala = BeautifulSoup(html_content_internshala, "html.parser")

for job_entry in soup_internshala.find_all("div", class_="individual_internship"):
    try:
        title = job_entry.find("a", class_="job-title-href").get_text(strip=True)
        href = job_entry.find("a", class_="job-title-href").get('href')
        company = job_entry.find("p", class_="company-name").get_text(strip=True)
        location = job_entry.find("p", class_="locations").get_text(strip=True).replace(" ", "")
        
        jobs.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "Job Link": "https://internshala.com" + href
        })
    except Exception as e:
        print(f"Error processing job entry in Internshala: {e}")

# Print all jobs in the specified format for FastAPI to capture
print(json.dumps(jobs))
import subprocess
from bs4 import BeautifulSoup
print("\n\n\nINTERNSHALA")



url = "https://www.linkedin.com/jobs/search?keywords=Data%20Science&location=Hyderabad&position=1&pageNum=0"

# Use curl to get the HTML content of the page
curl_command = f"curl -s {url}"  # The -s flag silences the progress output
html_content = subprocess.check_output(curl_command, shell=True, text=True)

# Parse the HTML content with BeautifulSoup
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
    job_link = job_link_element.get('href') if job_link_element else "N/A"

    jobs.append({
        "Title": title,
        "Company": company,
        "Location": location,
        "Job Link": job_link
    })
    for job in jobs:
        print(f"Title: {job['Title']}")
        print(f"Company: {job['Company']}")
        print(f"Location: {job['Location']}")
        print(f"Job Link: {job['Job Link']}")
        print("-" * 40)
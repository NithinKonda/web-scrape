import subprocess
from bs4 import BeautifulSoup
print("\n\nLINKEDIN")



url = "https://www.linkedin.com/jobs/search?keywords=Software+Engineer&location=Hyderabad"

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
    print(title_element)
    title = title_element.get_text(strip=True)
    # Extract the href attribute
      # This gets the href attribute value
    
    company = job_entry.find("a", class_="hidden-nested-link").get_text(strip=True)
    location = job_entry.find("span", class_="job-search-card__location").get_text(strip=True).replace(" ", "")
    # pay = job_entry.find("span", class_="desktop").get_text(strip=True)
    
    jobs.append({
        "Title": title,
        "Company": company,
        "Location": location,
        # "Pay": pay,
        # "Link": href  # Add the href to the dictionary
    })
    for job in jobs:
        print(f"Title: {job['Title']}")
        print(f"Company: {job['Company']}")
        print(f"Location: {job['Location']}")
        # print(f"Pay: {job['Pay']}")
        # print(f"Link : {job['Link']}")
        print("-" * 40)
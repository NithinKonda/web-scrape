# import subprocess
# from bs4 import BeautifulSoup

# # Define the URL you want to scrape
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
#     title = job_entry.find("a", class_="job-title-href").get_text(strip=True)
#     company = job_entry.find("p", class_="company-name").get_text(strip=True)
#     location = job_entry.find("p", class_="locations").get_text(strip=True).replace(" ", "")  # Clean up location
#     pay = job_entry.find("span", class_="desktop").get_text(strip=True)  # Assuming the salary is in the desktop span
    
#     jobs.append({
#         "Title": title,
#         "Company": company,
#         "Location": location,
#         "Pay": pay
#     })
#     print(jobs)




# import subprocess
# from bs4 import BeautifulSoup

# # Define the URL you want to scrape
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
#     title = job_entry.find("a", class_="job-title-href").get_text(strip=True)
#     company = job_entry.find("p", class_="company-name").get_text(strip=True)
#     location = job_entry.find("p", class_="locations").get_text(strip=True).replace(" ", "")  # Clean up location
#     pay = job_entry.find("span", class_="desktop").get_text(strip=True)  # Assuming the salary is in the desktop span
    
#     jobs.append({
#         "Title": title,
#         "Company": company,
#         "Location": location,
#         "Pay": pay,
#     })
#     print(jobs)



import subprocess
from bs4 import BeautifulSoup

# Define the URL you want to scrape
url = "https://internshala.com/jobs/data-science-jobs"

# Use curl to get the HTML content of the page
curl_command = f"curl -s {url}"  # The -s flag silences the progress output
html_content = subprocess.check_output(curl_command, shell=True, text=True)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Initialize a list to hold job details
jobs = []

# Extract job information
for job_entry in soup.find_all("div", class_="individual_internship"):
    title_element = job_entry.find("a", class_="job-title-href")
    title = title_element.get_text(strip=True)
    # Extract the href attribute
    href = title_element.get('href')  # This gets the href attribute value
    
    company = job_entry.find("p", class_="company-name").get_text(strip=True)
    location = job_entry.find("p", class_="locations").get_text(strip=True).replace(" ", "")
    pay = job_entry.find("span", class_="desktop").get_text(strip=True)
    
    jobs.append({
        "Title": title,
        "Company": company,
        "Location": location,
        "Pay": pay,
        "Link": href  # Add the href to the dictionary
    })
    for job in jobs:
        print(f"Title: {job['Title']}")
        print(f"Company: {job['Company']}")
        print(f"Location: {job['Location']}")
        print(f"Pay: {job['Pay']}")
        print(f"Link : {job['Link']}")
        print("-" * 40)
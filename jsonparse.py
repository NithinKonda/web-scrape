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




import subprocess
from bs4 import BeautifulSoup
import json

# URL to fetch HTML content from
url = "https://apna.co/jobs/dep_data_science_analytics-jobs"


print("APNA")

# Use curl to get the HTML content of the page
curl_command = f"curl -s {url}"
html_content = subprocess.check_output(curl_command, shell=True, text=True)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the script tag with id="__NEXT_DATA__"
script_tag = soup.find("script", id="__NEXT_DATA__")

# Check if the script tag is found
if script_tag:
    # Load the JSON data from the script tag content
    json_data = json.loads(script_tag.string)
    
    # Now we can access job details as usual
    for job in json_data["props"]["pageProps"]["jobs"]:
        title = job["title"]
        organization_name = job["organization"]["name"]
        public_url = job["public_url"]

        print(f"Title: {title}")
        print(f"Organization: {organization_name}")
        print(f"URL: {public_url}")
        print("-" * 30)
else:
    print("Script tag with id '__NEXT_DATA__' not found.")




print("\n\n\nINTERNSHALA")



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
        "Link": "https://internshala.com/"+href  # Add the href to the dictionary
    })
    for job in jobs:
        print(f"Title: {job['Title']}")
        print(f"Company: {job['Company']}")
        print(f"Location: {job['Location']}")
        print(f"Pay: {job['Pay']}")
        print(f"Link : {job['Link']}")
        print("-" * 40)






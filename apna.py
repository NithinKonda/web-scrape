from bs4 import BeautifulSoup

# Load the HTML content from the file or directly from a curl command
with open("jobs.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Assuming there are HTML tags with class names or attributes for job data
jobs = []
for job_entry in soup.find_all("div", class_="job-entry"):  # Adjust selector as needed
    title = job_entry.find("h2", class_="title").get_text(strip=True)
    company = job_entry.find("span", class_="company-name").get_text(strip=True)
    location = job_entry.find("span", class_="job-location").get_text(strip=True)
    min_salary = job_entry.find("span", class_="min-salary").get_text(strip=True)
    max_salary = job_entry.find("span", class_="max-salary").get_text(strip=True)
    
    jobs.append({
        "Title": title,
        "Company": company,
        "Location": location,
        "Pay": f"{min_salary} - {max_salary}"   
    })

print("Hello World")
for job in jobs:
    print(job)
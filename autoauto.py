import subprocess
from bs4 import BeautifulSoup
import schedule
import time

def fetch_jobs():
    url = "https://internshala.com/jobs/data-science-jobs"
    curl_command = f"curl -s {url}"
    html_content = subprocess.check_output(curl_command, shell=True, text=True)
    soup = BeautifulSoup(html_content, "html.parser")

    jobs = []
    for job_entry in soup.find_all("div", class_="individual_internship"):
        title = job_entry.find("a", class_="job-title-href").get_text(strip=True)
        company = job_entry.find("p", class_="company-name").get_text(strip=True)
        location = job_entry.find("p", class_="locations").get_text(strip=True).replace(" ", "")
        pay = job_entry.find("span", class_="desktop").get_text(strip=True)
        jobs.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "Pay": pay
        })
    print(jobs)


# Schedule the job to run every 6 hours
schedule.every(5).seconds.do(fetch_jobs)

# Keep the script running to execute the schedule
while True:
    schedule.run_pending()
    time.sleep(1)

from bs4 import BeautifulSoup

with open("testt.html", "r", encoding="utf-8") as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, "html.parser")


jobs = []
for job_entry in soup.find_all("div", class_="individual_internship"):
    title = job_entry.find("a", class_="job-title-href").get_text(strip=True)
    company = job_entry.find("p", class_="company-name").get_text(strip=True)
    location = job_entry.find("p", class_="locations").get_text(strip=True).replace(" ", "")  # Clean up location
    pay = job_entry.find("span", class_="desktop").get_text(strip=True)  # Assuming the salary is in the desktop span
    
    jobs.append({
        "Title": title,
        "Company": company,
        "Location": location,
        "Pay": pay
    })
    print(jobs)
print(type(jobs))
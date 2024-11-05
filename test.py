from bs4 import BeautifulSoup

html_content = """
<div class="company">
    <h3 class="job-internship-name">
        <a class="job-title-href" href="/job/details/fresher-data-analytics-executive-job-in-gurgaon-at-spectral-consultants1730534693" target="_blank">Data Analytics Executive</a>
    </h3>
    <div class="heading_6 company_name">
        <div class="company_and_premium">
            <p class="company-name">
                Spectral Consultants
            </p>
        </div>
    </div>
</div>
"""

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract the job title and company name
job_title = soup.find("a", class_="job-title-href").get_text(strip=True)
company_name = soup.find("p", class_="company-name").get_text(strip=True)

print("Job Title:", job_title)
print("Company Name:", company_name)

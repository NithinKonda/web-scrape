import requests
import json
from bs4 import BeautifulSoup

def fetch_apna_jobs(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the script tag containing JSON data
        script_tag = soup.find("script", id="__NEXT_DATA__")
        if not script_tag:
            print("No job data found on the page.")
            return []
        
        # Extract and parse the JSON data
        json_data = json.loads(script_tag.string)
        jobs = []
        
        # Extract job details
        for job in json_data.get("props", {}).get("pageProps", {}).get("jobs", []):
            jobs.append({
                "Title": job.get("title", "N/A"),
                "Company": job.get("organization", {}).get("name", "N/A"),
                "Location": "N/A",  # Location may not be provided in Apna's data
                "Job Link": job.get("public_url", "N/A")
            })
        
        return jobs
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Apna: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")
        return []

if __name__ == "__main__":
    url_apna = "https://apna.co/jobs/dep_data_science_analytics-jobs"
    jobs = fetch_apna_jobs(url_apna)
    
    # Print job data as a formatted JSON string
    print(json.dumps(jobs, indent=4))

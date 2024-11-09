from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from subprocess import check_output


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


import json

def parse_output(output):
    try:
        jobs = json.loads(output)
        return {"fetched jobs": jobs}
    except Exception as e:
        return {"error": str(e)}


@app.get("/run-script")
def run_script():
    print("Calling run_script function...")
    try:
        # Call the LinkedIn scraping function here

        result = check_output(["python3", "jsonparse.py"], text=True)
        print("Raw output from jsonparse.py:", result)
        return parse_output(result)
    except Exception as e:
        return {"error": str(e)}
# def parse_output(output):
#     print("Raw Output:", output)  # Add this line to check the raw output
    
#     jobs = []
#     job = {}
#     lines = output.splitlines()  # This ensures each line is processed separately
    
#     for line in lines:
#         print("Processing line:", line)  # Add this line to debug each line
        
#         if line.startswith("Title"):
#             job["Title"] = line.replace("Title", "").strip()
#         elif line.startswith("Company"):
#             job["Company"] = line.replace("Company", "").strip()
#         elif line.startswith("Location"):
#             job["Location"] = line.replace("Location", "").strip()
#         elif line.startswith("Job Link"):
#             job["Job Link"] = line.replace("Job Link", "").strip()
#         else:
#             if job:
#                 jobs.append(job)
#                 job = {}
    
#     if job:  # In case there's a final job left to append
#         jobs.append(job)
    
#     print("Parsed Jobs:", jobs)  # Add this line to check the parsed jobs
    
#     return jobs

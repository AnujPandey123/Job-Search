# jobscraper.py
from serpapi import GoogleSearch
import time

def serpapi_search_jobs(api_key, query, location=None, num=10):
    params = {
        "engine": "google_jobs",
        "q": query,
        "api_key": api_key,
        "limit": num
    }
    if location:
        params["location"] = location

    search = GoogleSearch(params)
    res = search.get_dict()
    jobs = []
    if "jobs_results" in res:
        for j in res.get("jobs_results", []):
            job_id = j.get("id") or j.get("link") or (j.get("title") + j.get("company_name", ""))
            jobs.append({
                "job_id": job_id,
                "title": j.get("title"),
                "url": j.get("link"),
                "company": j.get("company_name"),
                "snippet": j.get("description") or j.get("snippet"),
                "found_at": time.strftime("%Y-%m-%d %H:%M:%S")
            })
    return jobs

def find_jobs_for_keywords(api_key, keywords, locations):
    all_jobs = []
    for kw in keywords:
        for loc in locations:
            query = f"{kw} {loc}"
            results = serpapi_search_jobs(api_key, query, loc)
            for job in results:
                job["keyword"] = kw
                job["location"] = loc
                all_jobs.append(job)
    return all_jobs

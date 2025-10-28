# main.py
from apscheduler.schedulers.blocking import BlockingScheduler
from config import SERPAPI_KEY, KEYWORDS, LOCATIONS, POLL_INTERVAL_MIN
from db import MongoDB
from jobscraper import find_jobs_for_keywords
from notifier import send_email
import traceback

db = MongoDB()

def job_check():
    try:
        results = find_jobs_for_keywords(SERPAPI_KEY, KEYWORDS, LOCATIONS)
        new_jobs = []
        for job in results:
            if not db.is_seen(job["job_id"]):
                db.mark_seen(job)
                new_jobs.append(job)

        if new_jobs:
            message = "\n".join([
                f"{i+1}. {j['title']} - {j.get('company','')}\n   {j['url']}\n   ({j['keyword']} | {j['location']})"
                for i, j in enumerate(new_jobs)
            ])
            send_email(f"🔔 {len(new_jobs)} new job(s) found!", message)
            print(f"✅ {len(new_jobs)} new jobs sent.")
        else:
            print("No new jobs found.")
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()

if __name__ == "__main__":
    job_check()
    scheduler = BlockingScheduler()
    scheduler.add_job(job_check, 'interval', minutes=POLL_INTERVAL_MIN)
    print(f"⏳ Job search assistant running every {POLL_INTERVAL_MIN} minutes...")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Stopped.")

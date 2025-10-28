# main.py
from apscheduler.schedulers.blocking import BlockingScheduler
from config import SERPAPI_KEY, KEYWORDS, LOCATIONS, POLL_INTERVAL_MIN
from db import MongoDB
from jobscraper import find_jobs_for_keywords
from notifier import send_notification
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
            send_notification(f"{len(new_jobs)} new job(s) found!", new_jobs)
            print(f"✅ Sent {len(new_jobs)} new jobs to Telegram.")
        else:
            print("No new jobs found.")
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()

if __name__ == "__main__":
    job_check()
    scheduler = BlockingScheduler()
    scheduler.add_job(job_check, 'interval', minutes=POLL_INTERVAL_MIN)
    print(f"🤖 Job assistant running — checking every {POLL_INTERVAL_MIN} minutes...")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Stopped.")

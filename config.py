# config.py
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB", "jobassistant")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "seen_jobs")

SERPAPI_KEY = os.getenv("SERPAPI_KEY")
POLL_INTERVAL_MIN = int(os.getenv("POLL_INTERVAL_MIN", "30"))
KEYWORDS = [k.strip() for k in os.getenv("KEYWORDS", "software engineer intern").split(",")]
LOCATIONS = [l.strip() for l in os.getenv("LOCATIONS", "Noida,Remote").split(",")]

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
ALERT_RECIPIENT = os.getenv("ALERT_RECIPIENT", SMTP_USER)

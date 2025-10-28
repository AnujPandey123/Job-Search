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

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

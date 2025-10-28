# notifier.py
import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("⚠️ Telegram credentials not set in .env")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "disable_web_page_preview": True
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print("⚠️ Failed to send Telegram message:", response.text)
    except Exception as e:
        print("Error sending Telegram message:", e)

def send_notification(subject, jobs):
    message = f"🔔 {subject}\n\n"
    for i, job in enumerate(jobs, start=1):
        message += f"{i}. {job['title']} - {job.get('company','')}\n"
        message += f"{job['url']}\n"
        message += f"({job['keyword']} | {job['location']})\n\n"
    send_telegram_message(message)

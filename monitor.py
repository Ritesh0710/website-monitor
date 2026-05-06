import requests
import os

# ======================
# CONFIG
# ======================

URL = "https://google.com"

TARGET_TEXT = "search"

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ======================


def send_telegram(msg):

    api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    requests.post(api_url, data=payload)


def check_website():

    try:

        response = requests.get(URL, timeout=15)

        html = response.text.lower()

        if TARGET_TEXT.lower() in html:

            send_telegram(
                f"🚨 WEBSITE IS LIVE!\n{URL}"
            )

            print("ALERT SENT")

        else:
            print("Still waiting...")

    except Exception as e:
        print("ERROR:", e)


if __name__ == "__main__":
    check_website()

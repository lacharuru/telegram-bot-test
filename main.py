import requests

TELEGRAM_BOT_TOKEN = "xxxxxx" # bot token (be sure to copy-paste it correctly)
CHAT_ID = "xxxxxx" # Telegram Chat ID, you can use a group ID 

MESSAGE = "Yay, i'm here!"

# Send message trough API
response = requests.post(
    f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": MESSAGE,
        "parse_mode": "HTML",  # Can use HTML or markdown
        "disable_web_page_preview": True
    }
)

# Message status verifier
if response.ok:
    print("[✓] Oki doki!")
else:
    print(f"[✗] Something went wrong: {response.status_code} - {response.text}")

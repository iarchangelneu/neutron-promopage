import requests
import os


def send_message(message):
    requests.post(f"https://api.telegram.org/bot{os.environ['TG_BOT_LOGGER']}/sendMessage", 
        data={
            "chat_id": -1001998065929,
            "text": message,
            "message_thread_id": 89479,
        },
    )
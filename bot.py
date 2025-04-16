import requests
from telegram import Bot
import os

# Config
TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['CHAT_ID']
NSE_URL = "https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json"

def get_data():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept-Language": "en-US,en;q=0.9"
        }
        session = requests.Session()
        session.get("https://www1.nseindia.com", headers=headers)
        data = session.get(NSE_URL, headers=headers).json()
        top_gainer = max(data['data'], key=lambda x: float(x['pChange']))
        return f"🏆 Top Gainer: {top_gainer['symbol']} ({top_gainer['pChange']}%)"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

if __name__ == "__main__":
    Bot(token=TOKEN).send_message(
        chat_id=CHAT_ID,
        text=get_data(),
        parse_mode="Markdown"
    )

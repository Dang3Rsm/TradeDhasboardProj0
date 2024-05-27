from dhanhq import marketfeed
import os
from dotenv import load_dotenv
CLIENT_ID =  os.getenv("CLIENT_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

instruments = [(1, "1333"),(0,"13")]

subscription_code = marketfeed.Ticker


async def on_connect(instance):
    print("Connected to websocket")

async def on_message(instance, message):
    print("Received:", message)

print("Subscription code :", subscription_code)

feed = marketfeed.DhanFeed(CLIENT_ID,
    ACCESS_TOKEN,
    instruments,
    subscription_code,
    on_connect=on_connect,
    on_message=on_message)

feed.run_forever()
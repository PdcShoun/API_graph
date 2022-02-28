from datetime import datetime
from time import sleep
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import requests
import json

with open("data_info.json", "r") as f:
    file_data = json.load(f)

API_KEY = file_data["api_key"]
BASE_URL = "https://api.bitkub.com"
URL_MARKET_TICKER = "/api/market/ticker"

TAG_COIN1 = "THB_BTC"
TAG_COIN2 = "THB_ETH"
price_data1 = []
price_data2 = []
time_data = []

def make_api_url(url_api):
    url = BASE_URL + url_api
    return url

def api_market_ticker(tag):
    response = requests.get(make_api_url(URL_MARKET_TICKER))
    data = response.json()
    price = "{:,.2f}".format(data[tag]["last"])
    return price

def animate(i):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    price_data1.append(api_market_ticker(TAG_COIN1))
    time_data.append(current_time)
    if len(price_data1) == 21:
        price_data1.pop(0)
        time_data.pop(0)
    # print(price_data1)
    # print(price_data2)
    plt.cla()
    plt.plot(time_data, price_data1, label='Data 1')

    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

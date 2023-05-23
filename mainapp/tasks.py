from celery import shared_task
from threading import Thread
import queue
import asyncio
from channels.layers import get_channel_layer
import simplejson as json
from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_alpha_vantage_quote(symbol, api_key):
    base_url = "https://www.alphavantage.co/query"
    function = "GLOBAL_QUOTE"
    datatype = "json"

    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
        "datatype": datatype
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data["Global Quote"]


@shared_task(bind = True)
def update_stock(self, stockpicker):
    data = {}
    available_stocks = ["TSLA", "CHPT", "LCID", "GME", "AMD", "NVDA", "AMZN", "GOOG", "AAPL", "MSFT", "COIN", "WMT", "BOIL", "META", "AI", "BABA", "SQ", "NFLX", "WISH", "WBD", "DIS", "SNOW"]
    for i in stockpicker:
        if i in available_stocks:
            pass
        else:
            stockpicker.remove(i)
    
    n_threads = len(stockpicker)
    thread_list = []
    que = queue.Queue()
    for i in range(n_threads):
        thread = Thread(target = lambda q, arg1: q.put({stockpicker[i]: json.loads(json.dumps(get_alpha_vantage_quote(arg1, api_key), ignore_nan = True))}), args = (que, stockpicker[i]))

        thread_list.append(thread)
        thread_list[i].start()

    for thread in thread_list:
        thread.join()

    while not que.empty():
        result = que.get()
        data.update(result)
            
    # send data to group
    channel_layer = get_channel_layer()
    loop = asyncio.new_event_loop()

    asyncio.set_event_loop(loop)

    loop.run_until_complete(channel_layer.group_send("stock_track", {
        'type': 'send_stock_update',
        'message': data,
    }))

    
    return 'Done'
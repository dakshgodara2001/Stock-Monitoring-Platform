from django.shortcuts import render
from asgiref.sync import sync_to_async
from django.http.response import HttpResponse
import time
import queue
from threading import Thread
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")


def home(request):
    return render(request, 'mainapp/basic.html')


def stockPicker(request):
    stock_picker = ["TSLA", "CHPT", "LCID", "GME", "AMD", "NVDA", "AMZN", "GOOG", "AAPL", "MSFT", "COIN", "WMT", "BOIL", "META", "AI", "BABA", "SQ", "NFLX", "WISH", "WBD", "DIS", "SNOW"]
    return render(request, 'mainapp/stockpicker.html', {'stockpicker':stock_picker})

@sync_to_async
def checkAuthenticated(request):
    if not request.user.is_authenticated:
        return False
    else:
        return True

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

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data["Global Quote"]
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


async def stockTracker(request):
    is_loginned = await checkAuthenticated(request)
    if not is_loginned:
        return HttpResponse("Login First")

    stockpicker = request.GET.getlist('stockpicker')
    stockshare = ", ".join(stockpicker)
    
    data = {}
    available_stocks = ["TSLA", "CHPT", "LCID", "GME", "AMD", "NVDA", "AMZN", "GOOG", "AAPL", "MSFT", "COIN", "WMT", "BOIL", "META", "AI", "BABA", "SQ", "NFLX", "WISH", "WBD", "DIS", "SNOW"]
    stockpicker = [stock for stock in stockpicker if stock in available_stocks]

    if len(stockpicker) == 0:
        return HttpResponse("Error")

    n_threads = len(stockpicker)
    thread_list = []
    que = queue.Queue()
    start = time.time()

    for i in range(n_threads):
        thread = Thread(target = lambda q, arg1, i=i: q.put({stockpicker[i]: get_alpha_vantage_quote(arg1, api_key)}), args = (que, stockpicker[i]))
        thread_list.append(thread)
        thread_list[i].start()

    for thread in thread_list:
        thread.join()

    while not que.empty():
        result = que.get()
        data.update(result)

    end = time.time()
    time_taken =  end - start
    print("Time taken: ", time_taken)
            
    return render(request, 'mainapp/stocktracker.html', {'data': data, 'room_name': 'track','selectedstock':stockshare})

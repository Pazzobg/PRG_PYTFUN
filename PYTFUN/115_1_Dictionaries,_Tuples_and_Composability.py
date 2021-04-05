# 1.Use the finnhub.io websockets API to retrieve in realtime data the bitcoin price from the Binance exchange.
# You'll need to following symbol: BINANCE:BTCUSDT. The payload is json, so use the json module in Python
# to transform the message to dict.
# Your class should output in the console all relevant trades in the following format...
import json
from datetime import datetime
from websocket import create_connection


def process_data():
    for dataChunk in j["data"]:
        ts = dataChunk['t'] / 1000.0
        date_time = datetime.fromtimestamp(ts).strftime(fmt)
        print(f"{date_time} price: {dataChunk['p']} volume: {dataChunk['v']}")


tkn = "token"
fmt = "%Y-%m-%d %H:%M:%S"

ws = create_connection(f"wss://ws.finnhub.io?token={tkn}")
ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
res = ws.recv()


j = json.loads(res)

process_data()

ws.close()

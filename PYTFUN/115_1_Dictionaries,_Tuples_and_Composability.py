# 1.Use the finnhub.io websockets API to retrieve in realtime data the bitcoin price from the Binance exchange.
# You'll need to following symbol: BINANCE:BTCUSDT. The payload is json, so use the json module in Python
# to transform the message to dict.
# Your class should output in the console all relevant trades in the following format...
import json
import websocket
from datetime import datetime


def on_message(ws, message):
    j = json.loads(message)
    process_data(j)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send(btc_call)


def process_data(j):
    for dataChunk in j["data"]:
        ts = dataChunk['t'] / 1000.0
        date_time = datetime.fromtimestamp(ts).strftime(fmt)
        print(f"{date_time} price: {dataChunk['p']} volume: {dataChunk['v']}")


if __name__ == "__main__":
    tkn = "YOUR TOKEN HERE"
    btc_call = '{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}'
    fmt = "%Y-%m-%d %H:%M:%S"

    ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={tkn}",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


# Sample response:
# 2021-05-09 14:01:01 price: 57978.69 volume: 0.007672
# 2021-05-09 14:01:01 price: 57978.68 volume: 0.016889
# 2021-05-09 14:01:01 price: 57978.68 volume: 0.00033
# 2021-05-09 14:01:01 price: 57983.38 volume: 0.000373
# 2021-05-09 14:01:01 price: 57983.38 volume: 0.006767
# 2021-05-09 14:01:01 price: 57983.38 volume: 0.000373
# 2021-05-09 14:01:01 price: 57983.38 volume: 0.000249
# 2021-05-09 14:01:02 price: 57983.38 volume: 0.000251
# 2021-05-09 14:01:02 price: 57983.38 volume: 0.0025
# 2021-05-09 14:01:02 price: 57980.83 volume: 0.003523

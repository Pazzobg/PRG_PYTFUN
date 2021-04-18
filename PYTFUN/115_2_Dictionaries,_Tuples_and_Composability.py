# 2. Implement a data structure which calculates time averages. For each one minute period since the first message
# calculate the weighted average price. Keep in mind that there may be late arriving data, and generally the messages
# you receive are not guaranteed to be ordered.
import json
from datetime import datetime, timedelta
from websocket import create_connection


def process_data():
    for dataChunk in payload:
        ts = dataChunk['t'] / 1000.0
        date_time = datetime.fromtimestamp(ts).strftime(fmt)
        print(f"{date_time} price: {dataChunk['p']} volume: {dataChunk['v']}")


# Setting vars
tkn = "token"
tkn.split()
btc_call = '{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}'
fmt = "%Y-%m-%d %H:%M:%S"

prices = []

ws = create_connection(f"wss://ws.finnhub.io?token={tkn}")

ts_start = 0
ts_end = 0
first = 1

# Imitate run_forever()
# If needed, logic can be implemented also with run_forever() method
for i in range(300):
    ws.send(btc_call)
    res = ws.recv()

    # Get payload. If response is of type 'ping' - continue
    j = json.loads(res)
    if j["type"] == "ping":
        continue

    payload = j["data"]

    # Start of measured period
    if first == 1:
        # ts_start = payload[0]['t'] / 1000.0    # Use for measuring 1-min period from
        # ts_end = ts_start + 60                 # message TS, instead of actual datetime
        ts_start = datetime.now()
        ts_end = ts_start + timedelta(seconds=60)
        first = 0

    # If within the measured period - accumulate prices
    # Else - print out the average price and reset TS vars to start new measurement period
    if (datetime.now()) < ts_end:
        for k in range(len(payload)):
            prices.append(payload[k]['p'])
    else:
        # print(f"Start TS: {datetime.fromtimestamp(ts_start).strftime(fmt)}")
        # print(f"End TS: {datetime.fromtimestamp(ts_end).strftime(fmt)}")
        print(f"Start TS: {ts_start.strftime(fmt)}")
        print(f"End TS: {ts_end.strftime(fmt)}")
        print(f"Average price: {round(sum(prices) / len(prices), 2)}")
        ts_start = 0
        ts_end = 0
        first = 1

    # Uncomment to see real time dataflow
    # process_data()

ws.close()


# import websocket
#
# def on_message(ws, message):
#     print(message)
#
# def on_error(ws, error):
#     print(error)
#
# def on_close(ws):
#     print("### closed ###")
#
# def on_open(ws):
#     ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
#
# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=",
#                                 on_message = on_message,
#                                 on_error = on_error,
#                                 on_close = on_close)
#     ws.on_open = on_open
#     ws.run_forever()

# 2. Implement a data structure which calculates time averages. For each one minute period since the first message
# calculate the weighted average price. Keep in mind that there may be late arriving data, and generally the messages
# you receive are not guaranteed to be ordered.
import json
from datetime import datetime
import websocket


def prt(data_chunk):
    ts = data_chunk['t'] / 1000.0
    date_time = datetime.fromtimestamp(ts).strftime(fmt_secs)
    print(f"{date_time} price: {data_chunk['p']} volume: {data_chunk['v']}")


# Setting vars
tkn = "YOUR TOKEN HERE"
btc_call = '{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}'
fmt_secs = "%Y-%m-%d %H:%M:%S"
fmt_min = "%Y-%m-%d %H:%M"

all_prices_dict = {}

ws = websocket.create_connection(f"wss://ws.finnhub.io?token={tkn}")

# Imitate run_forever but using short-lived connection (https://pypi.org/project/websocket-client/)
# If needed, logic can be implemented also with run_forever() method
for i in range(300):
    ws.send(btc_call)
    res = ws.recv()

    # Get payload. If response is of type 'ping' - continue
    j = json.loads(res)
    if j["type"] == "ping":
        continue

    payload = j["data"]

    # Process each data row from response. Fetch the timestamp, price and volume.
    # Timestamp's seconds are truncated and the value serves as dictionary's key.
    # If the key is not yet present in the dict, it is added along with the price and volume
    # If it is already present, the weighted average price is re-calculated for this key (minute)
    # Then the value for this key is updated with the new weighted avg and the accumulated volume, which in turn serve
    # as 'old_price' and 'old_volume' for the next time calculation of weighted avg price for this minute.
    for dataChunk in payload:
        prt(dataChunk)
        time = datetime.fromtimestamp(int(dataChunk['t']) / 1000).strftime(fmt_min)
        new_price = dataChunk['p']
        new_volume = dataChunk['v']

        if time in all_prices_dict.keys():
            old_weighted_avg, old_volume = all_prices_dict[time]

            # Calculation of the new weighted average price
            accumulated_volume = old_volume + new_volume
            new_weighted_avg = ((old_weighted_avg * old_volume) + (new_price * new_volume)) / accumulated_volume

            all_prices_dict.update({time: (new_weighted_avg, accumulated_volume)})
        else:
            all_prices_dict.update({time: (new_price, new_volume)})

ws.close()

for key in all_prices_dict:
    w_price = all_prices_dict[key][0]
    print(f"For minute {key} - Weighted average price: {w_price:10.5f}")

import datetime
import time

import pandas as pd

import requests

def collect_data():
    

    data = 'max_rows=160&scan_clause=(%20%7B33492%7D%20(%20%5B0%5D%201%20minute%20rsi(%203%20)%20%3E%20%5B0%5D%201%20minute%20rsi(%206%20)%20and%20%5B0%5D%201%20minute%20rsi(%206%20)%20%3E%20%5B0%5D%201%20minute%20rsi(%209%20)%20and%20%5B0%5D%201%20minute%20rsi(%209%20)%20%3E%20%5B0%5D%201%20minute%20rsi(%2013%20)%20and%20%5B0%5D%201%20minute%20rsi(%2013%20)%20%3E%20%5B0%5D%201%20minute%20rsi(%2020%20)%20and%20%5B0%5D%201%20minute%20rsi(%2020%20)%20%3E%20%5B0%5D%201%20minute%20rsi(%2050%20)%20)%20)%20'

    response = requests.post('https://chartink.com/backtest/process', cookies=cookies, headers=headers, data=data)

    if response.status_code == 200:
        # Parse the response JSON and print the data
        data = response.json()

        date = data["metaData"][0]["tradeTimes"]
        stock = data["aggregatedStockList"]

        final_data = []
        for i in range(0, len(date)):
            stk = []
            if stock[i] != []:
                for j in range(len(stock[i])):
                    if j % 3 == 0:
                        stk.append(stock[i][j])

                final_data.append({
                    "Date": datetime.datetime.fromtimestamp(date[i]/1000),
                    "Stock": len(stk)
                })
        df = pd.DataFrame(final_data)

        print(df)
        max_stock_value = df["Stock"].max()
        if max_stock_value > 25:
            print(f"ALERT! Stock count has exceeded 25. Max stock value: {max_stock_value}")

    else:
        print(f"Request failed with status code {response.status_code}")

while True:
    collect_data()
    time.sleep(60)

import datetime
import time

import pandas as pd

import requests

def collect_data():
    cookies = {
        '_ga': 'GA1.2.301791879.1726215388',
        'FCNEC': '%5B%5B%22AKsRol9hwozDl6_xdockjNSP0_IV0oLdOaCJcCfWdWmit4blC2kIC_l0C7nXX5ygHdBCSquG5pyP-Q7d11prm3TOCar7axHeEM5oTfZ4_fZsqM0UdVKm3GHuXOP4TMJz5DFJ0r91x9pXmujK9CDsdOTpRVJBfgRgmQ%3D%3D%22%5D%5D',
        '__gads': 'ID=01d84225b269872c:T=1726215390:RT=1729225664:S=ALNI_MaBgaL3jfC-3mEaBCEnkZb5w00pKQ',
        '__eoi': 'ID=ec5994392e42d723:T=1726215390:RT=1729225664:S=AA-AfjbN2dDaqaxuId9sOUlekCQ2',
        'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6ImJsbkpxTVNJZlpSaXJCbUlHQTFDTEE9PSIsInZhbHVlIjoicEhyM01nRGducitnMFl6dU1SbGhFdTQrNXRSc0NwMHNSMHJJQjVPTkRCaWhxOW93TzBxakdSVG51a3J4dlJPUXY1MHhzUGRDZFhHUmxyVktNUHVKMCtxenMyV3NDcDhaQ3VUSEFOVmVWM2VaQjY3NG5DY2xBVWlRNldMTjVESkM3ZHJGVGVHYWhFc3hiSXJxUURTbjRSY2lRaHVmci9MUmh3VnloaDRHMmxmRFhDZDYrNUhWckREZFp4MVpTNHVnYlNRSUV4a1p2MzVOeHd5M3VkdjFlUXRHdVN5Z2thb0UyQ1c1MUgxbW1UTT0iLCJtYWMiOiI3OWU3MGI1NWVhNzM1YjBhNjk5Mjk1ZWQzN2I0MzU3ZGRmZTY5OWFlMTZmMWUwYzUzNjQyMGE2YjY5ZTM4ZTE3IiwidGFnIjoiIn0%3D',
        '__utma': '102564947.301791879.1726215388.1729323021.1729325824.3',
        '__utmz': '102564947.1729325824.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        '_gid': 'GA1.2.1370312915.1729485960',
        '_ga_7P3KPC3ZPP': 'GS1.2.1729485960.16.0.1729485960.0.0.0',
        'XSRF-TOKEN': 'eyJpdiI6Im4yMTFtbFpQR1FYMFdEQ2hlMTY3cGc9PSIsInZhbHVlIjoic3l0UTh5K1BqbldyVHhidkRSakpDSDZlVWVBSDZqVlpmU2NkcDF6SnlqRkRuY04yQUJWeENqRkpCWGVNcW9kVy9HUWJJZUNFVEs3Ri9MSm0zQjBvc2c5U01TTWw0SXNrWWl4eU5RY1hLTCtKelZuaGlOd1VCRmF1cXlkbUpSR0YiLCJtYWMiOiJiZmJjMjlkODk3MDQwNjE3ODNiYjYwZWQxMjUwZDZkMjFmZWZiZmU4MGMxMzAwM2JmY2IwOTJlMDY3OWRmMDc3IiwidGFnIjoiIn0%3D',
        'ci_session': 'eyJpdiI6IjNIZkMveFFtQVZlUXhsMnptbnRhWVE9PSIsInZhbHVlIjoicTBGVkRXSkxNMFJkL05LeGJFWkV4Ti9OZVFGcmZEVml6eFlJcUlEUVNMWSs3L1F4QkEvc0JmUktVNGM0dHYyZ2doTVdUWUEzN1B6d0Y0dU5uR21LN01sV2NJeURET1BrR1I2aFZKQWxKV3JUTHJGSzRFR2pBTWpRaU5LcmwxNHQiLCJtYWMiOiIzMDU1MWZmZWVkNWMwNjA4N2FmZjk1YTRiMDk1NmY1ZWJiYTgyNDUxNGM3YzVmYjc0YjA0ZDVkZTQ4NjQ2ZTQxIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_ga=GA1.2.301791879.1726215388; FCNEC=%5B%5B%22AKsRol9hwozDl6_xdockjNSP0_IV0oLdOaCJcCfWdWmit4blC2kIC_l0C7nXX5ygHdBCSquG5pyP-Q7d11prm3TOCar7axHeEM5oTfZ4_fZsqM0UdVKm3GHuXOP4TMJz5DFJ0r91x9pXmujK9CDsdOTpRVJBfgRgmQ%3D%3D%22%5D%5D; __gads=ID=01d84225b269872c:T=1726215390:RT=1729225664:S=ALNI_MaBgaL3jfC-3mEaBCEnkZb5w00pKQ; __eoi=ID=ec5994392e42d723:T=1726215390:RT=1729225664:S=AA-AfjbN2dDaqaxuId9sOUlekCQ2; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImJsbkpxTVNJZlpSaXJCbUlHQTFDTEE9PSIsInZhbHVlIjoicEhyM01nRGducitnMFl6dU1SbGhFdTQrNXRSc0NwMHNSMHJJQjVPTkRCaWhxOW93TzBxakdSVG51a3J4dlJPUXY1MHhzUGRDZFhHUmxyVktNUHVKMCtxenMyV3NDcDhaQ3VUSEFOVmVWM2VaQjY3NG5DY2xBVWlRNldMTjVESkM3ZHJGVGVHYWhFc3hiSXJxUURTbjRSY2lRaHVmci9MUmh3VnloaDRHMmxmRFhDZDYrNUhWckREZFp4MVpTNHVnYlNRSUV4a1p2MzVOeHd5M3VkdjFlUXRHdVN5Z2thb0UyQ1c1MUgxbW1UTT0iLCJtYWMiOiI3OWU3MGI1NWVhNzM1YjBhNjk5Mjk1ZWQzN2I0MzU3ZGRmZTY5OWFlMTZmMWUwYzUzNjQyMGE2YjY5ZTM4ZTE3IiwidGFnIjoiIn0%3D; __utma=102564947.301791879.1726215388.1729323021.1729325824.3; __utmz=102564947.1729325824.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _gid=GA1.2.1370312915.1729485960; _ga_7P3KPC3ZPP=GS1.2.1729485960.16.0.1729485960.0.0.0; XSRF-TOKEN=eyJpdiI6Im4yMTFtbFpQR1FYMFdEQ2hlMTY3cGc9PSIsInZhbHVlIjoic3l0UTh5K1BqbldyVHhidkRSakpDSDZlVWVBSDZqVlpmU2NkcDF6SnlqRkRuY04yQUJWeENqRkpCWGVNcW9kVy9HUWJJZUNFVEs3Ri9MSm0zQjBvc2c5U01TTWw0SXNrWWl4eU5RY1hLTCtKelZuaGlOd1VCRmF1cXlkbUpSR0YiLCJtYWMiOiJiZmJjMjlkODk3MDQwNjE3ODNiYjYwZWQxMjUwZDZkMjFmZWZiZmU4MGMxMzAwM2JmY2IwOTJlMDY3OWRmMDc3IiwidGFnIjoiIn0%3D; ci_session=eyJpdiI6IjNIZkMveFFtQVZlUXhsMnptbnRhWVE9PSIsInZhbHVlIjoicTBGVkRXSkxNMFJkL05LeGJFWkV4Ti9OZVFGcmZEVml6eFlJcUlEUVNMWSs3L1F4QkEvc0JmUktVNGM0dHYyZ2doTVdUWUEzN1B6d0Y0dU5uR21LN01sV2NJeURET1BrR1I2aFZKQWxKV3JUTHJGSzRFR2pBTWpRaU5LcmwxNHQiLCJtYWMiOiIzMDU1MWZmZWVkNWMwNjA4N2FmZjk1YTRiMDk1NmY1ZWJiYTgyNDUxNGM3YzVmYjc0YjA0ZDVkZTQ4NjQ2ZTQxIiwidGFnIjoiIn0%3D',
        'origin': 'https://chartink.com',
        'priority': 'u=1, i',
        'referer': 'https://chartink.com/screener/1-min-bull-by-dnm-og',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
        'x-xsrf-token': 'eyJpdiI6Im4yMTFtbFpQR1FYMFdEQ2hlMTY3cGc9PSIsInZhbHVlIjoic3l0UTh5K1BqbldyVHhidkRSakpDSDZlVWVBSDZqVlpmU2NkcDF6SnlqRkRuY04yQUJWeENqRkpCWGVNcW9kVy9HUWJJZUNFVEs3Ri9MSm0zQjBvc2c5U01TTWw0SXNrWWl4eU5RY1hLTCtKelZuaGlOd1VCRmF1cXlkbUpSR0YiLCJtYWMiOiJiZmJjMjlkODk3MDQwNjE3ODNiYjYwZWQxMjUwZDZkMjFmZWZiZmU4MGMxMzAwM2JmY2IwOTJlMDY3OWRmMDc3IiwidGFnIjoiIn0=',
    }

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
import datetime
import time
import schedule
import pandas as pd
import os

import requests

STOCK_DATA_FILE = "live_bull.csv"


def collect_data():
    cookies = {
        '_ga': 'GA1.2.301791879.1726215388',
        'FCNEC': '%5B%5B%22AKsRol9hwozDl6_xdockjNSP0_IV0oLdOaCJcCfWdWmit4blC2kIC_l0C7nXX5ygHdBCSquG5pyP-Q7d11prm3TOCar7axHeEM5oTfZ4_fZsqM0UdVKm3GHuXOP4TMJz5DFJ0r91x9pXmujK9CDsdOTpRVJBfgRgmQ%3D%3D%22%5D%5D',
        '__utma': '102564947.301791879.1726215388.1729323021.1729325824.3',
        '__utmz': '102564947.1729325824.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        '_gid': 'GA1.2.1949650.1729836752',
        '__gads': 'ID=01d84225b269872c:T=1726215390:RT=1729836752:S=ALNI_MaBgaL3jfC-3mEaBCEnkZb5w00pKQ',
        '__eoi': 'ID=ec5994392e42d723:T=1726215390:RT=1729836752:S=AA-AfjbN2dDaqaxuId9sOUlekCQ2',
        'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6IlJJUkp5L3lzVjFCaHJtY1hGT051blE9PSIsInZhbHVlIjoibUJQbzM4QkpKTXUvZ0hwVThJRy8yUGJZcklMYXNPVllTc2pYWEFmVjlkZnBlK053aHVISURXejFuVVFMMDA1b1Ixa0Fob0VkWXdVdXRJVGhLRWtBTmtIbnZTNnlOWm14TGZrQzFuaDNWWEtZNkQvdVd6WGpqdnU5djlIRllsZFF4U1NzNXNNMHhZMTBwM1dXN0cwSWRhZG9yWDljdThsME04NTdjWjAxb3FpZVQwb2Nzektnb0pVdGYwT0NNSDNPVzY1VTlQanpKZzZNSDhOZ0lSVHU1WjNrZ2YvT1NXTHJpeGNkM2RUVmhMYz0iLCJtYWMiOiIzYTcwNTY5OGE5ZmY0ZTI0M2M3NGNmOTVhMGExYzVkZDY5ZDBmZDE3ZjA5ODBhOTdhOTNmNjMzZjUwMWM3ZWQ3IiwidGFnIjoiIn0%3D',
        '_gat': '1',
        '_ga_7P3KPC3ZPP': 'GS1.2.1729836752.22.1.1729836813.0.0.0',
        'XSRF-TOKEN': 'eyJpdiI6IkZKWFFMK0JTd0dWSFJCV2JlSmRDbVE9PSIsInZhbHVlIjoibVVpQ0FTajJwbFc1WG5uUktBSzNYRGU0MldZTU1FNmx4RmhzVHVBb093d2xnY2IzMHJGclhqYmJtZVlzRXFsaTFLczNZeXNLUWNVaXEwQmNvNGdTc2VGMG1hd082amZNeVd2ell1L3kwVGg4T3V4SHFEYWM5b1RRZzd0Q1U1U3UiLCJtYWMiOiI3NzY2OWVjZTFlNWMwYmE2NTRmZDA3OGU5ODQ0Y2E3NzA5NzVmZTdhODJkOGY5ZWNkOGNiMjRmZjQzZmU1YWI4IiwidGFnIjoiIn0%3D',
        'ci_session': 'eyJpdiI6IkVxQlRmRno1Rk9Xcko4QTk5U2JXT3c9PSIsInZhbHVlIjoieVRNVzVyc2EyOHNTd2JWVGNWT3luU3owaTc3dXNoV0JleVFucjZ3S2srV2w2V3UzMVQ5RE5QOWhKeFBzenQ0WFBVc0drZmpWMERQWThOazdvRWJJR1RVaXF6KzhoSkU5anRIZFBoMUJJV1BQNWZnRnlLQjNqa095WWdvZllHUUgiLCJtYWMiOiJlOGJkNWM4MjNjMWU2MTg5ZjZjNGNlMDg5NDE4ZGRhOGJhNDEyNTczYmZmNTg0MGIxOWIzNGNiM2ZhYmJlNTVlIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_ga=GA1.2.301791879.1726215388; FCNEC=%5B%5B%22AKsRol9hwozDl6_xdockjNSP0_IV0oLdOaCJcCfWdWmit4blC2kIC_l0C7nXX5ygHdBCSquG5pyP-Q7d11prm3TOCar7axHeEM5oTfZ4_fZsqM0UdVKm3GHuXOP4TMJz5DFJ0r91x9pXmujK9CDsdOTpRVJBfgRgmQ%3D%3D%22%5D%5D; __utma=102564947.301791879.1726215388.1729323021.1729325824.3; __utmz=102564947.1729325824.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _gid=GA1.2.1949650.1729836752; __gads=ID=01d84225b269872c:T=1726215390:RT=1729836752:S=ALNI_MaBgaL3jfC-3mEaBCEnkZb5w00pKQ; __eoi=ID=ec5994392e42d723:T=1726215390:RT=1729836752:S=AA-AfjbN2dDaqaxuId9sOUlekCQ2; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlJJUkp5L3lzVjFCaHJtY1hGT051blE9PSIsInZhbHVlIjoibUJQbzM4QkpKTXUvZ0hwVThJRy8yUGJZcklMYXNPVllTc2pYWEFmVjlkZnBlK053aHVISURXejFuVVFMMDA1b1Ixa0Fob0VkWXdVdXRJVGhLRWtBTmtIbnZTNnlOWm14TGZrQzFuaDNWWEtZNkQvdVd6WGpqdnU5djlIRllsZFF4U1NzNXNNMHhZMTBwM1dXN0cwSWRhZG9yWDljdThsME04NTdjWjAxb3FpZVQwb2Nzektnb0pVdGYwT0NNSDNPVzY1VTlQanpKZzZNSDhOZ0lSVHU1WjNrZ2YvT1NXTHJpeGNkM2RUVmhMYz0iLCJtYWMiOiIzYTcwNTY5OGE5ZmY0ZTI0M2M3NGNmOTVhMGExYzVkZDY5ZDBmZDE3ZjA5ODBhOTdhOTNmNjMzZjUwMWM3ZWQ3IiwidGFnIjoiIn0%3D; _gat=1; _ga_7P3KPC3ZPP=GS1.2.1729836752.22.1.1729836813.0.0.0; XSRF-TOKEN=eyJpdiI6IkZKWFFMK0JTd0dWSFJCV2JlSmRDbVE9PSIsInZhbHVlIjoibVVpQ0FTajJwbFc1WG5uUktBSzNYRGU0MldZTU1FNmx4RmhzVHVBb093d2xnY2IzMHJGclhqYmJtZVlzRXFsaTFLczNZeXNLUWNVaXEwQmNvNGdTc2VGMG1hd082amZNeVd2ell1L3kwVGg4T3V4SHFEYWM5b1RRZzd0Q1U1U3UiLCJtYWMiOiI3NzY2OWVjZTFlNWMwYmE2NTRmZDA3OGU5ODQ0Y2E3NzA5NzVmZTdhODJkOGY5ZWNkOGNiMjRmZjQzZmU1YWI4IiwidGFnIjoiIn0%3D; ci_session=eyJpdiI6IkVxQlRmRno1Rk9Xcko4QTk5U2JXT3c9PSIsInZhbHVlIjoieVRNVzVyc2EyOHNTd2JWVGNWT3luU3owaTc3dXNoV0JleVFucjZ3S2srV2w2V3UzMVQ5RE5QOWhKeFBzenQ0WFBVc0drZmpWMERQWThOazdvRWJJR1RVaXF6KzhoSkU5anRIZFBoMUJJV1BQNWZnRnlLQjNqa095WWdvZllHUUgiLCJtYWMiOiJlOGJkNWM4MjNjMWU2MTg5ZjZjNGNlMDg5NDE4ZGRhOGJhNDEyNTczYmZmNTg0MGIxOWIzNGNiM2ZhYmJlNTVlIiwidGFnIjoiIn0%3D',
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
        'x-xsrf-token': 'eyJpdiI6IkZKWFFMK0JTd0dWSFJCV2JlSmRDbVE9PSIsInZhbHVlIjoibVVpQ0FTajJwbFc1WG5uUktBSzNYRGU0MldZTU1FNmx4RmhzVHVBb093d2xnY2IzMHJGclhqYmJtZVlzRXFsaTFLczNZeXNLUWNVaXEwQmNvNGdTc2VGMG1hd082amZNeVd2ell1L3kwVGg4T3V4SHFEYWM5b1RRZzd0Q1U1U3UiLCJtYWMiOiI3NzY2OWVjZTFlNWMwYmE2NTRmZDA3OGU5ODQ0Y2E3NzA5NzVmZTdhODJkOGY5ZWNkOGNiMjRmZjQzZmU1YWI4IiwidGFnIjoiIn0=',
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

                stock_count = len(stock)
                if stock_count > 25:

                    final_data.append({
                        "Date": datetime.datetime.fromtimestamp(date[i] / 1000),
                        "Stock": len(stk)
                    })
        df = pd.DataFrame(final_data)

        print(df)

        append_new_data(df)

        # df2 = df["Stock"] > 25
        # df.where(df2, inplace=True)
        # df.dropna(inplace=True)
        # df.to_csv(r'C:\Users\FZ\Downloads\bullsheet.csv')

        max_stock_value = df["Stock"].max()
        if max_stock_value > 25:
            print(f"ALERT! Stock count has exceeded 25. Max stock value: {max_stock_value}")
            print(max_stock_value)



    else:
        print(f"Request failed with status code {response.status_code}")


def append_new_data(new_df):
    # Check if file exists
    if os.path.exists(STOCK_DATA_FILE):
        # Load the existing data
        existing_df = pd.read_csv(STOCK_DATA_FILE)

        # Merge the new data, dropping duplicates
        combined_df = pd.concat([existing_df, new_df]).drop_duplicates(subset=["Date", "Stock"], keep='last')
    else:
        # If the file doesn't exist, use the new data
        combined_df = new_df

    # Save the combined data back to the CSV file
    combined_df.to_csv(STOCK_DATA_FILE, index=False)
    print(f"Data appended to {STOCK_DATA_FILE}")


while True:
    collect_data()
    time.sleep(60)

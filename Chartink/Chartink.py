import requests
from bs4 import BeautifulSoup as bs

import pandas as pd

url = "https://chartink.com/screener/process"

condition = {"scan_clause": "( {33492} ( [0] 1 minute rsi( 3 ) > [0] 1 minute rsi( 6 ) and [0] 1 minute rsi( 6 ) > ["
                            "0] 1 minute rsi( 9 ) and [0] 1 minute rsi( 9 ) > [0] 1 minute rsi( 13 ) and [0] 1 minute "
                            "rsi( 13 ) > [0] 1 minute rsi( 20 ) and [0] 1 minute rsi( 20 ) > [0] 1 minute rsi( 50 ) ) "
                            ")"}

with requests.session() as s:
    r_data = s.get(url)
    soup = bs(r_data.content, "lxml")
    meta = soup.find("meta", {"name": "csrf-token"})["content"]
    header = {"x-csrf-token": meta}

    data = s.post(url, headers=header, data=condition).json()

    print(data.keys)
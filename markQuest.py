"""
https://www.alphavantage.co/documentation/
"""

import requests
from dotenv import load_dotenv
import os
import sys
from pandas import DataFrame
from tabulate import tabulate

# from tabulate import tabulate

# load_dotenv(f"/mnt/c/Users/JLazaro/personal/market_request/env/shared/requests.env.shared")
load_dotenv(f"env/secret/requests.env.secret", override=True)


def get_price(url, stock_name=''):
    """ Get data """
    print("url", url)

    ### Request:
    response = requests.get(url)
    print('response: ', response)

    dicto = response.json()
    breakpoint()
    df = DataFrame(dicto['Time Series (5min)']).T

    return df


if __name__=='__main__':
    apikey = os.environ['AlphaVantage']
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=NVDA&interval=5min&apikey={apikey}"
    url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey={apikey}"
    df = get_price(url)
    print(tabulate(df, headers=df.columns))
    # breakpoint()

    # import requests
    # breakpoint()
    # apikey = os.environ['AlphaVantage']
    # # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    # url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={apikey}"
    # r = requests.get(url)
    # data = r.json()
    # print(data)

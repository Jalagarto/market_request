# https://yahooquery.dpguthrie.com/
from yahooquery import Ticker

aapl = Ticker('NVDA')

aapl.summary_detail
breakpoint()
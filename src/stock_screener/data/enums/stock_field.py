"""
Defines the StockField enumeration used throughout the stock analyzer.

SockField gives a set of field identifiers that represent attributes of a stock.
These attributes are use for:

- Building filter rules for the screener
- Referencing columns in DataFrames
- Requesting metrics from data providers (i.e. yfinance)
- Ensuring type safety and consistency

Each enum member inherits from 'str' to allow seamless usage with pandas,
JSON serializations, and API integrations.
"""
from enum import Enum

class StockField(str, Enum):
    ticker = 'ticker'
    price = 'price'
    avg_daily_volume = 'avg_daily_volume'
    dividend_yield = "dividend_yield"
    market_cap = "market_cap"
    pe_ratio = "pe_ratio"
    pb_ratio = "pb_ratio"
    sector = "sector"
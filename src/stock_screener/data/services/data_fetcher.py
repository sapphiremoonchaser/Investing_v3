import yfinance as yf
import pandas as pd
from typing import List

from stock_screener.data.enums.stock_field import StockField


def fetch_stock_data(
        ticker: str,
        fields: List[StockField]
) -> pd.DataFrame:
    """
    Fetches fundamental info for a single ticker.

    :param ticker (str): Stock symbol
    :param fields (List[StockField]): Fields to fetch:
    :return (pd.DataFrame): Single-row df with requested fields
    """
    t = yf.Ticker(ticker)
    info = t.info

    data = {}
    for field in fields:
        # getting ticker from yf
        if field == StockField.ticker:
            data[field.value] = ticker

        # Get the current price
        elif field == StockField.price:
            data[field.value] = info.get("currentPrice")

        # Fetch average volume
        elif field == StockField.avg_daily_volume:
            data[field.value] = info.get("averageVolume")

        # Fetch dividend yield
        elif field == StockField.dividend_yield:
            dividend_yield = info.get("dividendYield")
            data[field.value] = dividend_yield * 100 if dividend_yield is not None else 0

        # Fetch market cap
        elif field == StockField.market_cap:
            data[field.value] = info.get("marketCap")

        # Fetch trailing PE
        elif field == StockField.pe_ratio:
            data[field.value] = info.get("trailingPE")

        # Fetch price to book ratio
        elif field == StockField.pb_ratio:
            data[field.value] = info.get("priceToBook")

        # Fetch sector
        elif field == StockField.sector:
            data[field.value] = info.get("sector")

        else:
            data[field.value] = None

    return pd.DataFrame(data)

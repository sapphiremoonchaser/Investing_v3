from enum import Enum

class StockField(str, Enum):
    ticker = 'ticker'
    price = 'price'
    avg_daily_volume = 'avg_daily_volume'
    dividend_yield = "dividend_yield"
    market_cap = "market_cap"
    pe_ratio = "pe_ratio"
    pb_ratio = "pb_ratio"
    price ="price"
    sector = "sector"
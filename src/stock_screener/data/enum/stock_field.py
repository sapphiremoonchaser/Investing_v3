from enum import Enum

class StockField(str, Enum):
    dividen_yield = "dividen_yield"
    market_cap = "market_cap"
    avg_daily_volume = "avg_daily_volume"
    pe_ratio = "pe_ratio"
    pb_ratio = "pb_ratio"
    price ="price"
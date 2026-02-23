"""
Defines filtering rules used by the stock screener.

This module contains the FilterRule model, which represents a single screening
condition applied to stock data. A 'filter rule' consists of:

    - A SockField (the metric being evaluated)
    - A comparison operator (>, <, <=, >=, ==)
    - A comparison value

FilterRule serves as a structured, validated representation of user-defined screening
criteria. It's used by the screener to dynamically construct and apply filters.

The model includes:

    - Human-readable string formatting (__str__)
    - UI-friendly label formatting (label)
    - Pydantic validation
    - Enum-backed field validation
"""
from typing import Literal
from pydantic import BaseModel

from stock_screener.data.enums.stock_field import StockField

Operator = Literal['>', '<', '>=', '<=', '==']

class FilterRule(BaseModel):
    field: StockField
    operator: Operator
    value: float | int | str

    # Good for human readability
    def __str__(self) -> str:
        field = self.field.value

        # if dividend_yield format with 2 decimal places
        if self.field == 'dividend_yield':
            return f"Dividend Yield {self.operator} {self.value:.2%}"

        # Metrics in Billions of $
        if self.field == 'market_cap':
            return f"Market Cap {self.operator} {self.value/1e9:.1f}B"

        # ToDo: add formatting for rest of metrics

        return f'{field} {self.operator} {self.value}'


    def label(self) -> str:
        # Percentage formatting with 0 decimal places
        if self.field == 'dividend_yield':
            return f"Dividend Yield {self.operator} {self.value:.2%}"

        # Market Cap label formatting (B, M, K)
        if self.field == StockField.market_cap:
            # Formatting when more than a billion
            if self.value >= 1_000_000_000:
                billions = self.value / 1_000_000_000
                return f'Market Cap {self.operator} ${billions:,.1f}B'

            # Formatting for more than a million, less than a billion
            elif self.value >= 1_000_000:
                millions = self.value / 1_000_000
                return f'Market Cap {self.operator} ${millions:,.1f}M'

            # Formatting for more than 1,000, less than a million
            elif self.value >= 1_000:
                thousands = self.value / 1_000
                return f'Market Cap {self.operator} ${thousands:,.0f}K'

            # Formatting for less than 1,000
            else:
                return f'Market Cap {self.operator} ${self.value:,.0f}'

        # P/E ratio label formatting (2 decimals)
        if self.field == StockField.pe_ratio:
            return f'PE Ratio {self.operator} {self.value:,.1f}'

        # P/B ratio label formatting (2 decimals)
        if self.field == StockField.pb_ratio:
            return f'PB Ratio {self.operator} {self.value:,.1f}'

        # Anything else, just remove the '_' and repalce with blank space
        return f"{self.field.replace('_', ' ').title()} {self.operator} {self.value}"
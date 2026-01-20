"""Pydantic Class for custom filter rules.
    Models define what a filter is
    Services define how it runs
"""
from typing import Literal

from pandas.compat.numpy.function import validate_groupby_func
from pydantic import (
    BaseModel
)

from stock_screener.data.enums.stock_field import StockField

Operator = Literal['>', '<', '>=', '<=', '==']

class FilterRule(BaseModel):
    field: StockField
    operator: Operator
    value: float | int

    # Good for human readability
    def __str__(self) -> str:
        # if dividend_yield format with 2 decimal places
        if "yield" in self.field:
            return f'{self.field} {self.operator} {self.value:.2%}'
        return f'{self.field} {self.operator} {self.value}'

    # # Good for debugging
    # def __repr__(self) -> str:
    #     fields = ", ".join(
    #         f"{k}={v!r}" for k, v in self.model_data().items()
    #     )
    #     return f"{self.__class__.__name__}({fields})"

    def label(self) -> str:
        # Price label formatting
        if self.field == StockField.price:
            return f'Price {self.operator} ${self.value:,.2f}'

        # Avg Daily Volume label formatting (M and K)
        if self.field == StockField.avg_daily_volume:
            if self.value >= 1_000_000:
                millions = self.value / 1_000_000
                return f'Avg Daily Volume {self.operator} {millions:,.1f}M'

            elif self.value >= 1_000:
                thousands = self.value / 1_000
                return f'Avg Daily Volume {self.operator} {thousands:,.0f}K'

            else:
                return f'Avg Daily Volume {self.operator} {self.value:,.0f}'

        # Dividend Yield label formatting (% with no decimal)
        if self.field == StockField.dividend_yield:
            return f"Dividend Yield {self.operator} {self.value:.0%}"

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
            return f'PE Ratio {self.operator} {self.value:,.2}'





        # Anything else, just remove the '_' and repalce with blank space
        return f"{self.field.replace('_', ' ').title()} {self.operator} {self.value}"
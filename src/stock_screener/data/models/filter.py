"""Pydantic Class for custom filter rules.
    Models define what a filter is
    Services define how it runs
"""
from typing import Literal

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
        # Percentage formatting with 0 decimal places
        if self.field == 'dividend_yield':
            return f"Dividend Yield {self.operator} {self.value:.0%}"

        # Metrics in Billions of $
        if self.field == 'market_cap':
            return f"Market Cap {self.operator} {self.value/1e9:.1f}B"

        # Anything else, just remove the '_' and repalce with blank space
        return f"{self.field.replace('_', ' ').title()} {self.operator} {self.value}"
"""Pydantic Class for custom filter rules.
"""
import operator
from typing import Literal

import pandas as pd
from pydantic import (
    BaseModel,
    Field
)

Operator = Literal['>', '<', '>=', '<=', '==']

# This is for the pandas mask
OPS = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
}

class FilterRule(BaseModel):
    field: str = Field(
        ...,
        description='Stock Market Metric Name',
    )
    operator: Operator
    value: float | int

    # Good for human readability
    def __str__(self) -> str:
        # if dividend_yield format with 2 decimal places
        if "yield" in self.field:
            return f'{self.field} {self.operator} {self.value:.2%}'
        return f'{self.field} {self.operator} {self.value}'

    # Good for debugging
    def __repr__(self) -> str:
        return (
            f"FilterRule(field={self.field!r}, "
            f"operator={self.operator!r}, "
            f"value={self.value!r})"
        )

    def to_pandas_mask(
        self,
        df: pd.DataFrame,
    ):
        """This allows each rule to become a boolean mask.
            Operator symbols like <, >=, etc. are changed to
            something more friendly for Pandas (such as
            operator.lt, operator.ge, etc.

            See 'OPS' object above for the mapping.
        :param df:
        :return:
        """
        return OPS[self.operator](
            df[self.field],
            self.value
        )
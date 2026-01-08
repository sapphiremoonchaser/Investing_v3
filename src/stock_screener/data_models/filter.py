"""Pydantic Class for custom filter rules.
"""
from typing import Literal
from pydantic import (
    BaseModel,
    Field
)

Operator = Literal['>', '<', '>=', '<=', '==']

class FilterRule(BaseModel):
    field: str = Field(
        ...,
        description='Stock Market Metric Name',
    )
    operator: Operator
    value: float | int

    def __str__(self) -> str:
        return f'{self.field} {self.operator} {self.value}'



from pydantic import BaseModel
from typing import List
from .filter import FilterRule


class ScreenerPreset(BaseModel):
    name: str
    description: str
    filters: List[FilterRule]


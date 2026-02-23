"""Rule to create mask to use with pandas
"""
import operator
import pandas as pd
from stock_screener.data.models.filter import FilterRule

OPS = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
}

def rule_to_mask(
    rule: FilterRule,
    df: pd.DataFrame
) -> pd.Series:
    """This allows each rule to become a boolean mask.
        Operator symbols like <, >=, etc. are changed to
        something more friendly for Pandas (such as
        operator.lt, operator.ge, etc.

        See 'OPS' object above for the mapping.
    :param df:
    :return:
    """
    return OPS[rule.operator](
        df[rule.field],
        rule.value
    )
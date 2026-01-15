"""Services define how a filter runs
    Models define what a filter is

    Engine that applies rules to da DataFrame
"""
from stock_screener.data.models.filter import FilterRule
import pandas as pd


def apply_filters(
        df: pd.DataFrame,
        rules: list[FilterRule]
) -> pd.DataFrame:
    """Apply a list of FilterRule objects to a DataFrame.

    Rules are applied sequentially (AND logic).
    :param df:
    :param rules:
    :return:
    """
    filtered_df = df.copy()

    for rule in rules:
        mask = rule.to_pandas_mask(filtered_df)
        filtered_df = filtered_df[mask]

    return filtered_df



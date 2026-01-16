"""Integration Test for data/services/screener.py

Tests to make sure the following are working together correctly:
    - FilterRule
    - rule_to_mask()
    - apply_filters()
    - pandas indexing behavior

Behaviors that matter:
    - applies rules sequentially (may be more important if I add OR logic later)
    - uses AND logic
    - returns a DataFrame with the same schema
"""

# Imports
import pandas as pd
from pycparser.ply.yacc import resultlimit

from stock_screener.data.models.filter import FilterRule
from stock_screener.data.services.screener import apply_filters
from stock_screener.data.services.filtering.pandas import rule_to_mask

def test_apply_filters_multiple_rules_and_logic():
    # Create an arbitrary dataframe to test
    df = pd.DataFrame({
        "pe_ratio": [5, 10, 20],
        "market_cap": [2e9, 5e8, 3e9],
        "sector": ["Tech", "Tech", "Finance"],
    })

    # Set of rules to filter on
    rules = [
        FilterRule(
            field='pe_ratio',
            operator='<',
            value=15
        ),
        FilterRule(
            field='market_cap',
            operator='>',
            value=1e9
        ),
        FilterRule(
            field='sector',
            operator='==',
            value='Tech'
        )
    ]

    # Result after filtered
    result = apply_filters(df=df, rules=rules)

    assert len(result) == 1
    assert result.iloc[0]['pe_ratio'] == 5
    assert result.iloc[0]['sector'] == 'Tech'


# Testing that no rules returns the original dataframe
def test_apply_filters_no_rules_returns_original_df():
    df = pd.DataFrame({
        "a": [1, 2, 3]
    })

    result = apply_filters(df=df, rules=[])

    pd.testing.assert_frame_equal(result, df)



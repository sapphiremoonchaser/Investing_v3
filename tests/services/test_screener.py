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

from stock_screener.data.models.filter import FilterRule
from stock_screener.data.services.screener import apply_filters

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


def test_apply_filters_no_rules_returns_original_df():
    """Testing for cases where no rules are applied.
        Expected result is the original dataframe
    :return:
    """
    df = pd.DataFrame({
        "a": [1, 2, 3]
    })

    result = apply_filters(df=df, rules=[])

    pd.testing.assert_frame_equal(result, df)


def test_apply_filters_no_matches_returns_empty_df_same_schema():
    """Testing cases with no matches. Expected result is an empty dataframe.
    :return:
    """
    df = pd.DataFrame({
        "pe_ratio": [1, 2, 3]
    })

    rules = [
        FilterRule(
            field='pe_ratio',
            operator='>',
            value=100
        )
    ]

    result = apply_filters(df=df, rules=rules)

    assert result.empty
    assert list(result.columns) == ['pe_ratio']


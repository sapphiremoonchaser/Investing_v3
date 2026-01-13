from unittest import result

import pandas as pd

from stock_screener.data.models.filter import FilterRule
from stock_screener.data.services.filtering.pandas import rule_to_mask


def test_apply_filter_greater_than():
    df = pd.DataFrame({
        'pe_ratio': [5, 10,15]
    })

    rule = FilterRule(
        field='pe_ratio',
        operator='>',
        value=10
    )

    result = rule_to_mask(df, rule)

    assert len(result) == 1
    assert result.iloc[0]['pe_ratio'] == 15

def test_apply_filter_less_than():
    df = pd.DataFrame({
        'pe_ratio': [5, 10,15]
    })

    rule = FilterRule(
        field='pe_ratio',
        operator='<',
        value=10
    )

    result = rule_to_mask(df, rule)

    assert len(result) == 1
    assert result.iloc[0]['pe_ratio'] == 5

def test_apply_filter_greater_than_or_equal_to():
    df = pd.DataFrame({
        'pe_ratio': [5, 10, 15]
    })

    rule = FilterRule(
        field='pe_ratio',
        operator='>=',
        value=10
    )

    result = rule_to_mask(df, rule)

    assert len(result) == 1
    assert result.iloc[0]['pe_ratio'] == 10

def test_apply_filter_less_than_or_equal_to():
    df = pd.DataFrame({
        'pe_ratio': [5, 10, 15]
    })

    rule = FilterRule(
        field='pe_ratio',
        operator='<=',
        value=10
    )

    result = rule_to_mask(df, rule)

    assert len(result) == 1
    assert result.iloc[0]['pe_ratio'] == 10

def test_apply_filter_equal_to():
    df = pd.DataFrame({
        'pe_ratio': [5, 10, 15]
    })

    rule = FilterRule(
        field='pe_ratio',
        operator='==',
        value=10
    )

    result = rule_to_mask(df, rule)

    assert len(result) == 1
    assert result.iloc[0]['pe_ratio'] == 10
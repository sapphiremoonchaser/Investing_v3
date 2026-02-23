import pytest
from stock_screener.data.models.filter import FilterRule


def test_filter_rule_valid():
    rule = FilterRule(
        field='pe_ratio',
        operator='>',
        value=10
    )

    assert rule.field == 'pe_ratio'
    assert rule.operator == '>'
    assert rule.value == 10


def test_filter_rule_invalid():
    with pytest.raises(ValueError):
        FilterRule(
            field='pe_ratio',
            operator='INVALID',
            value=10
        )


def test_filter_rule_str_numeric():
    rule = FilterRule(
        field='pe_ratio',
        operator='>',
        value=10
    )

    assert str(rule) == 'pe_ratio > 10'


def test_filter_rule_str_percentage():
    rule = FilterRule(
        field='dividend_yield',
        operator='>',
        value=0.05
    )

    assert str(rule) == "dividend_yield > 5.00%"


def test_filter_rule_str_billions():
    rule = FilterRule(
        field='market_cap',
        operator='>',
        value=3e9
    )

    assert str(rule) == 'Market Cap > 3.0B'


def test_filter_rule_label_numeric():
    rule = FilterRule(
        field='pe_ratio',
        operator='>',
        value=10
    )

    assert str(rule.label()) == 'Pe Ratio > 10'


def test_filter_rule_label_percentage():
    rule = FilterRule(
        field='dividend_yield',
        operator='>',
        value=0.05
    )

    assert str(rule.label()) == "Dividend Yield > 5.00%"


def test_filter_rule_label_billions():
    rule = FilterRule(
        field='market_cap',
        operator='>',
        value=3e9
    )

    assert str(rule) == 'Market Cap > 3.0B'

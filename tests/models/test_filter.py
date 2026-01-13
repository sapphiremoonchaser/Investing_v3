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
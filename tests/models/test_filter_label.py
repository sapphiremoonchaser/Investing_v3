import pytest

from stock_screener.data.models.filter import FilterRule
from stock_screener.data.enums.stock_field import StockField

@pytest.mark.parametrize(
    "field, operator, value, expected_label",
    [
        # price special formatting (dollar sign, 2 decimal places)
        (StockField.price, "==", 208.23, "Price == 208.23")
        # (StockField.price, "<=", 208.23, "Price <= 208.23"),
        # (StockField.price, ">=", 208.23, "Price >= 208.23"),
        # (StockField.price, "<=", 0, "Price <= 0.00"),
        # (StockField.price, ">=", 0, "Price >= 0.00"),

        # dividend_yield special formatting (percentage, 0 decimal places)


        # avg_daily_volume special formatting (thousands)


        # market_cap special formatting (billions, 1 decimal place)


        # Regular numeric fields (title, case, raw value)
        # pe_ratio, pb_ratio


        # String field (sector, no special formatting)


        # Mixed / edge cases
        # Dividend yeild = 0 and market_cap = 0, and price = 0
    ]
)
def test_filter_rule_label(
    field,
    operator,
    value,
    expected_label,
):
    rule = FilterRule(
        field=field,
        operator=operator,
        value=value
    )

    assert rule.label == expected_label
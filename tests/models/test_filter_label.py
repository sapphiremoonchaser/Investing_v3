import pytest

from stock_screener.data.models.filter import FilterRule
from stock_screener.data.enums.stock_field import StockField

@pytest.mark.parametrize(
    "field, operator, value, expected_label",
    [
        # price special formatting (dollar sign, 2 decimal places)
        (StockField.price, "==", 208.23, "Price == $208.23"),
        (StockField.price, "<=", 0.124, "Price <= $0.12"),
        (StockField.price, ">=", 1234.56, "Price >= $1,234.56"),
        (StockField.price, "<=", 0, "Price <= $0.00"),
        (StockField.price, ">=", 0, "Price >= $0.00"),
        (StockField.price, "==", 0, "Price == $0.00"),

        # dividend_yield special formatting (percentage, 0 decimal places)
        (StockField.dividend_yield, "==", 0.03, "Dividend Yield == 3%"),
        (StockField.dividend_yield, "<=", 0.12, "Dividend Yield <= 12%"),
        (StockField.dividend_yield, ">=", 0.01, "Dividend Yield >= 1%"),
        (StockField.dividend_yield, "==", 0, "Dividend Yield == 0%"),
        (StockField.dividend_yield, ">=", 0, "Dividend Yield >= 0%"),
        (StockField.dividend_yield, "<=", 0, "Dividend Yield <= 0%"),

        # avg_daily_volume special formatting (thousands)
        (StockField.avg_daily_volume, "==", 2_100_000, "Avg Daily Volume == 2.1M"),
        (StockField.avg_daily_volume, "<=", 200_000, "Avg Daily Volume <= 200K"),
        (StockField.avg_daily_volume, ">=", 200, "Avg Daily Volume >= 200"),
        (StockField.avg_daily_volume, ">=", 9, "Avg Daily Volume >= 9"),
        (StockField.avg_daily_volume, "==", 0, "Avg Daily Volume == 0"),
        (StockField.avg_daily_volume, ">=", 0, "Avg Daily Volume >= 0"),
        (StockField.avg_daily_volume, "<=", 0, "Avg Daily Volume <= 0"),

        # market_cap special formatting (billions, 1 decimal place)
        (StockField.market_cap, "==", 4_500_000_000, "Market Cap == $4.5B"),
        (StockField.market_cap, "<=", 2_100_000, "Market Cap <= $2.1M"),
        (StockField.market_cap, ">=", 200_000, "Market Cap >= $200K")


        # Regular numeric fields (title, case, raw value)
        # pe_ratio, pb_ratio


        # String field (sector, no special formatting)


        # Mixed
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

    assert rule.label() == expected_label
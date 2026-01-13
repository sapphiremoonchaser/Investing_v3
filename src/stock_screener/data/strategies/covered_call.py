from stock_screener.data.models.filter import FilterRule
from stock_screener.data.models import ScreenerPreset

COVERED_CALL_PRESET = ScreenerPreset(
    name='Covered Call',
    description='Income-focused stocks suitable for covered call strategies',
    filters=[
        FilterRule(
            field='dividend_yield',
            operator='>',
            value=0.3
        ),
        FilterRule(
            field='market_cap',
            operator='>',
            value=2_000_000_000
        ),
        FilterRule(
            field='avg_daily_volume',
            operator='>',
            value=200_000
        ),
        FilterRule(
            field='pe_ratio',
            operator='<',
            value=15
        ),
        FilterRule(
            field='pb_ratio',
            operator='<',
            value=2
        ),
        FilterRule(
            field='price',
            operator='<=',
            value=20
        ),
    ],
)
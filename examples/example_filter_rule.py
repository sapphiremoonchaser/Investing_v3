from stock_screener.data.models.filter import FilterRule

rule = FilterRule(
    field='dividend_yield',
    operator='>',
    value=0.03
)

print(rule)

x = 1
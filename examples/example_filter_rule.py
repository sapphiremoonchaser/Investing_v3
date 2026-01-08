from src.stock_screener.data_models.filter import FilterRule

rule = FilterRule(
    field='dividend_yield',
    operator='>',
    value=0.3
)

print(rule)

x = 1
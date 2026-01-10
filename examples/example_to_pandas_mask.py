from src.stock_screener.data_models.filter import FilterRule as rule

mask = rule.to_mask(df)
df = df[mask]


# Filter over multiple rules
for rule in rules:
    df = df[
        rule.to_pandas_mask(df)
    ]
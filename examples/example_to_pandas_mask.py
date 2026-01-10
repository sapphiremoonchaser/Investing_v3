from src.stock_screener.data_models.filter import FilterRule as rule

mask = rule.to_mask(df)
df = df[mask]
"""Integration Test for data/services/screener.py

Tests to make sure the following are working together correctly:
    - FilterRule
    - rule_to_mask()
    - apply_filters()
    - pandas indexing behavior

Behaviors that matter:
    - applies rules sequentially (may be more important if I add OR logic later)
    - uses AND logic
    - returns a DataFrame with the same schema
"""

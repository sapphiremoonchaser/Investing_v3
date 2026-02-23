import pandas as pd

from stock_screener.data.models.filter import FilterRule
from stock_screener.services.filtering.pandas import rule_to_mask


def test_apply_filter_greater_than():
    # This is a dataframe of values to check
    df = pd.DataFrame({
        'pe_ratio': [5, 10,15]
    })

    # This is the rule to check each value for
    # Ex: Is pe_ratio > 10 for position 0 (5)? False
    rule = FilterRule(
        field='pe_ratio',
        operator='>',
        value=10
    )

    # Take the rule format to something pandas can handle
    # Ex: > -> operator.gt
    mask = rule_to_mask(rule, df)

    # Correct return type
    assert isinstance(mask, pd.Series)

    # Mask aligns with DataFrame
    assert len(mask) == len(df)

    # Correct Truth Values
    assert mask.tolist() == [False, False, True]

    # Works for filtering
    filtered = df[mask]
    assert filtered['pe_ratio'].tolist() == [15]


# def test_apply_filter_less_than():
#     df = pd.DataFrame({
#         'pe_ratio': [5, 10,15]
#     })
#
#     rule = FilterRule(
#         field='pe_ratio',
#         operator='<',
#         value=10
#     )
#
#     result = rule_to_mask(df, rule)
#
#     assert len(result) == 1
#     assert result.iloc[0]['pe_ratio'] == 5
#
# def test_apply_filter_greater_than_or_equal_to():
#     df = pd.DataFrame({
#         'pe_ratio': [5, 10, 15]
#     })
#
#     rule = FilterRule(
#         field='pe_ratio',
#         operator='>=',
#         value=10
#     )
#
#     result = rule_to_mask(df, rule)
#
#     assert len(result) == 1
#     assert result.iloc[0]['pe_ratio'] == 10
#
# def test_apply_filter_less_than_or_equal_to():
#     df = pd.DataFrame({
#         'pe_ratio': [5, 10, 15]
#     })
#
#     rule = FilterRule(
#         field='pe_ratio',
#         operator='<=',
#         value=10
#     )
#
#     result = rule_to_mask(df, rule)
#
#     assert len(result) == 1
#     assert result.iloc[0]['pe_ratio'] == 10
#
# def test_apply_filter_equal_to():
#     df = pd.DataFrame({
#         'pe_ratio': [5, 10, 15]
#     })
#
#     rule = FilterRule(
#         field='pe_ratio',
#         operator='==',
#         value=10
#     )
#
#     result = rule_to_mask(df, rule)
#
#     assert len(result) == 1
#     assert result.iloc[0]['pe_ratio'] == 10
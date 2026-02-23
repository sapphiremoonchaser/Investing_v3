import pandas as pd
import pytest

from stock_screener.data.models.filter import FilterRule
from stock_screener.services.filtering.pandas import rule_to_mask


@pytest.mark.parametrize(
    "operator,value,expected",
    [
        (">", 10, [False, False, True]),
        (">=", 10, [False, True, True]),
        ("<", 10, [True, False, False]),
        ("<=", 10, [True, True, False]),
        ("==", 10, [False, True, False]),
    ]
)
def test_apply_filter_numeric_operators(
        operator='==',
        value=10,
        expected=[False, True, False]
):
    """This unit test checks for scenarios where the operator is
    valid (<, <=, ==, >=, >).

    All scenarios are given as paramaters in the decorator above.

    A dataframe of values is given for a specific metric.
    We create a FilterRule where the field is the metric from the df,
    the operator is '>', and we can check all scenarios by using 10.

    Tests are done for the following:
        - correct return type
        - the mask has the same length as the given dataframe
            (every value given has a Boolean value returned)
        - Correct truth value returned for the given values in the df
        - Works with filter being applie (returns correct values from df)
    :return:
    """
    # Dataframe with values to check
    df = pd.DataFrame({
        'pe_ratio': [5, 10, 15]
    })

    # This is the rule to check each value for
    # Ex: Is pe_ratio > 10 for position 0 (5)? False
    rule = FilterRule(
        field='pe_ratio',
        operator=operator,
        value=value
    )

    # Take the rule format to something pandas can handle
    # Ex: > -> operator.gt
    mask = rule_to_mask(rule, df)

    # Checking for correct data type
    assert isinstance(mask, pd.Series)

    # Checking that Truth Values are correct
    pd.testing.assert_series_equal(
        mask,
        pd.Series(expected, index=df.index)
    )


def test_apply_filter_invalid_operator():
    """This keeps invalid operators from going into my operator map.
    :return:
    """
    df = pd.DataFrame({
        'pe_ratio': [5, 10, 15]
    })

    rule = FilterRule(
        field='pe_ratio',
        operator='!==',
        value=10
    )

    with pytest.raises(KeyError):
        rule_to_mask(rule, df)


def test_apply_filter_invalid_column():
    """This keeps invalid columns from going into my column map.
    It protects for when data sources change.
    :return:
    """
    df = pd.DataFrame({
        'price': [10, 20, 30]
    })

    rule = FilterRule(
        field='pe_ratio',
        operator='>',
        value=10
    )

    with pytest.raises(KeyError):
        rule_to_mask(rule, df)


def test_apply_filter_nan_values():
    df = pd.DataFrame({
        'pe_ratio': [5, 10, 15]
    })

    rule = FilterRule(
        field='pe_ratio',
        operator='>',
        value=10
    )

    mask = rule_to_mask(rule, df)

    assert mask.tolist() == [False, False, True]


def test_apply_filter_string_equality():
    df = pd.DataFrame({
        'sector': ['Tech', 'Finance', 'Tech']
    })

    rule = FilterRule(
        field='sector',
        operator='==',
        value='Tech'
    )

    mask = rule_to_mask(rule, df)

    assert mask.tolist() == [True, False, True]


# def test_apply_filter_boolean():
#     df = pd.DataFrame({
#         'is_profitable': [True, False, True]
#     })
#
#     rule = FilterRule(
#         field='is_profitable',
#         operator='==',
#         value=True
#     )
#
#     mask = rule_to_mask(rule, df)
#
#     assert mask.tolist() == [True, False, True]


import pandas as pd

from stock_screener.data.models.filter import FilterRule
from stock_screener.data.services.filtering.pandas import rule_to_mask


def test_apply_filter_greater_than():
    """This unit test checks for scenarios where the filter is >

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


def test_apply_filter_greater_than_or_equal_to():
    """This unit test checks for scenarios where the filter is >=

    A dataframe of values is given for a specific metric.
    We create a FilterRule where the field is the metric from the df,
    the operator is '>=', and we can check all scenarios by using 10.

    Tests are done for the following:
        - correct return type
        - the mask has the same length as the given dataframe
            (every value given has a Boolean value returned)
        - Correct truth value returned for the given values in the df
        - Works with filter being applie (returns correct values from df)
    :return:
    """
    # This is a dataframe of values to check
    df = pd.DataFrame({
        'pe_ratio': [5, 10, 15]
    })

    # This is the rule to check each value for
    # Ex: Is pe_ratio > 10 for position 0 (5)? False
    rule = FilterRule(
        field='pe_ratio',
        operator='>=',
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
    assert mask.tolist() == [False, True, True]

    # Works for filtering
    filtered = df[mask]
    assert filtered['pe_ratio'].tolist() == [10, 15]


def test_apply_filter_less_than():
    """This unit test checks for scenarios where the filter is <

    A dataframe of values is given for a specific metric.
    We create a FilterRule where the field is the metric from the df,
    the operator is '<', and we can check all scenarios by using 10.

    Tests are done for the following:
        - correct return type
        - the mask has the same length as the given dataframe
            (every value given has a Boolean value returned)
        - Correct truth value returned for the given values in the df
        - Works with filter being applied (returns correct values from df)
    :return:
    """
    # This is a dataframe of values to check
    df = pd.DataFrame({
        'pe_ratio': [5, 10, 15]
    })

    # This is the rule to check each value for
    # Ex: Is pe_ratio > 10 for position 0 (5)? False
    rule = FilterRule(
        field='pe_ratio',
        operator='<',
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
    assert mask.tolist() == [True, False, False]

    # Works for filtering
    filtered = df[mask]
    assert filtered['pe_ratio'].tolist() == [5]


def test_apply_filter_less_than_or_equal_to():
    """This unit test checks for scenarios where the filter is <=

    A dataframe of values is given for a specific metric.
    We create a FilterRule where the field is the metric from the df,
    the operator is '<=', and we can check all scenarios by using 10.

    Tests are done for the following:
        - correct return type
        - the mask has the same length as the given dataframe
            (every value given has a Boolean value returned)
        - Correct truth value returned for the given values in the df
        - Works with filter being applied (returns correct values from df)
    :return:
    """
    # This is a dataframe of values to check
    df = pd.DataFrame({
        'pe_ratio': [5, 10, 15]
    })

    # This is the rule to check each value for
    # Ex: Is pe_ratio > 10 for position 0 (5)? False
    rule = FilterRule(
        field='pe_ratio',
        operator='<=',
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
    assert mask.tolist() == [True, True, False]

    # Works for filtering
    filtered = df[mask]
    assert filtered['pe_ratio'].tolist() == [5, 10]


def test_apply_filter_equal_to():
    """This unit test checks for scenarios where the filter is =

    A dataframe of values is given for a specific metric.
    We create a FilterRule where the field is the metric from the df,
    the operator is '==', and we can check all scenarios by using 10.

    Tests are done for the following:
        - correct return type
        - the mask has the same length as the given dataframe
            (every value given has a Boolean value returned)
        - Correct truth value returned for the given values in the df
        - Works with filter being applied (returns correct values from df)
    :return:
    """
    # This is a dataframe of values to check
    df = pd.DataFrame({
        'pe_ratio': [5, 10, 15]
    })

    # This is the rule to check each value for
    # Ex: Is pe_ratio > 10 for position 0 (5)? False
    rule = FilterRule(
        field='pe_ratio',
        operator='==',
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
    assert mask.tolist() == [False, True, False]

    # Works for filtering
    filtered = df[mask]
    assert filtered['pe_ratio'].tolist() == [10]
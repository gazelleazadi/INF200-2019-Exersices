import pytest

__author__ = 'Ghazal_Azadi'
__email__ = '@ghazal.azadinmbu.no'


def median(data):
    # The main function which tests would be performed on it afterwards
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    sdata = sorted(data)
    n = len(sdata)
    if n == 0:
        raise ValueError("The list must contain at least one element")
    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_single():
    """Test that the median function works for one element list"""
    assert median([2]) == 2


def test_odd_length():
    """Test that the median function works for odd number of elements"""
    assert median([1, 2, 4]) == 2


def test_even_length():
    """Test that the median function works for even number of elements"""
    assert median([1, 2, 4, 6]) == 3


def test_reversed():
    """Test that the median function works for reversed ordered lists"""
    reversed_list = sorted([4, 1, 3, 7, 5], reverse=True)
    assert median(reversed_list) == 4


def test_median_raises_value_error_on_empty_list():
    """Test that the median function returns ValueError exception for emmty
    list input"""
    with pytest.raises(ValueError):
        median([])

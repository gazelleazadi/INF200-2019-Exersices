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


def test_ordered():
    """Test that the median function works for ordered lists"""
    ordered_list = sorted([4, 1, 3, 7, 5])
    assert median(ordered_list) == 4


def test_unordered():
    """Test that the median function works for unordered lists"""
    unordered_list = [4, 1, 3, 7, 5]
    assert median(unordered_list) == 4


def test_median_raises_value_error_on_empty_list():
    """Test that the median function returns ValueError exception for empty
    list input"""
    with pytest.raises(ValueError):
        median([])


def test_original_unchanged():
    """Test that ensures the median function leaves the original data
     unchanged."""
    data = [3, 7, 11, 4, 9, 10]
    median(data)
    assert data == [3, 7, 11, 4, 9, 10]


def test_tuples():
    """Test that ensures that the median function works for tuples as well
     as lists"""
    tuple_data = (3, 5, 9, 12, 8)
    assert median(tuple_data) == 8

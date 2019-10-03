__author__ = 'Ghazal_Azadi'
__email__ = '@ghazal.azadi@nmbu.no'


def bubble_sort(my_data):
    # The main function which tests would be performed on it afterwards
    my_data = list(my_data)
    # Changing type of data to list which becomes mutable
    dim = len(my_data)
    made_swap = True
    swaps = 0
    while made_swap:
        made_swap = False
        for cnt in range(dim-1):
            if my_data[cnt] > my_data[cnt+1]:
                my_data[cnt], my_data[cnt+1] = my_data[cnt+1], my_data[cnt]
            # Comparing elements and swap them if needed.
                made_swap = True
                swaps = swaps + 1
    return my_data


def test_empty():
    """Test that the sorting function works for empty list"""
    empty_list = []
    assert bubble_sort(empty_list) == empty_list


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    assert bubble_sort(data) != data


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert bubble_sort(sorted_data) == sorted_data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [3, 1, 2]
    reverse_sorted = sorted(data, reverse=True)
    assert bubble_sort(reverse_sorted) == sorted(data)


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    identical_list = [1, 1, 1, 1, 1]
    assert bubble_sort(identical_list) == identical_list


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    string_list = ['m', 'n', 'q', 'a', 'i']
    int_list = [5, 9, 5, 1, 4]
    for i in range(len(string_list)-1):
        assert bubble_sort(string_list)[i] < bubble_sort(string_list)[i+1]
        assert bubble_sort(int_list)[i] <= bubble_sort(int_list)[i+1]

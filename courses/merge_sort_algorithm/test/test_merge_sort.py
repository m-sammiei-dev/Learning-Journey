
from merge_sort import merge_sort

def test_merge_sort_ascending():
    numbers = [5, 1, 9, 3]
    merge_sort(numbers)
    assert numbers == [1, 3, 5, 9]


def test_merge_sort_descending():
    numbers = [5, 1, 9, 3]
    merge_sort(numbers, reverse=True)
    assert numbers == [9, 5, 3, 1]


def test_merge_sort_empty_list():
    numbers = []
    merge_sort(numbers)
    assert numbers == []


def test_merge_sort_single_element():
    numbers = [7]
    merge_sort(numbers)
    assert numbers == [7]


def test_merge_sort_with_duplicates():
    numbers = [4, 2, 4, 1, 2]
    merge_sort(numbers)
    assert numbers == [1, 2, 2, 4, 4]


def test_merge_sort_with_negative_numbers():
    numbers = [-3, 7, 0, -1, 5]
    merge_sort(numbers)
    assert numbers == [-3, -1, 0, 5, 7]


def test_merge_sort_comparison_count():
    numbers = [5, 1, 9, 3]
    stats = {"comparisons": 0}
    merge_sort(numbers, stats=stats)

    assert numbers == [1, 3, 5, 9]
    assert stats["comparisons"] > 0

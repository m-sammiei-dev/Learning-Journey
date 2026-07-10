def merge_sort(array, reverse=False, stats=None):
    """Sort array in-place using merge sort.

    Args:
        array: List of comparable elements to sort.
        reverse: If True, sort in descending order.
        stats: Optional dict to track comparison count.

    Returns:
        None. The array is modified in-place.
    """
     
    if len(array) <= 1:
        return

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    merge_sort(left_half, reverse, stats)
    merge_sort(right_half, reverse, stats)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if stats is not None:
            stats["comparisons"] += 1

        if (left_half[i] <= right_half[j] and not reverse) or (
            left_half[i] >= right_half[j] and reverse
        ):
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1

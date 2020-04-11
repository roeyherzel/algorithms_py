
def _swap(a: list, i: int, j: int):
    """
    swap values between 2 indexes on a list
    """
    a[j], a[i] = a[i], a[j]

def _partition(a: list, start: int, end: int) -> int:
    """
    rearrange list segment to items < pivot < items
    where pivot is the value from the end of the segment
    """
    pivot = a[end]

    # set partiton index as start
    part_idx = start

    for i in range(start, end):
        if a[i] < pivot:
            # swap if element is lesser then pivot
            _swap(a, i, part_idx)
            part_idx = part_idx + 1

    # swap pivot with element at partition index
    _swap(a, part_idx, end)

    return part_idx

def _sort(a, start, end):
    if start < end:
        partition_idx = _partition(a, start, end)
        _sort(a, start, partition_idx-1)
        _sort(a, partition_idx+1, end)

def quick_sort(a):
    """
    sort list in-place
    - time complexity: O(n log n) -> O(n^2) worst
    - space complexity: O(log n)
    """
    _sort(a, 0, len(a)-1)

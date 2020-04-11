def _merge(left: list, right: list) -> list:
    """
    merge 2 lists in time complexity of O(n)
    """
    left_len: int = len(left)
    right_len: int = len(right)
    merged: list = [None]*(left_len+right_len)

    l = 0
    r = 0
    m = 0

    # pick smallest between left and right
    while l < left_len and r < right_len:
        if left[l] < right[r]:
            merged[m] = left[l]
            l = l+1
        else:
            merged[m] = right[r]
            r = r+1
        m = m+1

    # add leftovers left or right
    while l < left_len:
        merged[m] = left[l]
        l = l+1
        m = m+1

    while r < right_len:
        merged[m] = right[r]
        r = r+1
        m = m+1

    return merged

def merge_sort(a: list) -> list:
    """
    return a sortted
    - time complexity: O(n log n)
    - space complexity: O(n)
    """
    if len(a) < 2:
        return a

    mid = len(a) // 2
    left = a[0:mid]
    right = a[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return _merge(left, right)
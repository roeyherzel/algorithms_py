
"""
* we want to spilt untill we have 2 arrays with 1 element
1. split array into 2 (left,right)
2. sort left array
3. sort right array
4. merge left and right

0. [2,4,1,6,8,5,3,7]
       /       \
1. [2,4,1,6] [8,5,3,7]
2. [1,2,4,6]
3.           [3,5,7,8]
4. [1,2,3,4,5,6,7,8]
"""

def merge_sort(a: list):
    """
    sort list in complexity of O(nlogn)
    """
    if len(a) < 2:
        return a

    mid = len(a) // 2
    left = a[0:mid]
    right = a[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left: list, right: list):
    """
    merge 2 lists
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
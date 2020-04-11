from .merge_sort import _merge, merge_sort


class TestMerge:
    def test_merge_sorted_lists(self):
        a = [1,2,4,6]
        b = [3,5,7,8]

        assert _merge(a, b) == [1,2,3,4,5,6,7,8]
        assert _merge(b, a) == [1,2,3,4,5,6,7,8]

    def test_merge_unsorted_lists(self):
        a = [2,1,6,4]
        b = [3,5,7,8]

        assert _merge(a, b) == [2,1,3,5,6,4,7,8]

class TestMergeSort:
    def test_sort_unsorted_list(self):
        assert merge_sort([2,4,1,6,8,5,3,7]) == [1,2,3,4,5,6,7,8]

    def test_sort_sorted_list(self):
        assert merge_sort([1,2,3,4,5,6,7,8]) == [1,2,3,4,5,6,7,8]

    def test_sort_odd_length_list(self):
        assert merge_sort([2,4,1,6,8,5,3]) == [1,2,3,4,5,6,8]

    def test_sort_empty_list(self):
        assert merge_sort([]) == []

    def test_sort_single_item(self):
        assert merge_sort([1]) == [1]

    def test_sort_negative_item(self):
        assert merge_sort([2,-4,1,6,8,5,3,-7]) == [-7,-4,1,2,3,5,6,8]

from .quick_sort import quick_sort


class TestQuickSort:
    def test_sort_unsorted_list(self):
        a = [2,4,1,6,8,5,3,7]
        quick_sort(a)

        assert a == [1,2,3,4,5,6,7,8]

    def test_sort_sorted_list(self):
        a = [1,2,3,4,5,6,7,8]
        quick_sort(a)

        assert a == [1,2,3,4,5,6,7,8]

    def test_sort_odd_length_list(self):
        a = [2,4,1,6,8,5,3]
        quick_sort(a)

        assert a == [1,2,3,4,5,6,8]

    def test_sort_empty_list(self):
        a = []
        quick_sort(a)

        assert a == []

    def test_sort_single_item(self):
        a = [1]
        quick_sort(a)

        assert a == [1]

    def test_sort_negative_item(self):
        a = [2,-4,1,6,8,5,3,-7]
        quick_sort(a)

        assert a == [-7,-4,1,2,3,5,6,8]
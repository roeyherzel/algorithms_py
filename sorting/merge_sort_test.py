from .merge_sort import merge


class TestMerge:
    def test_merge_sorted_lists(self):
        a = [1,2,4,6]
        b = [3,5,7,8]

        assert merge(a, b) == [1,2,3,4,5,6,7,8]
        assert merge(b, a) == [1,2,3,4,5,6,7,8]

    def test_merge_unsorted_lists(self):
        a = [2,1,6,4]
        b = [3,5,7,8]

        assert merge(a, b) == [2,1,3,5,6,4,7,8]
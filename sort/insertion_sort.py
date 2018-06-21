import random

from sort import Sort


class InsertionSort(Sort):
    """Quadratic running time"""

    def _sort(self, items):
        N = len(items)
        for i in range(1, N):
            j = i
            while j > 0 and self.less(items[j], items[j-1]):
                self.change(items, j, j-1)
                j -= 1


if __name__ == '__main__':
    my_items = [random.random() for i in range(30)]
    sorter = InsertionSort()
    sorter.sort(my_items)

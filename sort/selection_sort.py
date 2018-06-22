import random

from sort import Sort


class SelectionSort(Sort):
    """Quadratic running time"""

    def _sort(self, items):
        N = len(items)
        for i in range(N):
            min_ = i
            for j in range(i + 1, N):
                if self.less(items[j], items[min_]):
                    min_ = j
            self.change(items, i, min_)


if __name__ == '__main__':
    my_items = [random.random() for i in range(30)]
    sorter = SelectionSort()
    sorter.sort(my_items)
    print('working')

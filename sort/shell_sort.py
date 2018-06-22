import random

from sort import Sort


class ShellSort(Sort):
    def _sort(self, items):
        N = len(items)
        h = 1
        while h < N // 3:
            h = 3 * h + 1
        while h >= 1:
            i = h
            while i < N:
                j = i
                while j >= h and self.less(items[j], items[j-h]):
                    self.change(items, j, j-h)
                    j -= h
                i += 1
            h = h // 3


if __name__ == '__main__':
    sorter = ShellSort()
    data = [random.random() for i in range(30)]
    sorter.sort(data)
    print('working')

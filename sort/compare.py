import random

from utils.sort_compare import SortCompare
from selection_sort import SelectionSort
from insertion_sort import InsertionSort
from shell_sort import ShellSort

d = [random.random() for _ in range(100)]
data = {
    'random': d,
    'reversed': sorted(d, reverse=True),
    'sorted': sorted(d)
    }


ALGS = (SelectionSort, InsertionSort, ShellSort)


def compare(alg, data):
    data = data.copy()
    res = SortCompare.speed_test(alg, data)
    print(alg.__name__, res)


if __name__ == '__main__':
    for key, value in data.items():
        print(key)
        for alg in ALGS:
            compare(alg, value)

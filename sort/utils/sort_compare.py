import random
import time


class SortCompare:

    def __init__(self, array_size=1000, times=100):
        self.array_size = array_size
        self.times = times

    def compare_two(self, algorithm_1, algorithm_2):
        data = self.generate_arrays(self.array_size, self.times)
        first = second = 0
        first += self.time_it(algorithm_1, data.copy())
        second += self.time_it(algorithm_1, data.copy())
        return first / second

    def time_it(self, algorithm, data):
        total = 0
        for _ in range(self.times):
            total += self.speed_test(algorithm, data)
        return total

    @classmethod
    def speed_test(cls, algorithm, data):
        if callable(algorithm):
            algorithm = algorithm()
        start = time.time()
        algorithm.sort(data)
        return time.time() - start

    def generate_arrays(self, number, size):
        return [self.generate_array(number) for _ in range(number)]

    def generate_array(self, size):
        return [random.random() for _ in range(size)]

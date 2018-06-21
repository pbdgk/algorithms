class Sort():

    _debug = True

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, debug):
        self._debug = debug

    @staticmethod
    def less(first, second):
        return first < second

    @staticmethod
    def change(items, i, j):
        items[i], items[j] = items[j], items[i]

    @staticmethod
    def show(items):
        for item in items:
            print(item)

    def is_sorted(self, items):
        for i in range(1, len(items)):
            if self.less(items[i], items[i-1]):
                return False
        return True

    def sort(self, items):
        self._sort(items)
        assert self.is_sorted(items)
        if self.debug:
            self.show(items)
        return items

    def _sort(items):
        raise ValueError("""
            You have to override this method in subclass.
            Don't create objects from this class.
            """)

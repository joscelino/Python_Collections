from collections.abc import MutableSequence


class MyList(MutableSequence):
    def __init__(self, list_):
        self._d = list(list_)

    def __getitem__(self, pos):
        return self._d[pos]

    def __delitem__(self, pos):
        del(self._d[pos])

    def __setitem__(self, pos, val):
        self._d[pos] = val

    def __len__(self):
        return len(self._d)

    def __repr__(self):
        return '{}'.format(self._d)

    def insert(self, pos, val):
        self._d.insert(pos, val)

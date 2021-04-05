from myabc import Functor


class MyFunctor(Functor):

    def __init__(self, list_):
        self._d = list_

    def __getitem__(self, pos):
        return self._d[pos]

    def __len__(self):
        return len(self._d)

    def fmap(self, function):
        return [function(x) for x in self._d]

    def __repr__(self):
        return '{}'.format(self._d)

    def __mul__(self, functor):
        if isinstance(functor, Functor):
            return list(map(lambda value: [func(value) for func in functor], self._d))

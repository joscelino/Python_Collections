from collections import deque


class Fila:
    def __init__(self):
        self.fila = deque()

    def insere(self, val):
        self.fila.append(val)

    def remove(self):
        try:
            return self.fila.popleft()
        except IndexError:
            print('Fila vazia!')

    def __repr__(self):
        return 'Fila [{}]'.format(', '.join(str(x) for x in self.fila))

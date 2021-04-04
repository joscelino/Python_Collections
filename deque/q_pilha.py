from collections import deque


class Pilha:
    def __init__(self):
        self.pilha = deque()

    def insere(self, val):
        self.pilha.append(val)

    def remove(self):
        try:
            return self.pilha.pop()
        except IndexError:
            print('Pilha vazia!')

    def __repr__(self):
        return 'Pilha [{}]'.format(', '.join(str(x) for x in self.pilha))
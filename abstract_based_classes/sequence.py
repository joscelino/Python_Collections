from collections.abc import Sequence


class MySequence(Sequence):
    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, pos):
        return self.seq[pos]

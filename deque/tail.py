from collections import deque


def tail(filename, n=10):
    with open(filename, 'r', encoding='utf-8') as f:
        return deque(f, n)

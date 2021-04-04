from collections import ChainMap

a = {1: 'a', 2: 'b', 3: 'c'}
b = {2: 'x', 3: 'z',4: 'd'}

c = ChainMap(a, b)

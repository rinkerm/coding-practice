from itertools import groupby
s = input()
sg = groupby(s)
for char, group in sg:
    print('({}, {})'.format(len(list(group)),char),end=' ')

# count é um iterador sem fim(itertools)

from itertools import count

c1 = count(step=16, start=8)
r1 = range(16, 100, 8)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('c1', hasattr(r1, '__iter__'))
print('c1', hasattr(r1, '__next__'))
print('count')


for i in c1:
    if i >= 100:
        break

print()
print('range')

for i in r1:
    print(i)

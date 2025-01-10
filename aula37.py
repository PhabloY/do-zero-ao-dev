import importlib

import aula37_m

print(aula37_m.variavel)

for i in range(10):
    importlib.reload(aula37_m)
    print(i)
print('Fim')
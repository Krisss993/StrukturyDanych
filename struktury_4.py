t1 = (1,'cos',['sad','las'])
print(t1[2][1])

print((*t1, 99))
print(t1+(99,))

drinks = {'beer', 'milk','water'}
print('beer' in drinks)
healthy = {'milk','water', 'eggs'}

print(drinks | healthy)

print(drinks & healthy)

import time
max_limit = 50000
my_list = list(range(max_limit))
my_set = set(range(max_limit))
start = time.time()
for x in range(max_limit):
    if x not in my_list:
        print('False')
print('OK')
stop = time.time()
print(f'Operation duration was {stop - start}')

start = time.time()
for x in range(max_limit):
    if x not in my_set:
        print('False')
print('OK')
stop = time.time()
print(f'Operation duration was {stop - start}')

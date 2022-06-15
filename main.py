from random import randrange
from time import time
from radix_sort import radix_sort
from radix_sort2 import radix_sort2


test = [randrange(10**20, 10**20 + 10**5) for _ in range(10**6)]
print('starting sort...')
start = time()
radix_sort(test)
print(f'radix sort {time() - start} seconds')

start = time()
radix_sort2(test)
print(f'radix sort 2 {time() - start} seconds ')
from random import randrange
from time import time
from radix_sort import radix_sort
from radix_sort2 import radix_sort2, counting_sort_radix

test = [randrange(1, 10*4) for _ in range(10**6)]

# comparing two versions of radix sort
# complexity of first version pity is n log n, but the concept the same as in normal radix sort with complexity n * d

print(f'Testing radix sort with complexity n log n')
start1 = time()
radix_sort(test)
print(f'Ends with {time() - start1} seconds')

print(f'Testing radix sort with complexity n * d')
start2 = time()
radix_sort2(test)
print(f'Ends with {time() - start2} seconds')


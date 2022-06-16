from random import randrange
from msd import msd
from radix_sort2 import radix_sort2
from radix_sort import radix_sort
def analyse(input_size, step, function1, function2):
    import matplotlib.pyplot as plt
    from time import time
    x1 = []
    x2 = []
    naxis = []
    completed = 0
    for n in range(0, input_size, step):
        naxis.append(n)
        ar = [randrange(10**15, 10**16) for _ in range(n + 1)]
        start1 = time()
        function1(ar)
        end1 = time() - start1
        x1.append(end1)

        start2 = time()
        function2(ar)
        end2 = time() - start2
        x2.append(end2)
        if round((n/input_size)*100) > completed:
            completed = round((n/input_size)*100)
            print(f'{completed} % completed')
    plt.plot(naxis, x1, color='r')
    plt.plot(naxis, x2, color='g')
    plt.show()

analyse(10**4, 10**2, msd, radix_sort)

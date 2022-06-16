
from radix_sort2 import radix_sort2
from msd import msd

n = int(input("Введіть загальне число родин: "))
treasures = []
while n > 0:
    treasures.extend(list(map(int, list(input(f'Введіть скарби для родини {n}: ').split(" ")))))
    n -= 1

print("Ось складений список скарбів (msd): ", msd(treasures))
print("Ось складений список скарбів (lsd): ", radix_sort2(treasures))
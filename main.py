from random import randrange
from radix_sort import radix_sort
# test = [randrange(1, 100000) for _ in range(50000)]
# mx_length = len(str(max(test)))
# test = list(map(lambda x: "0" * (mx_length - len(str(x))) + str(x) if len(str(x)) < mx_length else str(x), test ))
# mx_length -= 1
# while mx_length > -1:
#     test = sorted(test, key=lambda x: x[mx_length])
#     mx_length -= 1
# for index in range(len(test)):
#     num = list(test[index])
#     while num[0] == '0':
#         num.pop(0)
#     test[index] = float(''.join(test[index]))

test = [randrange(1, 100000) for _ in range(10)]
test = radix_sort(test)
print(test)
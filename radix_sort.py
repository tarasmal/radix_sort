
def radix_sort(arr):
    mx_length = len(str(max(arr)))
    arr = list(map(lambda x: "0" * (mx_length - len(str(x))) + str(x) if len(str(x)) < mx_length else str(x), arr))
    mx_length -= 1
    while mx_length > -1:
        arr = sorted(arr, key=lambda x: x[mx_length])
        mx_length -= 1
    for index in range(len(arr)):
        num = list(arr[index])
        while num[0] == '0':
            num.pop(0)
        arr[index] = float(''.join(arr[index]))
    return arr

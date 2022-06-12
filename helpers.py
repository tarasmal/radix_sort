def reformat(arr):
    for index in range(len(arr)):
        num = list(arr[index])
        while num[0] == '0':
            num.pop(0)
        arr[index] = float(''.join(arr[index]))

    return arr

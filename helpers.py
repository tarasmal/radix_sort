def reformat(arr):
    for index in range(len(arr)):
        num = list(arr[index])
        if num == '0':
            arr[index] = int("".join(num))
            continue
        else:
            while num[0] == '0':
                if num == '0':
                    break
                num.pop(0)
            else:
                arr[index] = float(''.join(arr[index]))

    return arr


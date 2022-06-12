from helpers import reformat
def counting_sort_radix(arr, degree):
    counter = {}
    result = []
    for a in arr:
        if a not in counter.keys():
            counter[a] = 1
        else:
            counter[a] += 1
    keys = sorted(counter.keys(), key=lambda x: x[degree])
    while len(keys) != 0:
        key = keys.pop(0)
        result.extend([key] * counter[key])
    return result


def radix_sort2(arr):
    mx = len(str(max(arr)))
    arr = list(map(lambda x: "0" * (mx - len(str(x))) + str(x) if len(str(x)) < mx else str(x), arr))
    mx -= 1
    while mx > - 1:
        arr = counting_sort_radix(arr, mx)
        mx -= 1

    reformat(arr)

    return arr



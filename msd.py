

from helpers import reformat
def msd(arr):
    mx = len(str(max(arr)))
    arr = list(map(lambda x: "0" * (mx - len(str(x))) + str(x) if len(str(x)) < mx else str(x), arr))

    return reformat(msd_(arr, mx - 1))

def msd_(array, mx, index=0):
    if len(array) <= 1 or index == mx:
        return sorted(array)
    else:
        answer = []
        buckets = [[] for _ in range(10)]
        for x in array:
            buckets[int(x[index])].append(x)

        for bucket in buckets:
            answer.extend(msd_(bucket, mx, index + 1))
        return answer

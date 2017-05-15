def binSearch(arr, x):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end)/2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def hasSumPair(arr, t):
    lookup = dict()
    n = len(arr)
    for j in xrange(n):
        lookup[arr[j]] = j
    for i in xrange(n):
        x = t - arr[i]
        if x in lookup and lookup[x] != i:
            return True
    return False

print(hasSumPair([5, 4, 2, 4], 8))
print(hasSumPair([5, 1, 2, 4], 8))

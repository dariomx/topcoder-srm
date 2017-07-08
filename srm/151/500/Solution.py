class MergeSort:
    def __init__(self):
        self.cntCmp = 0

    def merge(self, left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            elif left[i] > right[j]:
                res.append(right[j])
                j += 1
            else:
                res.append(left[i])
                i += 1
                res.append(right[j])
                j += 1
            self.cntCmp += 1
        if i < len(left):
            res += left[i:]
        elif j < len(right):
            res += right[j:]
        return res

    def mergeSort(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
        else:
            mid = n / 2
            left = self.mergeSort(arr[0:mid])
            right = self.mergeSort(arr[mid:])
            return self.merge(left, right)

    def howManyComparisons(self, numbers):
        self.cntCmp = 0
        sortedNums = self.mergeSort(numbers)
        print(sortedNums)
        return self.cntCmp

numbers = [1, 2, 3, 4]
numbers = [2, 3, 2]
numbers = [-17]
numbers = []
numbers = [-2000000000,2000000000,0,0,0,-2000000000,2000000000,0,0,0]
print(MergeSort().howManyComparisons(numbers))
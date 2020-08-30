class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2 = {x: i for i, x in enumerate(arr2)}
        last = []
        first = []
        for x in arr1:
            if x in arr2:
                first.append(x)
            else:
                last.append(x)
        first.sort(key=lambda x: arr2[x])
        last.sort()
        return first + last

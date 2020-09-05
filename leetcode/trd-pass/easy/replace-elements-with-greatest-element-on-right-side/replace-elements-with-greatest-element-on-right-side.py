class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cmax = -1
        for i in reversed(range(len(arr))):
            tmp = arr[i]
            arr[i] = cmax
            cmax = max(cmax, tmp)
        return arr
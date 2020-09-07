class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        changes = n
        while changes > 0:
            tmp = [arr[0]]
            changes = 0
            for i in range(1, n - 1):
                if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    tmp.append(arr[i] + 1)
                    changes += 1
                elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    tmp.append(arr[i] - 1)
                    changes += 1
                else:
                    tmp.append(arr[i])
            tmp.append(arr[n - 1])
            arr = tmp
        return arr


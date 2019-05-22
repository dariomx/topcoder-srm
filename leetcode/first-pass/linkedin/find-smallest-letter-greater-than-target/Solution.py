class Solution:
    def nextGreatestLetter(self, letters, target):
        n = len(letters)
        start, end = 0, n-1
        ans = letters[0]
        while start <= end:
            mid = (start + end) // 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                ans = letters[mid]
                end = mid - 1
        return ans  
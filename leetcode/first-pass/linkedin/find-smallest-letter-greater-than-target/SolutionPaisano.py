# Derived from a friend's solution

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        start, end = 0, len(letters) - 1
        while start < end:
            mid = (start + end) / 2
            x = letters[mid]
            if target >= x:
                start = mid + 1
            else:
                end = mid
        if start == end and letters[start] > target:
            return letters[start]
        else:
            return letters[0]


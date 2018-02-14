"""
Python3 solution with O(n) and O(1) space

We look only at the extremes of the array, and explore 3 cases to reduce into a
shorter array where we can recurse:

1) sum is greater than target: only way to reduce sum is dropping last element

2) sum is smaller than target: only way to increase sum dropping first element

3) sum is equal to target: we are done

For the first and second cases we would recurse over the resulting sub-array.
Due efficiency reasons, we opt to implement this strategy iteratively.

"""

class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers)-1
        while True:
            psum = numbers[i] + numbers[j]
            if psum == target:
                return [i+1, j+1]
            elif psum > target:
                j -= 1
            else:
                i += 1
        return None
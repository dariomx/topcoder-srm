class Solution:
    def sortedArrayToBST(self, nums):
        def rec(start, end):
            if start > end:
                return None
            else:
                mid = (start + end) // 2
                root = TreeNode(nums[mid])
                root.left = rec(start, mid - 1)
                root.right = rec(mid + 1, end)
                return root

        return rec(0, len(nums) - 1)

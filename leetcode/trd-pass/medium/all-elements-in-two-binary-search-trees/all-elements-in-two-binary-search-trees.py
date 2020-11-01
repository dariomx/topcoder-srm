# not sure why materializing the inorder as list is faster than generators

class Solution:
    def inorder(self, root, lst):
        if root:
            self.inorder(root.left, lst)
            lst.append(root.val)
            self.inorder(root.right, lst)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lst1, lst2 = [], []
        self.inorder(root1, lst1), self.inorder(root2, lst2)
        n, m = len(lst1), len(lst2)
        i, j = 0, 0
        ans = []
        while i < n or j < m:
            if j == m or (i < n and lst1[i] < lst2[j]):
                ans.append(lst1[i])
                i += 1
            elif i == n or (j < m and lst2[j] < lst1[i]):
                ans.append(lst2[j])
                j += 1
            else:
                ans.append(lst1[i])
                ans.append(lst2[j])
                i += 1
                j += 1
        return ans

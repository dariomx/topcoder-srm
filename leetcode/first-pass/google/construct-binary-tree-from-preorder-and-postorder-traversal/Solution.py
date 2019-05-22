class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        post = {x:i for (i,x) in enumerate(post)}
        # (i,j) and (k,l) are current portions of pre and post
        def build(i, j, k, l):
            if i > j:
                return None
            elif i == j:
                return TreeNode(pre[i])
            else:
                root = TreeNode(pre[i])
                left_val = pre[i+1]
                left_len = post[left_val] - k + 1
                root.left = build(i+1, i+left_len, k, k+left_len-1)
                root.right = build(i+left_len+1, j, k+left_len, l-1)
                return root
        n = len(pre)
        return build(0, n-1, 0, n-1)
class Solution:
    def findSecondMinimumValue(self, root):
        def snd(node, fst):
            if node is None:
                return -1
            else:
                if node.val == fst:
                    l_snd = snd(node.left, fst)
                    r_snd = snd(node.right, fst)
                    if l_snd < 0:
                        return r_snd
                    elif r_snd < 0:
                        return l_snd
                    else:
                        return min(l_snd, r_snd)
                else:
                    return node.val

        if root is None:
            return -1
        else:
            return snd(root, root.val)

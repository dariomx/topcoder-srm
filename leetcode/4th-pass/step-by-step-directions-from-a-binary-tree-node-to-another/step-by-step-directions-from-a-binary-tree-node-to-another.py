# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergePaths(self, parent: Dict[TreeNode, Tuple[TreeNode, str]], 
                         start: int, dest: int) -> str:
        path_left = []
        while start:
            path_left.append((start, 'U'))                        
            start = parent[start][0]
            
        path_right = []   
        while dest:
            path_right.append((dest, parent[dest][1]))
            dest = parent[dest][0]
                       
        while path_left and path_right and path_left[-1][0] == path_right[-1][0]:
            path_left.pop()
            path_right.pop()

        path = "".join((d for _,d in path_left))
        path += "".join((d for _,d in path_right[::-1]))
        return path
    
    def getDirections(self, root: Optional[TreeNode], start: int, dest: int) -> str:
        queue = deque([root])
        parent = {root.val: (None, '')}
        while queue and (start not in parent or dest not in parent):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                parent[node.left.val] = (node.val, 'L')
            if node.right:
                queue.append(node.right)
                parent[node.right.val] = (node.val, 'R')
        return self.mergePaths(parent, start, dest)        
            
        

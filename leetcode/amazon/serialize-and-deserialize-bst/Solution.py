"""
Linear Python solution with sparse heap array representation

We use the canonical index trick for heaps, which map the left and right
children to indexes 2*i and 2*i+1, respectively (we shift one place to the
right, in order to start indexing at 0).

Since the heap representation is good for full-trees, we would need
exponential space to fulfill it; assuming that we can potentially find thin
trees, we opt to use an sparse representation for the array. We serialize the
list of (index,value) pairs. Actually, the array is represented in memory as
a dictionary.

Space complexity is O(n), due both the array representation and the
auxiliary stack we use DFS traversal. Time should be O(n) as well due DFS.
"""

class Codec:
    def serialize(self, root):
        arr = dict()
        if not root:
            return ""
        stack = [(root, 0)]
        while stack:
            node, i = stack.pop()
            arr[i] = node.val
            for child, j in ((node.left, 2 * i + 1), (node.right, 2 * i + 2)):
                if child:
                    arr[j] = child.val
                    stack.append((child, j))
        ser = ""
        for i, v in arr.iteritems():
            ser += ("," if i > 0 else "") + str(i) + ":" + str(v)
        return ser

    def deserialize(self, data):
        if not data:
            return None
        parse_pair = lambda p: tuple(map(int, p.split(":")))
        arr = dict([parse_pair(p) for p in data.split(",")])
        root = TreeNode(arr[0])
        stack = [(root, 0)]
        def getpush_child(j):
            child = None
            if j in arr:
                child = TreeNode(arr[j])
                stack.append((child, j))
            return child
        while stack:
            node, i = stack.pop()
            node.left = getpush_child(2 * i + 1)
            node.right = getpush_child(2 * i + 2)
        return root


class SparseVector:
    def __init__(self, nums: List[int]):
        self.val = {i: x for i, x in enumerate(nums) if x != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(x * vec.val.get(i, 0) for i, x in self.val.items())

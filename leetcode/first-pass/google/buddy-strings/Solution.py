class Solution:
    def buddyStrings(self, A, B):
        if len(A) == len(B):
            pair = None
            swaps = False
            uniq = set()
            for a, b in zip(A, B):
                if a == b:
                    uniq.add(a)
                elif pair is None:
                    pair = a, b
                elif swaps:
                    return False
                else:
                    x, y = pair
                    if x == b and a == y:
                        swaps = True
                    else:
                        return False
            return swaps or len(uniq) < len(A)
        else:
            return False

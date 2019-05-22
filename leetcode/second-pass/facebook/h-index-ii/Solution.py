class Solution:
    def hIndex(self, citations):
        h = 0
        while citations:
            if citations.pop() < h + 1:
                break
            else:
                h += 1
        return h


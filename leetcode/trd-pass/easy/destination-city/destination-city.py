class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out = set()
        cities = set()
        for u, v in paths:
            out.add(u)
            cities.add(v)
        return (cities - out).pop()

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)

        def get_key(s):
            return ''.join(sorted(s))

        for s in strs:
            grp[get_key(s)].append(s)
        return grp.values()

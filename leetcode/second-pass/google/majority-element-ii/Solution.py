class Solution:
    def keep_dict_k(self, d, k):
        if len(d) < k:
            return
        min_val = min(d.values())
        for k in d:
            if d[k] == min_val:
                min_key = k
                break
        del d[min_key]

    def majorityElement(self, nums: List[int]) -> List[int]:
        k = 3  # should we always keep k cand? not sure
        cnt = dict()
        for x in nums:
            if x in cnt:
                cnt[x] += 1
            else:
                self.keep_dict_k(cnt, k)
                cnt[x] = 1
        cand = {x: 0 for x in cnt}
        for x in nums:
            if x in cand:
                cand[x] += 1
        return [x for x in cand if cand[x] > len(nums) // k]

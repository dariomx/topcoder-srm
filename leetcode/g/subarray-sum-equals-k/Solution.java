import java.util.*;

class Solution {
    private class Tuple {
        int fst, snd;

        public Tuple(int fst, int snd) {
            this.fst = fst;
            this.snd = snd;
        }

        public boolean equals(Object obj) {
            if (obj == null || !(obj instanceof Tuple))
                return false;
            Tuple other = (Tuple) obj;
            return this.fst == other.fst && this.snd == other.snd;
        }

        public int hashCode() {
            return 31*this.fst + this.snd;
        }
    }

    private int rec(int[] nums, int n, int i, int k,
                   Map<Tuple, Integer> cache) {
        Tuple key = new Tuple(i, k);
        if (cache.containsKey(key))
            return cache.get(key);
        int ret;
        if (i >= n)
            ret = 0;
        else {
            ret = nums[i] == k? 1 : 0;
            ret += rec(nums, n, i+1, k-nums[i], cache);
        }
        cache.put(key, ret);
        return ret;
    }

    public int subarraySum(int[] nums, int t) {
        int n = nums.length;
        if (n == 0)
            return 0;
        Map<Tuple, Integer> cache = new HashMap<>();
        int ans = 0;
        for(int i=0; i<n; i++)
            ans += rec(nums, n, i, t, cache);
        return ans;
    }
}
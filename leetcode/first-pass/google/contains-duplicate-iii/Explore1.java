import static java.lang.Math.*;

class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        int n = nums.length;
        for(int i=0; i<n; i++) {
            for(int j=max(0, i-k); j<min(n-1, i+k); j++) {
                if (j == i) {
                    continue;
                }
                long dist = (long) nums[i] - (long) nums[j];
                if (abs(dist) <= t && abs(i - j) <= k) {
                    return true;
                }
            }
        }
        return false;
    }
}
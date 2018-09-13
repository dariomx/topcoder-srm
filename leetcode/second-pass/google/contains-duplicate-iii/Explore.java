class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeMap<Long, Integer> last = new TreeMap<>();
        for(int i=0; i<nums.length; i++) {
            long x = nums[i];
            Set<Long> cand =
                new HashSet<>(last.headMap(t + x, true).keySet());
            cand.retainAll(last.tailMap(x - t, true).keySet());
            for(Long y: cand) {
                if (i - last.get(y) <= k) {
                    return true;
                }
            }
            last.put(x, i);
        }
        return false;
    }
}
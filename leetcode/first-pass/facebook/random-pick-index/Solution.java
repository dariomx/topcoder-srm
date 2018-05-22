import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

class Solution {

    private int[] nums;
    private int maxCacheSize;
    private Map<Integer, List<Integer>> cache;
    private Map<Integer, Integer> cacheCnt;
    private SortedMap<Integer, Set<Integer>> sortedCnt;
    private Random random;

    public Solution(int[] nums) {
        this.nums = nums;
        maxCacheSize = (int) Math.ceil(nums.length * 0.1);
        cache = new HashMap<>();
        cacheCnt = new HashMap<>();
        sortedCnt = new TreeMap<>();
        random = new Random();
    }

    private void ensureCacheSpace() {
        if (cache.size() == maxCacheSize) {
            int leastUsedCnt = sortedCnt.firstKey();
            Set<Integer> vals = sortedCnt.get(leastUsedCnt);
            Iterator<Integer> it = vals.iterator();
            int leastUsed = it.next();
            it.remove();
            cache.remove(leastUsed);
            cacheCnt.remove(leastUsed);
            if (vals.isEmpty()) {
                sortedCnt.remove(leastUsedCnt);
            }
        }
    }

    private List<Integer> computeIndexes(int target) {
        List<Integer> idx = new ArrayList<>();
        for(int i=0; i<nums.length; i++) {
            if (nums[i] == target) {
                idx.add(i);
            }
        }
        return idx;
    }

    public int pick(int target) {
        List<Integer> idx;
        int cnt;
        if (cache.containsKey(target)) {
            idx = cache.get(target);
            cnt = cacheCnt.get(target);
            sortedCnt.get(cnt).remove(target);
        } else {
            ensureCacheSpace();
            idx = computeIndexes(target);
            cache.put(target, idx);
            cnt = 0;
        }
        cacheCnt.put(target, cnt+1);
        sortedCnt.computeIfAbsent(cnt+1, c -> new HashSet<>()).add(target);
        int i = ThreadLocalRandom.current().nextInt(0, idx.size());
        return idx.get(i);
    }
}


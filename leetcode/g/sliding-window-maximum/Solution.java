import java.util.*;

public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> maxs = new ArrayList<>();
        Queue<Integer> window = new LinkedList<>();
        SortedMap<Integer, Integer> values = new TreeMap<>();
        for(int i=0; i<nums.length; i++) {
            int x = nums[i];
            if ( !values.containsKey(x) ) {
                values.put(x, 0);
            }
            values.put(x, values.get(x) + 1);
            window.add(x);
            if (window.size() > k) {
                int y = window.remove();
                values.put(y, values.get(y) - 1);
                if (values.get(y) == 0) {
                    values.remove(y);
                }
            }
            if (window.size() == k) {
                maxs.add(values.lastKey());
            }
        }
        return maxs.stream().mapToInt(i -> i).toArray();
    }
}
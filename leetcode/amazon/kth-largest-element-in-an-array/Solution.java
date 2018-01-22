/*
Java solution with O(n + k*log(n)) complexity

Could not use Python due the lack of oob max-heap, enter Java.

Idea is to put everything into a max-heap (which is O(n)), and then just
pull the k-1 largest elements first, in order to return the k-th we need.
Pulling takes O(log(n)), hence the total complexity of O(n + k*log(n)). I
think that such can be simplified to just O(n) if n >> k.
*/

import java.util.*;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap =
            new PriorityQueue<>(nums.length, Collections.reverseOrder());
        for(Integer x: nums) {
            minHeap.add(x);
        }
        for(int i=0; i<k-1; i++) {
            minHeap.poll();
        }
        return minHeap.poll();
    }
}
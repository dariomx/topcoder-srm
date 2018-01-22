/*
Java solution with O(n) space and O(n*log(n)) time

Not the linear time you would expect, but hey, I created it myself ;-?

We put into a max-heap all prices, and then do a second pass over them. For
each price we remove it from the max-heap, and peek the maximum value. The
difference between them gives the profit (could be negative), and then we just
reduce along the iteration to compute the maximum of them.
*/

import java.util.*;

class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0)
            return 0;
        PriorityQueue<Integer> maxHeap =
            new PriorityQueue<>(prices.length, Collections.reverseOrder());
        for(Integer x: prices)
            maxHeap.add(x);
        int profit = 0;
        for(Integer x: prices) {
            maxHeap.remove(x);
            if (maxHeap.isEmpty())
                break;
            profit = Math.max(profit, maxHeap.peek() - x);
        }
        return profit;
    }
}
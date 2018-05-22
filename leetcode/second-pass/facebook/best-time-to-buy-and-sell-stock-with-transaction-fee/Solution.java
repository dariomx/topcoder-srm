                 import java.util.*;

class Solution {
    public int maxProfit(int[] prices, int fee) {
        int n = prices.length;
        int[] profit = new int[n+1];
        NavigableMap<Integer, Integer> posPrices = new TreeMap<>();
        posPrices.put(prices[n-1], n-1);
        for(int i=n-2; i>=0; i--) {
            profit[i] = profit[i+1];
            SortedMap<Integer, Integer> biggerPrices =
                posPrices.tailMap(prices[i], false);
            for(Integer p: biggerPrices.keySet()) {
                int restProfit = profit[biggerPrices.get(p)+1];
                profit[i] = Math.max(profit[i],
                                     (p - prices[i] - fee) + restProfit);
            }
            posPrices.put(prices[i], i);
        }
        return profit[0];
    }
}
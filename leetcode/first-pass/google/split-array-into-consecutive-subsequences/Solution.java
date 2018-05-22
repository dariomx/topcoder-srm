/*
  The idea is to keep track of the sequences built so far, by remembering
  the endings; the structure can be a map which uses these ending points
  as keys so we allow for fast retrieval.

  When processing a particular element x, we can simply lookup if there are
  sequences ending with x-1; so we know we can append it. If there are not,
  we can start a new sequence that starts and ends with x.

  The internal struggle I had was about the values to associate to those
  keys, that is: should I just keep track of how many sequences ended in
  that way, or, I should keep something more concrete. Because when I find
  that there are sequences I can append to, do I care which one is chosen
  or not?

  Somehow I thought that smaller sequences should be preferred. Hence, used
  as value in map, a min-heap with current sizes of sequences sharing same
  ending. This allowed me to pick the smallest sequence in O(log(k)), where
  k was the number of sequences sharing same ending.

  Later on I realized that with some additional tricks, it was enough to
  remember how many sequences we had per ending (but this required an
  additional structure to keep track of the remaining occurrences per number).
  This should reduce the complexity from O(n*log(n)) to O(n); no wonder why
  I ended up in lowest quartile ;-?
*/

import java.util.*;

class Solution {
    public boolean isPossible(int[] nums) {
        Map<Integer, PriorityQueue<Integer>> endSizes = new HashMap<>();
        PriorityQueue<Integer> sizes = new PriorityQueue<>();
        sizes.add(1);
        endSizes.put(nums[0], sizes);
        for(int i=1; i<nums.length; i++) {
            int x = nums[i];
            int oldSize = 0;
            sizes = endSizes.get(x - 1);
            if ( sizes != null ) {
                oldSize = sizes.poll();
                if ( sizes.size() == 0 )
                    endSizes.remove(x - 1);
            }
            sizes = endSizes.get(x);
            if ( sizes == null ) {
                sizes = new PriorityQueue<>();
                endSizes.put(x, sizes);
            }
            sizes.add(oldSize + 1);
        }
        for(PriorityQueue<Integer> ss: endSizes.values())
            for(Integer size: ss)
                if (size < 3)
                    return false;
        return true;
    }
}
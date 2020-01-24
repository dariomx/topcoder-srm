import java.util.*;

class Solution {
    public int oddEvenJumps(int[] A) {
        int n = A.length;
        boolean[] odd = new boolean[n];
        boolean[] even = new boolean[n];
        odd[n-1] = even[n-1] = true;
        int ans = 1;
        NavigableSet<Integer> ahead = new TreeSet<>();
        ahead.add(A[n-1]);
        Map<Integer, Integer> lastIx = new HashMap<>();
        lastIx.put(A[n-1], n-1);
        for(int i=n-2; i>=0; i--) {
            int x = A[i];
            NavigableSet<Integer> leAhead = ahead.tailSet(x, true);
            if (!leAhead.isEmpty()) {
                int nextIx = lastIx.get(leAhead.first());
                if (even[nextIx]) {
                    odd[i] = true;
                    ans++;
                    //System.out.format("ans: %d, %d\n", i, x);
                }
            }
            NavigableSet<Integer> geAhead = ahead.headSet(x, true);
            if (!geAhead.isEmpty()) {
                int nextIx = lastIx.get(geAhead.last());
                if (odd[nextIx]) {
                    even[i] = true;
                }
            }
            ahead.add(x);
            lastIx.put(x, i);
        }
        return ans;
    }
}
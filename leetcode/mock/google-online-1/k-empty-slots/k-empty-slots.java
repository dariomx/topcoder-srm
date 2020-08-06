import java.util.TreeSet;

class Solution {
    private boolean hasKBetween(TreeSet<Integer> used, int x, int y) {
        if (used.contains(y)) {
            int min = Integer.min(x, y);
            int max = Integer.max(x, y);
            return used.higher(min) == max && used.lower(max) == min;
        } else {
            return false;
        }
    }

    public int kEmptySlots(int[] bulbs, int K) {
        TreeSet<Integer> used = new TreeSet<>();
        for(int i=0; i<bulbs.length; i++) {
            int x = bulbs[i];
            used.add(x);
            if (hasKBetween(used, x, x - (K + 1)) || hasKBetween(used, x, x + (K + 1))) {
                return i + 1;
            }
        }
        return -1;
    }
}
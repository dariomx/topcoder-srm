/*
Java O(log(n)) solution.

We keep the starting points in a sorted map, and associate as value the
corresponding ending point. When getting a new range, we search the starting
points on the left and right; and for each case check whether we have an
overlapping.

There are a couple of special cases: where we have no one on the left, and when
we have no one on the right. In such cases, we still need to validate there is
no overlapping using respectively the first and last entries.
*/

import java.util.*;

class MyCalendar {

    private TreeMap<Integer, Integer> slots;

    public MyCalendar() {
        slots = new TreeMap<>();
    }

    public boolean book(int start, int end) {
        Map.Entry<Integer, Integer> left = slots.floorEntry(start);
        if (left == null) {
            left = slots.firstEntry();
            if ( left != null && end > left.getKey() ) {
                return false;
            }
        } else if (left != null && start < left.getValue()) {
            return false;
        }
        Map.Entry<Integer, Integer> right = slots.ceilingEntry(start);
        if(right == null) {
            right = slots.lastEntry();
            if ( right != null && start < right.getValue()) {
                return false;
            }
        } else if(right != null && end > right.getKey()) {
            return false;
        }
        slots.put(start, end);
        return true;
    }
}

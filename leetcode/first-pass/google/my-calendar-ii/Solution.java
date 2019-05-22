import java.util.*;
import static java.lang.Math.min;
import static java.lang.Math.max;

class MyCalendarTwo {
    private NavigableMap<Integer, Integer> events;
    private Map<Integer, Integer> numOverlaps;

    public MyCalendarTwo() {
        events = new TreeMap<>();
        numOverlaps = new HashMap<>();
    }

    // an overlapping event is defined as one with a non empty intersection
    private boolean isOverlap(int start, int end,
                              Map.Entry<Integer, Integer> evt) {
        int iStart = max(start, evt.getKey());
        int iEnd = min(end, evt.getValue());
        return iStart < iEnd;
    }

    private void add(Map.Entry<Integer, Integer> evt,
                     boolean right,
                     Deque<int[]> overs) {
        int[] evtArr = new int[]{evt.getKey(), evt.getValue()};
        if (right) {
            overs.addLast(evtArr);
        } else {
            overs.addFirst(evtArr);
        }
    }

    // overlapping events on the right and left (null means we got triple booking)
    private Deque<int[]> getOverlaps(int start, int end) {
        Deque<int[]> overs = new ArrayDeque<>();
        NavigableMap<Integer, Integer> candMap = events.tailMap(start, true);
        overs = addLeftCand(start, end, candMap, overs);
        if (overs == null) {
            return null;
        }
        for(Map.Entry<Integer, Integer> evt: candMap.entrySet()) {
            if (!isOverlap(start, end, evt)) {
                break;
            }
            if (numOverlaps.get(evt.getKey()) > 1) {
                return null;
            } else {
                add(evt, true, overs);
            }
        }
        return overs;
    }

    // special case: there is overlapping event on the left
    private Deque<int[]> addLeftCand(int start, int end,
                                     NavigableMap<Integer, Integer> candMap,
                                     Deque<int[]> overs) {
        Map.Entry<Integer, Integer> leftEvt = null;
        if (candMap == null || candMap.isEmpty()) {
            leftEvt = events.floorEntry(start);
        } else {
            leftEvt = events.lowerEntry(candMap.firstKey());
        }
        if (leftEvt != null) {
            if (isOverlap(start, end, leftEvt)) {
                if (numOverlaps.get(leftEvt.getKey()) > 1) {
                    return null;
                }
                add(leftEvt, false, overs);
            }
        }
        return overs;
    }

    private void add(int start, int end, int numOver) {
        if (start < end) {
            events.put(start, end);
            numOverlaps.put(start, numOver);
        }
    }

    public boolean book(int start, int end) {
        Deque<int[]> overs = getOverlaps(start, end);
        if (overs == null) {
            return false;
        }
        while (!overs.isEmpty()) {
            int[] evt = overs.pollFirst();
            int evtStart = evt[0];
            int evtEnd = evt[1];
            int iStart = max(start, evtStart);
            int iEnd = min(end, evtEnd);
            events.remove(evtStart);
            numOverlaps.remove(evtStart);
            add(min(start, evtStart), iStart, 1);
            add(iStart, iEnd, 2);
            start = iEnd;
            end = max(end, evtEnd);
        }
        add(start, end, 1);
        return true;
    }
}

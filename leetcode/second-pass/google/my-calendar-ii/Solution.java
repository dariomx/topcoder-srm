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

    private boolean isOverlap(int start, int end,
                              Map.Entry<Integer, Integer> evt) {
        int oStart = max(start, evt.getKey());
        int oEnd = min(end, evt.getValue());
        return oStart < oEnd;
    }

    private void add(Map.Entry<Integer, Integer> evt,
                     boolean right,
                     Deque<int[]> cands) {
        int[] evtArr = new int[]{evt.getKey(), evt.getValue()};
        if (right) {
            cands.addLast(evtArr);
        } else {
            cands.addFirst(evtArr);
        }
    }

    // overlapping events on the right and left
    private Deque<int[]> getCandidates(int start, int end) {
        Deque<int[]> cands = new ArrayDeque<>();
        NavigableMap<Integer, Integer> candMap = events.tailMap(start, true);
        cands = addLeftCand(start, end, candMap, cands);
        if (cands == null) {
            return null;
        }
        for(Map.Entry<Integer, Integer> evt: candMap.entrySet()) {
            if (!isOverlap(start, end, evt)) {
                break;
            }
            if (numOverlaps.get(evt.getKey()) > 1) {
                return null;
            } else {
                add(evt, true, cands);
            }
        }
        return cands;
    }

    // special case: there is overlapping event on the left
    private Deque<int[]> addLeftCand(int start, int end,
                                     NavigableMap<Integer, Integer> candMap,
                                     Deque<int[]> cands) {
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
                add(leftEvt, false, cands);
            }
        }
        return cands;
    }

    private void add(int start, int end, int numOver) {
        if (start < end) {
            events.put(start, end);
            numOverlaps.put(start, numOver);
        }
    }

    public boolean book(int start, int end) {
        Deque<int[]> cands = getCandidates(start, end);
        if (cands == null) {
            return false;
        }
        while (!cands.isEmpty()) {
            int[] evt = cands.pollFirst();
            int evtStart = evt[0];
            int evtEnd = evt[1];
            int ovrStart = max(start, evtStart);
            int ovrEnd = min(end, evtEnd);
            events.remove(evtStart);
            numOverlaps.remove(evtStart);
            add(min(start, evtStart), ovrStart, 1);
            add(ovrStart, ovrEnd, 2);
            start = ovrEnd;
            end = max(end, evtEnd);
        }
        add(start, end, 1);
        return true;
    }
}

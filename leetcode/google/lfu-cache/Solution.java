/*
    Java solution with O(log(n)) operations.

    Not much mystery: simply use a sorted map of sorted sets. The first
    level gives least frequency, while the second gives least used. Rest
    of the information is stored in maps and used for comparisons.

    Will try to come up with an O(1) solution later.
 */
import java.util.*;

class LFUCache {
    private Map<Integer, Integer> cache;
    private Map<Integer, Integer> freq;
    private Map<Integer, Integer> last;
    private SortedMap<Integer, SortedSet<Integer>> order;
    private int time;
    private int capacity;
    private Comparator<Integer> lastCmp =
            (k1,k2) -> {
                int diff = last.get(k1) - last.get(k2);
                return diff == 0? k1 - k2 : diff;
            };

    public LFUCache(int capacity) {
        cache = new HashMap<>();
        freq = new HashMap<>();
        last = new HashMap<>();
        order = new TreeMap<>();
        time = 0;
        this.capacity = capacity;
    }

    public int get(int key) {
        time++;
        int val = cache.getOrDefault(key, -1);
        if ( val >= 0 ) {
            int f = freq.getOrDefault(key, 0);
            if ( f > 0 ) {
                SortedSet<Integer> sameFreq = order.get(f);
                sameFreq.remove(key);
                if (sameFreq.isEmpty())
                    order.remove(f);
            }
            f++;
            freq.put(key, f);
            last.put(key, time);
            if ( order.get(f) == null )
                order.put(f, new TreeSet(lastCmp));
            order.get(f).add(key);
        }
        return val;
    }

    public void put(int key, int value) {
        if( capacity == 0 )
            return;
        if (!cache.containsKey(key) && cache.size() == capacity) {
            int leastFreq = order.firstKey();
            SortedSet<Integer> leastFreqs = order.get(leastFreq);
            int leastUsed = leastFreqs.first();
            leastFreqs.remove(leastUsed);
            if ( leastFreqs.isEmpty() )
                order.remove(leastFreq);
            cache.remove(leastUsed);
            freq.remove(leastUsed);
            last.remove(leastUsed);
        }
        cache.put(key, value);
        get(key);
    }
}

public class Solution {
    public static void main1(String[] args) throws Exception {
        LFUCache lfu = new LFUCache(2);
        lfu.put(1, 1);
        lfu.put(2, 2);
        System.out.println(lfu.get(1));
        lfu.put(3, 3);
        System.out.println(lfu.get(2));
        System.out.println(lfu.get(3));
        lfu.put(4, 4);
        System.out.println(lfu.get(1));
        System.out.println(lfu.get(3));
        System.out.println(lfu.get(4));
    }

    public static void main(String[] args) throws Exception {
        LFUCache lfu = new LFUCache(0);
        lfu.put(0, 0);
        System.out.println(lfu.get(0));
    }
}


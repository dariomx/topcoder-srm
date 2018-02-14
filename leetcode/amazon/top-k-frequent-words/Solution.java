/*
Java solution using a min-heap + java8 streams

In theory building the min-heap is linear, and retrieving k times the smallest
element is O(k * log(n)).

In practice, the usage of streams seems quite slow.
*/

import java.util.*;
import java.util.stream.*;

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> cnt = new HashMap<>();
        Arrays.stream(words).
            forEach(w -> cnt.put(w, cnt.getOrDefault(w, 0) + 1));
        Comparator<String> revCmp = (w1, w2) -> {
            int diff = cnt.get(w2) - cnt.get(w1);
            return diff==0? w1.compareTo(w2): diff;
        };
        PriorityQueue<String> minHeap = new PriorityQueue<>(revCmp);
        cnt.keySet().stream().forEach(w -> minHeap.add(w));
        return IntStream.range(0, k).
                mapToObj(i -> minHeap.poll()).
                collect(Collectors.toList());
    }
}
class Key {
    int end, last, size;

    public Key(int end, int last, int size) {
        this.end = end;
        this.last = last;
        this.size = size;
    }

    @Override
    public boolean equals(Object obj) {
        Key other = (Key) obj;
        return  (end == other.end && last == other.last && size == this.size);
    }

    @Override
    public int hashCode() {
        int p = 31;
        return p*p*end + p*last + size;
    }
}

class Solution {
    private Map<Key, Integer> cache;

    private int rec(int end, int last, int size, int[] nums) {
        Key key = new Key(end, last, size);
        if (cache.containsKey(key)) {
            return cache.get(key);
        }
        int ret;
        if (end == nums.length) {
            ret = size;
        } else if (last < nums[end]) {
            ret = Math.max(rec(end+1, nums[end], size+1, nums),
                           rec(end+1, last, size, nums));
        } else {
            ret = Math.max(rec(end+1, nums[end], 1, nums),
                           rec(end+1, last, size, nums));
        }
        ret = Math.max(cache.getOrDefault(key, 0), ret);
        cache.put(key, ret);
        return cache.get(key);
    }

    public int lengthOfLIS(int[] nums) {
        if (nums.length <= 1) {
            return nums.length;
        }
        cache = new HashMap<>();
        return rec(0, nums[0], 1, nums);
    }
}
class KthLargest {

    private int k;
    private TreeMap<Integer, Integer> cnt;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        cnt = new TreeMap<>();
        for(int i=0; i<nums.length; i++) {
            cnt.put(nums[i], 1 + cnt.getOrDefault(nums[i], 0));
        }
    }

    public int add(int val) {
        cnt.put(val, 1 + cnt.getOrDefault(val, 0));
        int sum = 0;
        Map<Integer, Integer> desc = cnt.descendingMap();
        for(Map.Entry<Integer, Integer> entry: desc.entrySet()) {
            sum += entry.getValue();
            if (sum >= k) {
                return entry.getKey();
            }
        }
        return -1;
    }
}

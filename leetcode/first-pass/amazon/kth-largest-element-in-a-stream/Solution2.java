class KthLargest {

    private int k;
    private TreeSet<int[]> kNums;
    private int time;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        kNums = new TreeSet<>((t1, t2) ->
                              t1[0]==t2[0]? t1[1] - t2[1] :
                                            t1[0] - t2[0]);
        time = 0;
        for(int i=0; i<nums.length; i++) {
            add(nums[i]);
        }
    }

    public int add(int val) {
        kNums.add(new int[]{val, time++});
        if (kNums.size() > k) {
            kNums.pollFirst();
        }
        return kNums.first()[0];
    }
}

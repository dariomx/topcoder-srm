class Solution {
    private int[] arr = new int[3];
    private int base;

    private int calcKey(int base, int x, int y, int z) {
        arr[0] = x;
        arr[1] = y;
        arr[2] = z;
        Arrays.sort(arr);
        int key = 0;
        int powBase = 1;
        for(int i=0; i<2; i++) {
            key += powBase * arr[i];
            powBase *= base;
        }
        return key;
    }

    private Map<Integer, List<int[]>> getSum2SetBase(int[] nums) {
        int n = nums.length;
        Map<Integer, List<int[]>> sum2 = new HashMap<>();
        int minn = Integer.MAX_VALUE;
        int maxn = Integer.MIN_VALUE;
        for(int i=0; i<n; i++) {
            int y = nums[i];
            minn = Math.min(minn, y);
            maxn = Math.max(maxn, y);
            for(int j=i+1; j<n; j++) {
                int s = y + nums[j];
                List<int[]> pairs = sum2.getOrDefault(s, new ArrayList<>());
                pairs.add(new int[]{i, j});
                sum2.put(s, pairs);
            }
        }
        base = maxn - minn + 1;
        return sum2;
    }

    public List<List<Integer>> threeSum(int[] nums) {
        Map<Integer, List<int[]>> sum2 = getSum2SetBase(nums);
        List<List<Integer>> triples = new ArrayList<>();
        Set<Integer> used = new HashSet<>();
        for(int k=0; k<nums.length; k++) {
            int x = nums[k];
            if (sum2.containsKey(-x)) {
                for(int[] pair: sum2.get(-x)) {
                    int i = pair[0];
                    int j = pair[1];
                    if (k == i || k == j)
                        continue;
                    int y = nums[i];
                    int z = nums[j];
                    int key = calcKey(base, x, y, z);
                    if (!used.contains(key)) {
                        used.add(key);
                        triples.add(Arrays.asList(x, y, z));
                    }
                }
            }
        }
        return triples;
    }
}
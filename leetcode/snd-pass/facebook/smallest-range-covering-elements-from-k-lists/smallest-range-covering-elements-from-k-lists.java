class Solution {
    private int k;
    private List<int[]> xis;
    private int[] ans;

    private boolean isSmallerRange(int a, int b, int c, int d) {
        return b - a < d - c || (a < c && b - a == d - c);
    }

    private void checkAns(int start, int end, int usedSize) {
        int a = xis.get(start)[0];
        int b = xis.get(end)[0];
        if (usedSize == k &&
            (ans == null || isSmallerRange(a, b, ans[0], ans[1]))) {
            if (ans == null) {
                ans = new int[2];
            }
            ans[0] = a;
            ans[1] = b;
        }
    }

    private List<int[]> createXis(List<List<Integer>> nums) {
        xis = new ArrayList<>();
        for(int i=0; i<nums.size(); i++) {
            for(int x: nums.get(i)) {
                xis.add(new int[]{x, i});
            }
        }
        xis.sort((t1, t2) -> t1[0] - t2[0]);
        return xis;
    }

    private Map<Integer, List<Integer>> createMembership(List<int[]> xis) {
        Map<Integer, List<Integer>> mem = new HashMap<>();
        for(int[] xi: xis) {
            int x = xi[0];
            int i = xi[1];
            List<Integer> lst = mem.get(x);
            if (lst == null) {
                lst = new ArrayList<>();
                mem.put(x, lst);
            }
            lst.add(i);
        }
        return mem;
    }

    public int[] smallestRange(List<List<Integer>> nums) {
        k = nums.size();
        xis = createXis(nums);
        Map<Integer, List<Integer>> mem = createMembership(xis);
        int[] used = new int[k];
        int usedSize = 0;
        int start = 0, end = -1;
        int total = 0;
        ans = null;

        for(int[] xi: xis) {
            int x = xi[0];
            int i = xi[1];
            for(int j: mem.get(x)) {
                used[j]++;
                if (used[j] == 1) {
                    usedSize++;
                }
                total++;
            }
            end++;
            checkAns(start, end, usedSize);
            while (usedSize == k && total > k) {
                for(int j: mem.get(xis.get(start)[0])) {
                    used[j]--;
                    if (used[j] == 0) {
                        usedSize--;
                    }
                    total--;
                }
                start++;
                checkAns(start, end, usedSize);
            }
        }
        return ans;
    }
}
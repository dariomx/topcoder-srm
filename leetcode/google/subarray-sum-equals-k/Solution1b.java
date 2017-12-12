class Solution {
    public int subarraySum(int[] nums, int k) {
        int n = nums.length;
        if (n == 0)
            return 0;
        int[] psum = new int[n];
        psum[0] = nums[0];
        for(int i=1; i<n; i++)
            psum[i] = psum[i-1] + nums[i];
        int cnt = 0;
        for(int i=0; i<n; i++)
            for(int j=i; j<n; j++)
                if (psum[j] - (i>0? psum[i-1] : 0) == k)
                    cnt += 1;
        return cnt;
    }
}
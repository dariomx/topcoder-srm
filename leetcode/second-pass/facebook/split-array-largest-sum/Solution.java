import static java.lang.Math.max;

class Solution {
    public int splitArray(int[] nums, int m) {
        int n = nums.length;
        if (n == 0)
            return 0;
        int[][] max_sum = new int[n][];
        int[][] left_sum = new int[n][];
        for(int i=0; i<n; i++) {
            max_sum[i] = new int[m+1];
            left_sum[i] = new int[m+1];
        }
        int[] cum_sum = new int[n];
        max_sum[n-1][1] = nums[n-1];
        left_sum[n-1][1] = nums[n-1];
        cum_sum[n-1] = nums[n-1];
        for(int i=n-2; i>=0; i--) {
            cum_sum[i] = cum_sum[i+1] + nums[i];
            max_sum[i][1] = cum_sum[i];
            left_sum[i][1] = cum_sum[i];
            for(int k=2; k<m+1; k++) {
                if (max_sum[i+1][k] > 0) {
                    left_sum[i][k] = left_sum[i+1][k] + nums[i];
                    max_sum[i][k] = max(max_sum[i+1][k], left_sum[i][k]);
                }
                for(int j=i+1; j<n; j++) {
                    if (max_sum[j][k-1] == 0)
                        continue;
                    int left = cum_sum[i] - cum_sum[j];
                    int s_max_sum = max(max_sum[j][k-1], left);
                    if (max_sum[i][k] == 0 || s_max_sum < max_sum[i][k]) {
                        left_sum[i][k] = left;
                        max_sum[i][k] = s_max_sum;
                    }
                }
            }
        }
        return max_sum[0][m];
    }
}
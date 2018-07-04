import static java.lang.Math.max;
import static java.lang.Math.min;
import static java.lang.Integer.MAX_VALUE;
import java.util.Arrays;

class Solution {
    public int splitArray(int[] nums, int m) {
        int n = nums.length;
        if (n == 0)
            return 0;
        int[][] max_sum = new int[n][];
        for(int i=0; i<n; i++) {
            max_sum[i] = new int[m+1];
            Arrays.fill(max_sum[i], MAX_VALUE);
        }
        int[] cum_sum = new int[n];
        max_sum[n-1][1] = nums[n-1];
        cum_sum[n-1] = nums[n-1];
        for(int i=n-2; i>=0; i--) {
            cum_sum[i] = cum_sum[i+1] + nums[i];
            max_sum[i][1] = cum_sum[i];
            for(int k=2; k<m+1; k++) {
                for(int j=i+1; j<n; j++) {
                    max_sum[i][k] =
                        min(max_sum[i][k],
                            max(max_sum[j][k-1], cum_sum[i] - cum_sum[j]));
                }
            }
        }
        return max_sum[0][m];
    }
}
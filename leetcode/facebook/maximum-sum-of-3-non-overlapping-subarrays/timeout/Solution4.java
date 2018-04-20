import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.function.BiFunction;

public class Solution {
    private static final Integer NONE = -1;

    private int[] calcPrefixSum(int[] nums) {
        int n = nums.length;
        int[] pfxSum = new int[n];
        pfxSum[0] = nums[0];
        for (int i = 1; i < n; i++) {
            pfxSum[i] = pfxSum[i - 1] + nums[i];
        }
        return pfxSum;
    }

    private int[] findMax(int n,
                          int k,
                          Map<Tuple<Integer, Integer>, Tuple<Integer, int[]>> rec) {
        int maxSum = 0;
        int[] maxIdx = null;
        Tuple<Integer, Integer> key = new Tuple<>(0, 0);
        for(int i=0; i<n-3*k; i++) {
            key.x = i;
            key.y = 3;
            Tuple<Integer, int[]> val = rec.get(key);
            int sum = val.x;
            int[] idx = val.y;
            if (sum > maxSum) {
                maxSum = sum;
                maxIdx = idx;
            }
        }
        return maxIdx;
    }

    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length;
        int[] pfxSum = calcPrefixSum(nums);
        BiFunction<Integer, Integer, Integer> subSum =
                (i, j) -> pfxSum[j] - pfxSum[i] + nums[i];
        Map<Tuple<Integer, Integer>, Tuple<Integer, int[]>> rec = new HashMap<>();
        for(int i=0; i<n; i++) {
            rec.put(new Tuple(i, 0), new Tuple(0, new int[]{}));
        }
        for(int p=0; p<4; p++) {
            rec.put(new Tuple(n, p), new Tuple(0, new int[]{}));
        }
        Tuple<Integer, Integer> key = new Tuple<>(0, 0);
        for(int p=1; p<4; p++) {
            for(int i=0; i<n; i++) {
                if (n - i < p * k) {
                    rec.put(new Tuple(i, p), new Tuple(NONE, new int[]{}));
                    break;
                }
                int sum = 0;
                int[] idx = new int[]{};
                for(int j=i; j<n-k+1; j++) {
                    key.x = j + k;
                    key.y = p - 1;
                    Tuple<Integer, int[]> val = rec.get(key);
                    int sum_j = val.x;
                    int[] idx_j = val.y;
                    if (sum_j == NONE) {
                        break;
                    }
                    sum_j += subSum.apply(j, j + k - 1);
                    if (sum_j > sum) {
                        sum = sum_j;
                        idx = new int[1+idx_j.length];
                        idx[0] = j;
                        System.arraycopy(idx_j, 0, idx, 1, idx_j.length);
                    }
                }
                if (sum == 0) {
                    sum = NONE;
                }
                rec.put(new Tuple(i, p), new Tuple(sum, idx));
            }
        }
        return findMax(n, k, rec);
    }

    // stolen from stackoverflow, im lazy
    public class Tuple<X, Y> {
        public X x;
        public Y y;

        public Tuple(X x, Y y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "(" + x + "," + y + ")";
        }

        @Override
        public boolean equals(Object other) {
            if (other == this) {
                return true;
            }
            if (!(other instanceof Tuple)){
                return false;
            }
            Tuple<X,Y> other_ = (Tuple<X,Y>) other;
            // this may cause NPE if nulls are valid values for x or y. The logic may be improved to handle nulls properly, if needed.
            return other_.x.equals(this.x) && other_.y.equals(this.y);
        }

        @Override
        public int hashCode() {
            final int prime = 31;
            int result = 1;
            result = prime * result + ((x == null) ? 0 : x.hashCode());
            result = prime * result + ((y == null) ? 0 : y.hashCode());
            return result;
        }
    }

}


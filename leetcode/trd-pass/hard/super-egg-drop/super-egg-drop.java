// the binary search is not entirely correct; hence this
// can be further optimized to be O(K*N*log(N))


import static java.lang.Integer.MAX_VALUE;
import static java.lang.Math.min;
import static java.lang.Math.max;

class Solution {
    private int[][] cache;

    private void initCache(int K, int N) {
        cache = new int[K+1][N+1];
        for(int i=0; i<cache.length; i++) {
            Arrays.fill(cache[i], MAX_VALUE);
        }
    }

    private int binSearch(int K, int N, int startCost) {
        int ret = startCost;
        int start = 1, end = N;
        while (start < end) {
            int mid = (start + end) / 2;
            int cost = 1 + max(solve(K-1, mid-1), solve(K, N-mid));
            if (cost < startCost) {
                ret = cost;
                break;
            } else {
                end = mid;
            }
        }
        return ret;
    }

    private int linSearch(int K, int N) {
        int ret = MAX_VALUE;
        for(int i=1; i<=N; i++) {
            int prev = ret;
            ret = min(ret, 1 + max(solve(K-1, i-1), solve(K, N-i)));
            if (prev < MAX_VALUE && ret < prev) {
                break;
            }
        }
        return ret;
    }

    public int solve(int K, int N) {
        int ret = cache[K][N];
        if (ret < MAX_VALUE) {
            return ret;
        }
        if (K == 1 || N <= 1) {
            ret = max(1, N);
        } else {
            int startCost = 1 + max(solve(K-1, 0), solve(K, N-1));
            ret = binSearch(K, N, startCost);
            if (ret >= startCost) {
                ret = linSearch(K, N);
            }
        }
        cache[K][N] = ret;
        return ret;
    }

    public int superEggDrop(int K, int N) {
        initCache(K, N);
        return solve(K, N);
    }
}
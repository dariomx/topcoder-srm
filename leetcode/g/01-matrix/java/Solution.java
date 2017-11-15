import java.util.*;

class Solution {
    private static class Tuple {
        int fst;
        int snd;
        int dist;
        public Tuple(int fst, int snd, int dist) {
            this.fst = fst;
            this.snd = snd;
            this.dist = dist;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj instanceof Tuple) {
                Tuple other = (Tuple) obj;
                return this.fst == other.fst && this.snd == other.snd;
            } else {
                return false;
            }
        }

        @Override
        public int hashCode() {
            int res = 17;
            res = res * 31 + Math.min(this.fst, this.snd);
            res = res * 31 + Math.max(this.fst, this.snd);
            return res;
        }
    }

    private Tuple[] childIdx = new Tuple[] {
        new Tuple(-1,0,0),
        new Tuple(+1,0,0),
        new Tuple(0,-1,0),
        new Tuple(0,+1,0)
    };

    private void bfs_search(int[][] matrix, Tuple start, int[][] min_dist) {
        int n = matrix.length;
        int m = matrix[0].length;
        Deque<Tuple> queue = new ArrayDeque<>();
        queue.add(start);
        Set<Tuple> visited = new HashSet<>();
        visited.add(start);
        while (!queue.isEmpty()) {
            Tuple tup = queue.remove();
            int x = tup.fst;
            int y = tup.snd;
            int dist = tup.dist;
            if (matrix[x][y] == 1) {
                min_dist[x][y] = Math.min(min_dist[x][y], dist);
            }
            for(Tuple idx: childIdx) {
                int i = x + idx.fst;
                int j = y + idx.snd;
                if (i >= 0 && i < n && j >= 0 && j < m) {
                    tup = new Tuple(i, j, dist + matrix[i][j]);
                    if (!visited.contains(tup)) {
                        visited.add(tup);
                        queue.add(tup);
                    }
                }
            }
        }
    }
    public int[][] updateMatrix(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        int[][] min_dist = new int[n][m];
        for(int x=0; x<n; x++)
            for(int y=0; y<m; y++)
                if (matrix[x][y] == 1)
                    min_dist[x][y] = Integer.MAX_VALUE;
        for(int x=0; x<n; x++)
            for(int y=0; y<m; y++)
                if (matrix[x][y] == 0)
                    bfs_search(matrix, new Tuple(x,y,0), min_dist);
        return min_dist;
    }
}
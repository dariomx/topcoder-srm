import java.util.*;

class Tuple {
    public int fst;
    public int snd;

    public Tuple(int fst, int snd) {
        this.fst = fst;
        this.snd = snd;
    }

    @Override
    public boolean equals(Object other) {
        Tuple tup = (Tuple) other;
        return fst == tup.fst && snd == tup.snd;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + fst;
        result = prime * result + snd;
        return result;
    }
}

public class Solution {
    private Tuple[] deltasNeighbors = new Tuple[] {
        new Tuple(-1,0),
        new Tuple(+1,0),
        new Tuple(0,-1),
        new Tuple(0,+1)
    };

    private int countValley(int level, Tuple start, int[][] heightMap, Set<Tuple> visited) {
        Deque<Tuple> stack = new ArrayDeque();
        stack.add(start);
        int cnt = 0;
        int height = 1;
        int m = heightMap.length;
        int n = heightMap[0].length;
        while (stack.size() > 0) {
            Tuple cell = stack.removeFirst();
            if (visited.contains(cell))
                continue;
            visited.add(cell);
            cnt += 1;
            int x = cell.fst;
            int y = cell.snd;
            if (x == 0 || x == (m-1) || y == 0 || y == (n-1))
                height = 0;
            for(Tuple tup: deltasNeighbors) {
                int i = x + tup.fst;
                int j = y + tup.snd;
                if (!(0 <= i && i < m) || !(0 <= j && j < n))
                    continue;
                if (heightMap[i][j] < level)
                    stack.addFirst(new Tuple(i, j));
            }

        }
        return cnt * height;
    }

    private int countLevel(int level, int[][] heightMap) {
        int cnt = 0;
        Set<Tuple> visited = new HashSet();
        int m = heightMap.length;
        int n = heightMap[0].length;
        for(int x=0; x<m; x++)
            for(int y=0; y<n; y++)
                if (heightMap[x][y] < level)
                    cnt += countValley(level, new Tuple(x,y), heightMap, visited);
        return cnt;
    }

    private List<Integer> sortHeights(int[][] heightMap) {
        Set<Integer> sh = new TreeSet();
        int m = heightMap.length;
        int n = heightMap[0].length;
        for(int x=0; x<m; x++)
            for(int y=0; y<n; y++)
                sh.add(heightMap[x][y]);
        return new ArrayList(sh);
    }

    public int trapRainWater(int[][] heightMap) {
        if (heightMap.length==0 || heightMap[0].length==0)
            return 0;
        int cnt = 0;
        List<Integer> sh = sortHeights(heightMap);
        for(int k=1; k<sh.size(); k++) {
            cnt += (sh.get(k) - sh.get(k-1)) * countLevel(sh.get(k), heightMap);
        }
        return cnt;
    }
}
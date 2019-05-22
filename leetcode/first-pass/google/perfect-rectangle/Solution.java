class Solution {
    static int k = 2;
    static double eps = 0.001f;

    KDTree buildTree(List<double[]> xs, int lev) {
        int n = xs.size();
        if (n == 0) {
            return null;
        }
        int i = lev % k;
        int med = median(xs, i);
        return new KDTree(xs.get(med),
                          buildTree(xs.subList(0, med), lev+1),
                          buildTree(xs.subList(med+1, n), lev+1));
    }

    int median(List<double[]> xs, int i) {
        xs.sort((x, y) -> Double.compare(x[i], y[i]));
        int med = xs.size() / 2;
        while (med < xs.size()-1 &&
               xs.get(med)[i] == xs.get(med+1)[i]) {
            med++;
        }
        return med;
    }

    int rsearch(KDTree t, double[] low, double[] high, int lev) {
        if (t == null) {
            return 0;
        }
        int cnt = 0;
        int i = lev % k;
        if (t.key[i] >= low[i]) {
            cnt += rsearch(t.left, low, high, lev+1);
        }
        int j = 0;
        for(;j < k && low[j] <= t.key[j] && t.key[j] <= high[j]; j++);
        if (j == k) {
            cnt += 1;
        }
        if (t.key[i] < high[i]) {
            cnt += rsearch(t.right, low, high, lev+1);
        }
        return cnt;
    }

    boolean overlap(Set<Rectangle> rectangles,
                    List<double[]> points) {
        KDTree tree = buildTree(points, 0);
        for(Rectangle r: rectangles) {
            double[] low = {r.x1, r.y1};
            double[] high = {r.x2 - eps, r.y2 - eps};
            if (rsearch(tree, low, high, 0) != 4) {
                return true;
            }
        }
        return false;
    }

    public boolean isRectangleCover(int[][] rectangles) {
        int n = rectangles.length;
        List<double[]> points = new ArrayList<>();
        Set<Rectangle> seenR = new HashSet<>(n);
        Set<Point> seenP = new HashSet<>(n*4);
        Point start = new Point(Float.MAX_VALUE, Float.MAX_VALUE);
        Point end = new Point(0f, 0f);
        double area = 0;
        for(int i=0; i<n; i++) {
            Rectangle r = new Rectangle(rectangles[i][0],
                                        rectangles[i][1],
                                        rectangles[i][2],
                                        rectangles[i][3]);
            if (seenR.contains(r)) {
                return false;
            }
            seenR.add(r);
            area += r.area();
            double x1 = r.x1;
            double y1 = r.y1;
            double x2 = r.x2;
            double y2 = r.y2;
            Point myStart = new Point(x1, y1);
            if (myStart.compareTo(start) < 0) {
                start = myStart;
            }
            Point myEnd = new Point(x2, y2);
            if (myEnd.compareTo(end) > 0) {
                end = myEnd;
            }
            x2 -= eps;
            y2 -= eps;
            for(Point p: new Point[] {new Point(x1, y1),
                                      new Point(x2, y1),
                                      new Point(x1, y2),
                                      new Point(x2, y2)}) {
                if(!seenP.contains(p)) {
                    seenP.add(p);
                    points.add(p.toArray());
                }
            }
        }
        Rectangle total = new Rectangle(start, end);
        return (total.area() == area) && !overlap(seenR, points);
    }

    static class Point implements Comparable<Point> {
        double x, y;

        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj != null && obj instanceof Point) {
                Point p = (Point) obj;
                return x == p.x && y == p.y;
            } else {
                return false;
            }
        }

        @Override
        public int hashCode() {
            return (int) (31*x + y);
        }

        @Override
        public int compareTo(Point p) {
            int cmp = Double.compare(x, p.x);
            if (cmp == 0) {
                cmp = Double.compare(y, p.y);
            }
            return cmp;
        }

        double[] toArray() {
            return new double[]{x, y};
        }
    }

    static class Rectangle {
        double x1, y1, x2, y2;

        public Rectangle(Point start, Point end) {
            this(start.x, start.y, end.x, end.y);
        }

        public Rectangle(double x1, double y1, double x2, double y2) {
            this.x1 = x1;
            this.y1 = y1;
            this.x2 = x2;
            this.y2 = y2;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj != null && obj instanceof Rectangle) {
                Rectangle r = (Rectangle) obj;
                return x1 == r.x1 && y1 == r.y1 &&
                    x2 == r.x2 && y2 == r.y2;
            } else {
                return false;
            }
        }

        @Override
        public int hashCode() {
            double p = 31;
            double key = x1;
            key = key*p + y1;
            key = key*p + x2;
            key = key*p + y2;
            return (int) key;
        }

        double area() {
            return (x2 - x1) * (y2 - y1);
        }

        @Override
        public String toString() {
            return String.format("(%f, %f, %f, %f)", x1, y1, x2, y2);
        }
    }

    static class KDTree {
        double[] key;
        KDTree left, right;

        public KDTree(double[] key, KDTree left, KDTree right) {
            this.key = key;
            this.left = left;
            this.right = right;
        }
    }
}
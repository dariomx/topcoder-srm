class Solution {
    public int kEmptySlots(int[] flowers, int k) {
        TreeSet<Integer> slots = new TreeSet<>();
        int day = 0;
        for(Integer i: flowers) {
            day++;
            slots.add(i);
            Integer lower = slots.lower(i);
            if (lower != null && (i - lower - 1) == k) {
                return day;
            }
            Integer higher = slots.higher(i);
            if (higher != null && (higher - i - 1) == k) {
                return day;
            }
        }
        return -1;
    }
}
import java.util.Arrays;

class Solution {
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    private int floor(int[] nums, int i, int x) {
        int start = i;
        int end = nums.length - 1;
        int fidx = -1;
        int fval = 0;
        while (start <= end) {
            int middle = (start + end)/2;
            if ( nums[middle] > x ) {
                if ( fidx < 0 || nums[middle] < fval ) {
                    fidx = middle;
                    fval = nums[middle];
                }
                end = middle - 1;
            } else {
                start = middle + 1;
            }
        }
        return fidx;
    }

    private boolean next(int[] nums, int i) {
        boolean handled = false;
        int n = nums.length - i;
        if ( n == 2 ) {
            if (nums[i] < nums[i+1]) {
                swap(nums, i, i+1);
                handled = true;
            }
        } else if ( next(nums, i+1) ) {
            handled = true;
        } else {
            Arrays.sort(nums, i+1, nums.length);
            int j = floor(nums, i+1, nums[i]);
            if ( j >= 0 ) {
                swap(nums, i, j);
                Arrays.sort(nums, i+1, nums.length);
                handled = true;
            } else if ( i == 0 ) {
                Arrays.sort(nums, 0, nums.length);
                handled = true;
            }
        }
        return handled;
    }

    public void nextPermutation(int[] nums) {
        if (nums.length > 1) {
            next(nums, 0);
        }
    }
}
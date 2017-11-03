class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        if ( n == 0 ) {
            return nums;
        }
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        for(int i=0; i<n; i++) {
            for(int j=i+1; j<i+n; j++) {
                if (nums[j%n] > nums[i]) {
                    ans[i] = nums[j%n];
                    break;
                }
            }
        }
        return ans;
    }
}
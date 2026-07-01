class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int j = 1; j < nums.length; j++) {
            for (int i = 0; i < nums.length-j; i++) {
                if (nums[i]+nums[i+j] == target) return new int[] {i,i+j};
            }
        } return null;
    }
}
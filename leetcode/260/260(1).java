//ry

class Solution {
    public int[] singleNumber(int[] nums) {
        int[] res = new int[2];
        Arrays.sort(nums);
        int j = 0;
        int i = 0;
        while(i < nums.length - 1) {
            if(nums[i] == nums[i + 1]) i += 2;
            else res[j++] = nums[i++];
            if(j == 2) break;
        }
        if(j == 1) res[j] = nums[i];
        return res;
    }
}

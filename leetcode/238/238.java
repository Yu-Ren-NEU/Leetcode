//ry

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] L = new int[len];
        L[0] = 1;
        for(int i = 1; i < len; i++) {
            L[i] = L[i - 1] * nums[i - 1];
        }
        int R = 1;
        for(int i = len - 2; i >= 0; i--) {
            R *= nums[i + 1];
            L[i] *= R;
        }
        return L;
    }
}

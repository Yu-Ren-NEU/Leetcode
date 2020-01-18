//ry

class Solution {
    public int[] singleNumber(int[] nums) {
        int[] res = new int[2];
        int tmp = 0;
        for (int num : nums) {
            tmp ^= num; 
        }
        int flag = tmp & -tmp;
        for (int num : nums) {
            if ((num & flag) == 0) {
                res[0] ^= num;
            } else {
                res[1] ^= num;
            }
        }
        return res;
    }
}

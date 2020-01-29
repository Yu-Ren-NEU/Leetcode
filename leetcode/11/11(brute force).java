//ry

class Solution {
    public int maxArea(int[] height) {
        int max = 0;
        for(int i = 0; i < height.length; i++) {
            for(int j = i + 1; j < height.length; j++) {
                int water = (j - i) * (height[i] <= height[j] ? height[i] : height[j]);
                max = max >= water ? max : water;
            }
        }
        return max;
    }
}

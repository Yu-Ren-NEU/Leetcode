// Yu Ren
class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int[] remains = new int[60];
        for(int t : time) remains[t % 60]++;
        int res = 0;
        for(int i = 0; i < 31; i++) {
            if(i == 0 || i == 30) res += (remains[i] * (remains[i] - 1)) / 2;
            else res += remains[i] * remains[60 - i];
        }
        return res;
    }
}

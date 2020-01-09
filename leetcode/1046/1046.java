//ry

class Solution {
    public int lastStoneWeight(int[] stones) {
        if(stones.length == 0) return 0;
        if(stones.length == 1) return stones[0];
        Arrays.sort(stones);
        int i = stones.length - 1;
        while(i > 0) {
            if(stones[i] == stones[i - 1]) i -= 2;
            else if(stones[i] > stones[i - 1]) {
                int rem = stones[i] - stones[i - 1];
                i--;
                int j = i;
                for(; j > 0; j--) {
                    if(rem > stones[j - 1]) {
                        stones[j] = rem;
                        break;
                    }
                    stones[j] = stones[j - 1];
                }
                if(j == 0) stones[j] = rem;
            }
        }
        if(i == -1) return 0;
        return stones[0];
    }
}

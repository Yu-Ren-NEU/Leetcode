// ry

class KthLargest {

    PriorityQueue<Integer> pq;
    int max;
    
    public KthLargest(int k, int[] nums) {
        pq = new PriorityQueue<>(k);
        max = k;
        
        if(nums != null && nums.length > 0){
        int index = 0;
        while(index < k && index < nums.length){
            pq.add(nums[index]);
            index++;
        }
        
        while(index < nums.length) {
            if(nums[index] > pq.peek()){
                pq.poll();
                pq.add(nums[index]);
            }
            index++;
        }
        }
    }
    
    public int add(int val) {
        if(pq.size() < max){
            pq.add(val);
        } else
        if(val >= pq.peek()){
            pq.poll();
            pq.add(val);
        }
        return pq.peek();
    }
}


/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */

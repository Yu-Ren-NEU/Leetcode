//ry

//Priority Queue

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BSTIterator {
    PriorityQueue<Integer> pq;
    public BSTIterator(TreeNode root) {
        pq = new PriorityQueue<>();
        helper(root);
    }
    
    private void helper(TreeNode node) {
        if(node == null) return;
        pq.add(node.val);
        helper(node.left);
        helper(node.right);
    }
    
    /** @return the next smallest number */
    public int next() {
        return pq.poll();
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !pq.isEmpty();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */

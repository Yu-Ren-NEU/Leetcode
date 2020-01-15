//ry

//stack and pointer

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
    Stack<TreeNode> stack;
    TreeNode node;
    public BSTIterator(TreeNode root) {
        stack = new Stack<>();
        node = root;
    }
    
    /** @return the next smallest number */
    public int next() {
        while(node != null) {
            stack.push(node);
            node = node.left;
        }
        node = stack.pop();
        int res = node.val;
        node = node.right;
        return res;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty() || node != null;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */

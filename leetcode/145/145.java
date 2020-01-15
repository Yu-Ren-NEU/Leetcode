//ry

//Recursion

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    
    List<Integer> res = new ArrayList<>();
    
    public List<Integer> postorderTraversal(TreeNode root) {
        helper(root);
        return res;
    }
    
    private void helper(TreeNode node) {
        if(node == null) return;
        helper(node.left);
        helper(node.right);
        res.add(node.val);
    }
}

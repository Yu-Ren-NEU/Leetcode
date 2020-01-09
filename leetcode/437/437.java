//ry

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
    int res = 0;
    public int pathSum(TreeNode root, int sum) {
        search(root, sum);
        return res;
    }
    public void search(TreeNode node, int sum) {
        if(node == null) return;
        helper(node, sum);
        search(node.left, sum);
        search(node.right, sum);
    }
    public void helper(TreeNode node, int sum) {
        if(node == null) return;
        sum -= node.val;
        if(sum == 0) res++;
        helper(node.left, sum);
        helper(node.right, sum);
    }
}

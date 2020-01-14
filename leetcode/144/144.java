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
    public List<Integer> preorderTraversal(TreeNode root) {
        pdt(root);
        return res;
    }
    public void pdt(TreeNode node) {
        if(node == null) return;
        res.add(node.val);
        pdt(node.left);
        pdt(node.right);
    }
}

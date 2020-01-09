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
    List<String> result = new ArrayList<>();
    public List<String> binaryTreePaths(TreeNode root) {
        if(root == null) return result;
        helper(root, "");
        return result;
    }
    public void helper(TreeNode node, String path) {
        if(node.left != null) helper(node.left, path + node.val + "->");
        if(node.right != null) helper(node.right, path + node.val + "->");
        if(node.left == null && node.right == null) result.add(path + node.val);
    }
}

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
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return null;
        Queue<TreeNode> queue = new LinkedList<>();
        dfs(root, queue);
        while(!queue.isEmpty()) {
            TreeNode node = queue.poll();
            TreeNode tmp = node.left;
            node.left = node.right;
            node.right = tmp;
        }
        return root;
    }
    public void dfs(TreeNode node, Queue<TreeNode> queue) {
        if(node.left == null && node.right == null) return;
        queue.offer(node);
        if(node.left != null) dfs(node.left, queue);
        if(node.right != null) dfs(node.right, queue);
    }
}

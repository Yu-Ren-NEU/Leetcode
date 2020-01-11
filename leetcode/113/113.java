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
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if(root == null) return res;
        helper(root, sum, 0, new ArrayList<>());
        return res;
    }
    public void helper(TreeNode node, int target, int now, List<Integer> path) {
        now += node.val;
        if(node.left == null && node.right == null) {
            if(now == target) {
                path.add(node.val);
                res.add(new ArrayList<>(path));
                path.remove(path.size() - 1);
            }
            return;
        }
        path.add(node.val);
        if(node.left != null) helper(node.left, target, now, path);
        if(node.right != null) helper(node.right, target, now, path);
        path.remove(path.size() - 1);
    }
}

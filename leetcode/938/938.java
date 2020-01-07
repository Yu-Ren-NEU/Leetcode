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
    public int rangeSumBST(TreeNode root, int L, int R) {
        int result = 0;
        result = Search(root, L, R, result);
        return result;
    }
    public int Search(TreeNode node, int L, int R, int result) {
        if(node == null) return result;
        if(node.val < L) {
            result = Search(node.right, L, R, result);
            return result;
        }
        if(node.val > R) {
            result = Search(node.left, L, R, result);
            return result;
        }
        result += node.val;
        result = Search(node.left, L, R, result);
        result = Search(node.right, L, R, result);
        return result;
    }
}

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
    public int kthSmallest(TreeNode root, int k) {
        int i = 0;
        Stack<TreeNode> stack = new Stack<>();
        while(true){
            while(root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if(++i == k) return root.val;
            root = root.right;
        }
    }
}

//ry

//Iteration

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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        while (true) {
            while (root != null) {
                res.add(root.val);
                if(root.right != null) stack.push(root.right);
                root = root.left;
            }
            if(stack.isEmpty()) break;
            root = stack.pop();
        }
        return res;
    }
}

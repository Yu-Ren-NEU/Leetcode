//ry

class Solution {
    int max_sum = Integer.MIN_VALUE;
    int max_minus = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        int path = helper(root, 0);
        max_sum = Math.max(path, max_sum);
        if(max_sum == 0) return max_minus;
        return max_sum;
    }
    public int helper(TreeNode node, int path) {
        if(node == null) return path;
        path += node.val;
        max_minus = Math.max(max_minus, node.val);
        if(node.left == null && node.right == null) return path;
        int leftpath = Math.max(helper(node.left, 0), 0);
        int rightpath = Math.max(helper(node.right, 0), 0);
        int maxpath = Math.max(leftpath, rightpath);
        max_sum = Math.max(max_sum, Math.max(maxpath + node.val, Math.max(leftpath + rightpath + node.val, maxpath)));
        return maxpath + node.val;
    }
}

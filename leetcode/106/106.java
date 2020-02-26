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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int inlen = inorder.length;
        int postlen = postorder.length;
        return buildTree(inorder, 0, inlen - 1, postorder, postlen - 1, 0);
    }
    private TreeNode buildTree(int[] in, int instart, int inend, int post[], int poststart, int postend) {
        if(instart > inend || poststart < postend) return null;
        int rootval = post[poststart];
        int rootindex = 0;
        for(int i = instart; i <= inend; i++) {
            if(in[i] == rootval) {
                rootindex = i;
                break;
            }
        }
        int len = inend - rootindex;
        TreeNode root = new TreeNode(rootval);
        root.left = buildTree(in, instart, rootindex - 1, post, poststart - len - 1, postend);
        root.right = buildTree(in, rootindex + 1, inend, post, poststart - 1, poststart - len);
        return root;
    }
}

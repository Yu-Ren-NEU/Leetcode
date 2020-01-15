//ry

/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
    public Node connect(Node root) {
        Stack<Node> stack = new Stack<>();
        Stack<Node> stack_help = new Stack<>();
        stack.add(root);
        do {
            while(!stack_help.isEmpty()) {
                stack.push(stack_help.pop());
            }
            Node pre = null;
            Node nex = stack.pop();
            while(nex != null) {
                pre = nex;
                if(nex.left != null) stack_help.push(nex.left);
                if(nex.right != null) stack_help.push(nex.right);
                if(!stack.isEmpty()) nex = stack.pop();
                else nex = null;
                pre.next = nex;
            }
        } while(!stack_help.isEmpty());
        return root;
    }
}

//ry

class Solution {
    class Node {
        int l;
        int r;
        Node next;
        public Node(int l, int r, Node next) {
            this.l = l;
            this.r = r;
            this.next = next;
        }
    }
    public int[][] merge(int[][] intervals) {
        if(intervals.length == 0) return intervals;
        Node head = new Node(0, 0, null);
        for(int[] interval : intervals) {
            Node pre = head;
            Node node = head.next;
            while(node != null) {
                if(interval[1] < node.l) {
                    pre.next = new Node(interval[0], interval[1], node);
                    break;
                }
                else if(interval[0] > node.r) {
                    pre = node;
                    node = node.next;
                }
                else {
                    node.l = node.l < interval[0] ? node.l : interval[0];
                    node.r = node.r > interval[1] ? node.r : interval[1];
                    pre = node;
                    node = node.next;
                    while(node != null) {
                        if(pre.r < node.l) break;
                        if(pre.r > node.r) node = node.next;
                        else {
                            pre.r = node.r;
                            node = node.next;
                            break;
                        }
                    }
                    pre.next = node;
                    node = pre;
                    break;
                }
            }
            if(node == null) pre.next = new Node(interval[0], interval[1], null);
        }
        head = head.next;
        Node num = head;
        int n = 0;
        while(num != null) {
            n++;
            num = num.next;
        }
        num = head;
        int[][] res = new int[n][2];
        n = 0;
        while(num != null) {
            res[n][0] = num.l;
            res[n][1] = num.r;
            n++;
            num = num.next;
        }
        return res;
    }
}

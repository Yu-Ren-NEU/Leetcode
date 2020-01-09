//ry

class MyQueue {
    
    Stack<Integer> stack;
    Stack<Integer> stack_helper;
    
    /** Initialize your data structure here. */
    public MyQueue() {
        stack = new Stack<>();
        stack_helper = new Stack<>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        while(!stack.isEmpty()) {
            stack_helper.push(stack.pop());
        }
        stack_helper.push(x);
        while(!stack_helper.isEmpty()) {
            stack.push(stack_helper.pop());
        }
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if(stack.isEmpty()) return -1;
        return stack.pop();
    }
    
    /** Get the front element. */
    public int peek() {
        if(stack.isEmpty()) return -1;
        return stack.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */

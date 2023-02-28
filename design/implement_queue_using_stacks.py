class Stack:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        new_head = self.ListNode(val, self.head)
        self.head = new_head

    def pop(self) -> None:
        ret_val = self.head.val
        self.head = self.head.next
        return ret_val

    def top(self) -> int:
        return self.head.val

    def is_empty(self):
        return (self.head is None)


class MyQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()
        self.front = None

    def push(self, x: int) -> None:
        if self.first_stack.is_empty():
            self.front = x
        self.first_stack.push(x)

    def pop(self) -> int:
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                self.second_stack.push(self.first_stack.pop())
        return self.second_stack.pop()

    def peek(self) -> int:
        if self.second_stack.is_empty():
            return self.front
        else:
            return self.second_stack.top()

    def empty(self) -> bool:
        return self.first_stack.is_empty() and self.second_stack.is_empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

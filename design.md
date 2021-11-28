# Design

+ [Min Stack](#min-stack)

+ [Implement Stack using Queues](#implement-stack-using-queues)

## Min Stack

<https://leetcode.com/problems/min-stack/>

```python3
class LinkedListIterator:
    def __init__(self, head):
        self.cur_node = head

    def __next__(self):
        pr_node = self.cur_node
        if pr_node != None:
            self.cur_node = self.cur_node.next
            return pr_node.val
        else:
            raise StopIteration

    def __iter__(self):
        return self


class MinStack:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.min_val = None

    def push(self, val: int) -> None:
        new_head = self.ListNode(val, self.head)
        self.head = new_head
        if self.min_val == None:
            pass
        else:
            self.min_val = min(val, self.min_val)

    def pop(self) -> None:
        ret_val = self.head.val
        self.head = self.head.next
        if ret_val == self.min_val:
            self.min_val = None
        return ret_val

    def top(self) -> int:
        return self.head.val

    def __iter__(self):
        return LinkedListIterator(self.head)

    def getMin(self) -> int:
        if self.min_val == None:
            self.min_val = min(self)
        return self.min_val



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

```
## Implement Stack using Queues

<https://leetcode.com/problems/implement-stack-using-queues/>

```python3
from collections import deque


class QueueFromDeque:
    def __init__(self):
        self.kernel = deque()


    def add(self, val):
        self.kernel.appendleft(val)


    def remove(self):
        return self.kernel.pop()


    def peek(self):
        ret_val = self.kernel.pop()
        self.kernel.append(ret_val)
        return ret_val


    def is_empty(self):
        return (len(self.kernel) == 0)


    def __len__(self):
        return self.kernel.__len__()


class MyStack:
    def __init__(self):
        self.q = QueueFromDeque()


    def push(self, x: int) -> None:
        self.q.add(x)
        n = len(self.q)
        for _ in range(n - 1):
            self.q.add(self.q.remove())


    def pop(self) -> int:
        return self.q.remove()


    def top(self) -> int:
        return self.q.peek()


    def empty(self) -> bool:
        return self.q.is_empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

```

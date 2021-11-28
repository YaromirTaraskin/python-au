# Design

+ [Min Stack](#min-stack)

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
        new_head = ListNode(val, self.head)
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
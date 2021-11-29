#Linked-List

+ [Reverse Linked List](#reverse-linked-list)

+ [Palindrome Linked List](#palindrome-linked-list)

+ [Middle of the Linked List](#middle-of-the-linked-list)

## Reverse Linked List

<https://leetcode.com/problems/reverse-linked-list/>

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            new_prev = cur
            new_nxt = prev
            new_cur = cur.next
            prev = new_prev
            cur.next = new_nxt
            cur = new_cur
        return prev
            
```

## Middle of the Linked List

<https://leetcode.com/problems/middle-of-the-linked-list/>

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        l = 0
        while cur != None:
            cur = cur.next
            l += 1
        cur = head
        for _ in range(l//2):
            cur = cur.next
        return cur

```

## Palindrome Linked List

<https://leetcode.com/problems/palindrome-linked-list/>

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_middle(self, head):
        slow = fast = head
        while fast != None and fast.next != None:
            fast, slow = fast.next.next, slow.next
        return slow


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = self.find_middle(head)
        node = None
        while slow != None:
            slow.next, node, slow = node, slow, slow.next
        while node != None:
            if node.val != head.val:
                return False
            else:
                node, head = node.next, head.next
        return True

```

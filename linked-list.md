#Linked-List

+ [Reverse Linked List](#reverse-linked-list)

+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

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

## Merge Two Sorted Lists

<https://leetcode.com/problems/merge-two-sorted-lists/>

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        zero_node = ans
        while (list1 != None and list2 != None):
            if (list1.val <= list2.val):
                ans.next = list1
                list1 = list1.next
            else:
                ans.next = list2
                list2 = list2.next
            ans = ans.next

        if list1 == None:
            list1 = list2
        while (list1 != None):
            ans.next = list1
            list1 = list1.next
            ans = ans.next

        return zero_node.next

```

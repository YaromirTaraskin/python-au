# Linked-List

+ [Reverse Linked List](#reverse-linked-list)

+ [Sort List](#sort-list)

+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)

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

## Intersection of Two Linked Lists

<https://leetcode.com/problems/intersection-of-two-linked-lists/>

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def ll_len(self, head):
            temp = head
            n = 0
            while temp:
                n +=1
                temp = temp.next
            return n

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n1 = self.ll_len(headA)
        n2 = self.ll_len(headB)
        if n1 < n2:
            headA, headB, n1, n2 = headB, headA, n2, n1
        diff = n1 - n2
        tempA = headA
        for i in range(diff, 0, -1):
            tempA = tempA.next
        tempB = headB
        while tempA:
            if tempA == tempB:
                return tempA
            else:
                tempA, tempB = tempA.next, tempB.next
        return None

```

## Sort List

<https://leetcode.com/problems/sort-list/>

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        midPrev = None
        while (head != None and head.next != None):
            midPrev = head if (midPrev == None) else midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid


    def merge(self, list1, list2):
        cur = ListNode()
        tail = cur
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        tail.next = list1 if (list1 != None) else list2
        return cur.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

```

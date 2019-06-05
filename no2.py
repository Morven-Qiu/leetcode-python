# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        temp = str(self.val);
        t = self
        while(t.next is not None):
            temp = temp +  ","+ str(t.next.val)
            t = t.next
        return temp

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = last = ListNode(0);
        left = 0;
        while l1 or l2 or left :
            temp1 = temp2 = 0;
            if l1 :
                temp1 = l1.val
                l1 = l1.next
            if l2 :
                temp2 = l2.val
                l2 = l2.next
            sum = temp2 + temp1 + left
            left = int(sum / 10)
            temp3 = ListNode(sum%10)
            last.next = temp3
            last = temp3
        return result.next


n1 = ListNode(1)
n2 = ListNode(9)
n1.next = n2
n3 = ListNode(9)


t = Solution()

print(t.addTwoNumbers(n1,n3))
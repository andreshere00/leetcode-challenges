# TODO: Still is not completely right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        flag = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + flag
            flag = total // 10
            if total > 9:
                current.next = ListNode(total % 10)
            else:
                current.next = ListNode(total % 10 + flag)
                flag = 0

            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

def list_to_listnode(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def listnode_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

sol = Solution()

l1 = list_to_listnode([2,4,3]) 
l2 = list_to_listnode([5,6,4]) 

solution = sol.addTwoNumbers(l1, l2)
print(listnode_to_list(solution) == [7,0,8])

l1 = list_to_listnode([0]) 
l2 = list_to_listnode([0]) 

solution = sol.addTwoNumbers(l1, l2)
print(listnode_to_list(solution) == [0])

l1 = list_to_listnode([9,9,9,9,9,9,9]) 
l2 = list_to_listnode([9,9,9,9]) 

solution = sol.addTwoNumbers(l1, l2)
print(listnode_to_list(solution) == [8,9,9,9,0,0,1])


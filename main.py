class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        pointerA = headA
        pointerB = headB
        
        while pointerA != pointerB:
            # Move to the next node or switch to the other head
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        return pointerA  # Can return either pointerA or pointerB; both are the same at this point

# Example usage:
# Assume you have already created linked list nodes and connected them as needed.
# solution = Solution()
# intersection_node = solution.getIntersectionNode(headA, headB)
# if intersection_node:
#     print("Intersected at:", intersection_node.val)
# else:
#     print("No intersection")

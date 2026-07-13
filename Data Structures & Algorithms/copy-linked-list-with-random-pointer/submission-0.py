"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.Map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        if head in self.Map: 
            return self.Map[head]
        
        copy = Node(head.val)
        self.Map[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.Map.get(head.random)
        return copy


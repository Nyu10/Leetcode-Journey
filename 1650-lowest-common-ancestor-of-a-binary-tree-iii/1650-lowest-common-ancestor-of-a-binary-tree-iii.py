"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q

        # Traverse until both pointers meet
        while a != b:
            # Move each pointer up, or switch to the other node when reaching None
            a = a.parent if a else q
            b = b.parent if b else p

        return a
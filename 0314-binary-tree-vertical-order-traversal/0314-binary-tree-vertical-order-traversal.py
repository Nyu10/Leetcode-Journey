# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        columnTable = defaultdict(list)
        queue = deque([(root,0)])
        minCol = maxCol = 0
        while queue:
            node, column = queue.popleft()
            if node:
                columnTable[column].append(node.val)
                minCol = min(minCol, column)
                maxCol = max(maxCol, column)


                queue.append((node.left, column-1))
                queue.append((node.right, column+1))
        res = []
        for col in range(minCol, maxCol + 1):
            res.append(columnTable[col])
        return res
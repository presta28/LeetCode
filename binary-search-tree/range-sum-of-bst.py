# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ=0
        def range(node:Optianal[TreeNode]):
            nonlocal summ
            if node==None:
                return 
            range(node.left)
            if node.val>=low and node.val<=high:
                summ+=node.val
            range(node.right)
            return
        range(root)
        return summ        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ancestor(node:Optianal[TreeNode]):
            if node==None:
                return None
            if p.val>node.val and q.val>node.val:
                ans= ancestor(node.right)
            elif p.val<node.val and q.val<node.val:
                ans =  ancestor(node.left)
            else:
                return node
            return ans
        return ancestor(root)
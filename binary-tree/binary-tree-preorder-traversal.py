# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1=[]
        def preorder(node:optional[TreeNode]):
            if node==None:
                return
            list1.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return list1
        
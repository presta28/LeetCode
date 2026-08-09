# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(node1:Optional[TreeNode],node2: Optional[TreeNode]):
            if node1==None and node2==None:
                return True
            if node1!=None and node2 == None:
                return False
            if node2!=None and node1 == None:
                return False   
            if node1.val!=node2.val:
                return False
            lefttree= same(node1.left,node2.left)
            righttree = same(node1.right,node2.right)
            return lefttree and righttree
        return same(p,q)


            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        s = ""
        answer=[]
        def path(node:Optinal[TreeNode],s:str):
            if node==None:
                return
            s = s +str(node.val) + "-" + ">"
            if node.left==None and node.right==None:
                answer.append(s[:-2])
                s=s[:-3]
                return 
            path(node.left,s)
            path(node.right,s)
            return
        path(root,s)
        return answer        
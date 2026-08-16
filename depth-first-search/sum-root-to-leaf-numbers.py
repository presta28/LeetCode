# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s=""
        answer=[]
        def solution(node:Optinal[TreeNode],s:str):
            if node==None:
                return
            s=s+str(node.val)
            if node.left==None and node.right == None:
                answer.append(int(s))
                return
            solution(node.left,s)
            solution(node.right,s)
            return
        solution(root,s)
        ans=0
        for i in answer:
            ans=ans+i
        return ans
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dictt={}
        listt=[]
        def find(node:Optinal[TreeNOde]):
            nonlocal dictt
            if node==None:
                return
            find(node.left)
            if node.val not in dictt:
                dictt[node.val]=1
            else:
                dictt[node.val]+=1
            find(node.right)
            return
        find(root)
        for key ,value in dictt.items():
            if len(listt)==0:
                listt.append(key)
            else:
                if value>listt[-1]:
                    listt.pop()
                    listt.append(key)
                elif value==listt[-1]:
                    listt.append(key)
        return listt

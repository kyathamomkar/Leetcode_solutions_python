# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.finalans = None
        def sendParent(root):
            if not root:
                return False
            leftans=rightans=myans= False
            leftans = sendParent(root.left)
            rightans = sendParent(root.right)
            myans = root in [p,q]
            if leftans + rightans + myans >=2 :
                self.finalans = root
            return leftans or rightans or myans
            
        sendParent(root)
        return self.finalans
        
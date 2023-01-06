# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        answer = []

        def recursive(root, answer):
            if root == None :
                return;
            recursive(root.left,answer)
            answer.append(root.val)
            recursive(root.right,answer)
        
        recursive(root,answer)

        return answer

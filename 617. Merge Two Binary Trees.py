class Solution(object):
    def mergeTrees(self, root1, root2):
        def recursive(a,b) :
            if a == None and b != None :
                return b
            elif a != None and b == None :
                return a
            elif a == None and b == None :
                return ;
            else : 
                a.val = a.val + b.val
            a.left = recursive(a.left,b.left)
            a.right = recursive(a.right,b.right)
            return a

        
        return recursive(root1,root2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        compliment_dict = {} #compliment val
        
        q = deque()
        q.append(root)
        
        while q:
            
            level_len = len(q)
            
            for i in range(level_len):
                
                node = q.popleft()
                
                if node:
                    compliment = k - node.val
                    if node.val in compliment_dict:
                        return True
                    compliment_dict[compliment] = node.val
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
        print(compliment_dict)        
        return False
        
        
        
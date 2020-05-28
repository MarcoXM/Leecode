## may-28th

\617. Merge Two Binary Trees

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        ## 就四种情况,
        ## 先写终止
        if not t1 and not t2:
            return 
        
        ## root 开始 中序
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
        if not t2 :
            return t1
        if not t1 :
            return t2
      
        return root
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        ## 就四种情况,
        ## 先写终止
        if not t1: return t2
        if not t2: return t1
        q = collections.deque()
        q.append((t1,t2))
        while q:
            n1, n2 = q.popleft()
            n1.val += n2.val
            if n1.left and n2.left:
                q.append((n1.left,n2.left))
            if not n1.left and n2.left:
                n1.left = n2.left

            if n1.right and n2.right:
                q.append((n1.right,n2.right))
            if not n1.right and n2.right:
                n1.right = n2.right
                    
        return t1 # return type 为tree 尽量不对输入tree 进行破坏
                
```

\606. Construct String from Binary Tree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        ## preorder traversing way
        
        return self.t(root)
        
    def t(self, root) -> str:
        if not root:
            return ""
        
        res = str(root.val)
        if root.left:
            res += "("
            res += self.t(root.left)
            res += ")"
            if root.right:
                res += "("
                res += self.t(root.right)
                res += ")"
        else:
            if root.right:
                res += "()" ## 左边空了
                res += "("
                res += self.t(root.right)
                res += ")"
        return res
        
            
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        ## preorder traversing way
        ans = ""
        if root == None:
            return ans
        stack = [root]
        while stack:
            node = stack.pop()
            if node == ')' or node == '(' or node == '()':
                ans += node
                
            else:
                ans += str(node.val)
                if not node.right and not node.left:
                    continue
                if node.right: # stack 反过来,先右
                    stack.append(')')
                    stack.append(node.right)
                    stack.append('(')
                if node.left:
                    stack.append(')')
                    stack.append(node.left)
                    stack.append('(')
                else: # 没有左边
                    stack.append('()')
        return ans


            
        
            
```


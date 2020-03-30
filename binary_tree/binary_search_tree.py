


#235. 二叉搜索树的最近公共祖先

class Solution:
    #1.递归
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if p.val > root.val < q.val:
    #         self.lowestCommonAncestor(root.right, p, q)
    #     elif p.val < root.val > q.val:
    #         self.lowestCommonAncestor(root.left, p, q)
    #     else:
    #         return root
    #2.迭代
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        pv = p.val
        nv = q.val
        while node:
            nodeval = node.val
            if pv > nodeval < nv:
                node = node.right
            elif pv < nodeval > nv:
                node = node.left
            else:
                return node

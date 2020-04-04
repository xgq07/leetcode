from typing import List
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        self.valList = []
        self.invert = None #翻转的树

    # node 在本身的类中
    def add(self, val):
        if val > self.val:
            if self.right is not None:
                self.right.add(val)
            else:
                newNode = BinarySearchTree(val)
                self.right = newNode
        elif val < self.val:
            if self.left is not None:
                self.left.add(val)
            else:
                newNode = BinarySearchTree(val)
                self.left = newNode

    # node 另存在TreeNode类
    def add_For_All(self, node, val):
        if val < node.val:
            if node.left is not None:
                self.add_For_All(node.left, val)
            else:
                newNode = TreeNode(val)
                node.left = newNode

        if val > node.val:
            if node.right is not None:
                self.add_For_All(node.right, val)
            else:
                newNode = TreeNode(val)
                node.right = newNode


    def delete(self):
        pass

    def find(self, node, val):
        # if val > node.val:
        #     if node.right is not None:
        #         return self.find(node.right, val)
        #     else:
        #         return None
        # elif val < node.val:
        #     if node.left is not None:
        #         return self.find(node.left, val)
        #     else:
        #         return None      
        # else:
        #     return node.val

        while node is not None:
            if val > node.val : node = node.right
            elif val < node.val : node = node.left
            else : return node.val
        return None

    
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)


    def preorder(self, node):
        if node is None:
            return
        print(node.val)
        self.preorder(node.left)
        self.preorder(node.right)


    def postorder(self, node):
        if node is None:
            return
        self.preorder(node.left)
        self.preorder(node.right)
        print(node.val)


    # 94. 二叉树的中序遍历
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # if root is None:
        #     return
        
        # self.inorderTraversal(root.left)
        # self.valList.append(root.val)
        # self.inorderTraversal(root.right)
        
        # return self.valList

        # 迭代
        res, stack = [], []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res

            node = stack.pop()
            res.append(node.val)
            root = node.right
    
    #144. 二叉树的前序遍历
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return self.valList
        
        self.valList.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.valList

    #590. N叉树的后序遍历
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return self.valList
        for child in root.children:
            self.postorder(child)

        self.valList.append(root.val)

        return self.valList
    
    # 广度遍历
    def levelOrder(self, root):
        # write your code here
        res = []
        # 如果根节点为空，则返回空列表
        if root is None:
            return res
        # 模拟一个队列储存节点
        q = []
        # 首先将根节点入队
        q.append(root)
        # 列表为空时，循环终止
        while len(q) != 0:
            length = len(q)
            for i in range(length):
                # 将同层节点依次出队
                r = q.pop(0)
                if r.left is not None:
                    # 非空左孩子入队
                    q.append(r.left)
                if r.right is not None:
                    # 非空右孩子入队
                    q.append(r.right)
                res.append(r.val)
        return res

    # 226. 翻转二叉树
    def invertTree(self, root: TreeNode) -> TreeNode:
        # terminator
        if root is None:
            return
        # process
        # drill down
        self.invertTree(root.right)
        self.invertTree(root.left)
        # reverse states
        leftnode = root.left
        rightnode = root.right
        root.left = rightnode
        root.right = leftnode
        return root
        
    # 98. 验证二叉搜索树
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

    # 104. 二叉树的最大深度
    def maxDepth(self, root: TreeNode) -> int:
        # terminator
            if root is None:
                return 0
        # process

        # drill down 
            lefth = self.maxDepth(root.left)
            righth = self.maxDepth(root.right)

            return max(lefth, righth) + 1
        # reverse states


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
            if pv > node.val < nv:
                node = node.right
            elif pv < node.val > nv:
                node = node.left
            else:
                return node


if __name__ == "__main__":
    # b = BinarySearchTree(6)
    # b.add(2)
    # b.add(8)
    # b.add(0)
    # b.add(4)
    # b.add(7)
    # b.add(9)
    # preorder(b)
    # print("---------")
    # inorder(b)
    # print("---------")
    # postorder(b)

    b1 = TreeNode(6)
    b_control = BinarySearchTree()
    b_control.add_For_All(b1, 2)
    b_control.add_For_All(b1, 8)
    b_control.add_For_All(b1, 0)
    b_control.add_For_All(b1, 4)
    b_control.add_For_All(b1, 7)
    b_control.add_For_All(b1, 9)
    b_control.inorder(b1)
    print("find result:", b_control.find(b1, 2))

    print("中序")
    print(b_control.inorderTraversal(b1))
    print("前序")
    print(b_control.preorderTraversal(b1))
    print("广度")
    print(b_control.levelOrder(b1))
    b2 = b1
    print("是否二叉搜索树")
    print(b_control.isValidBST(b1))
    print("翻转")
    b_control.invertTree(b1)
    print(b_control.levelOrder(b1))
    print("是否二叉搜索树")
    print(b_control.isValidBST(b1))
    print(b_control.maxDepth(b1))

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

class BinaryTree():
    def __init__(self, dataval):
        super().__init__()
        self.val = dataval
        self.left = None
        self.right = None

    def append_left_node(self, val):
        if self.left != None:
            self.left.append_left_node(val)
        else:
            self.left = BinaryTree(val)

    def append_right_node(self, val):
        if self.right != None:
            self.right.append_right_node(val)
        else:
            self.right = BinaryTree(val)



class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        print(f"b1.Val:{p.val}, b2.Val:{q.val}")
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    b1 = BinaryTree(1)
    b2 = BinaryTree(1)
    b1.append_left_node(2)
    b2.append_left_node(2)
    b1.append_right_node(3)
    b2.append_right_node(3)
   
    s = Solution()
    print(s.isSameTree(b1, b2))
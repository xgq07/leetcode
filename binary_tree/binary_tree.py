# class Node:
# 	def __init__(self, dataval):
# 		self.dataval = dataval
# 		self.leftchild = None
# 		self.rightchild = None


# class Bi_tree:
# 	def __init__(self):
# 		self.rootval = None
# 		self.queue = []  # 将节点的值存放在列表中

# 	def creat(self, newdata):
# 		Newnode = Node(newdata)
# 		if self.rootval == None:
# 			self.rootval = Newnode
# 			self.queue.append(self.rootval)
# 		else:
# 			laste = self.queue[0]
# 			# print(laste.dataval)
# 			if laste.leftchild == None:
# 				laste.leftchild = Newnode
# 				self.queue.append(laste.leftchild)
# 			else:
# 				laste.rightchild = Newnode
# 				self.queue.append(laste.rightchild)
# 				#如果该结点存在右子树，将此结点丢弃。
# 				self.queue.pop(0)

# 	#先序遍历
# 	def pre_order(self, rootval):
# 		#主要是利用递归算法
# 		#第一步：临界点---有回
# 		if rootval == None:
# 			return None
# 		#第二步：算法（根节点->左子树->右子树）---可去
# 		print(rootval.dataval, end=' ')
# 		self.pre_order(rootval.leftchild)
# 		self.pre_order(rootval.rightchild)

# 	def mid_order(self, rootval):
# 		#主要利用递归算法
# 		#第一步：临界点---有回
# 		if rootval == None:
# 			return None
# 		#第二步：算法（左子树->根节点->右子树）
# 		self.pre_order(rootval.leftchild)
# 		print(rootval.dataval, end=' ')
# 		self.pre_order(rootval.rightchild)

# 	def post_order(self, rootval):
# 		if rootval == None:
# 			return None
# 		self.pre_order(rootval.leftchild)
# 		self.pre_order(rootval.rightchild)
# 		print(rootval.dataval, end=' ')
	
#     #层次遍历----广度优先遍历
# 	def level_order(self, rootval):
# 		if rootval is None:
# 			return None
# 		q = []
# 		# 首先将根节点入队
# 		q.append(rootval)
# 		# 列表为空时，循环终止
# 		while len(q) != 0:
# 			length = len(q)
# 			for i in range(length):
# 				# 将同层节点依次出队
# 				r = q.pop(0)
# 				if r.leftchild is not None:
# 					# 非空左孩子入队
# 					q.append(r.leftchild)
# 				if r.rightchild is not None:
# 					# 非空右孩子入队
# 					q.append(r.rightchild)
# 				print(r.dataval)


class BinaryTree():
    def __init__(self, dataval):
        super().__init__()
        self.dataval = dataval
        self.leftchild = None
        self.rightchild = None

    def append_left_node(self, val):
        if self.leftchild != None:
            self.leftchild.append_left_node(val)
        else:
            self.leftchild = BinaryTree(val)

    def append_right_node(self, val):
        if self.rightchild != None:
            self.rightchild.append_right_node(val)
        else:
            self.rightchild = BinaryTree(val)


    def pre_order(self):
        # print(self.dataval)
        if self.leftchild != None:
            # print(self.dataval)
            self.leftchild.pre_order()
        
        if self.rightchild != None:
            self.rightchild.pre_order()
        # print(self.dataval)

def preorder(tree):
    if tree:
        print(tree.dataval)
        preorder(tree.leftchild)
        preorder(tree.rightchild)

def inorder(tree):
    if tree:
        inorder(tree.leftchild)
        print(tree.dataval)
        inorder(tree.rightchild)

def postorder(tree):
    if tree:
        postorder(tree.leftchild)
        postorder(tree.rightchild)
        print(tree.dataval)

if __name__ == '__main__':
    # b_tree = BinaryTree()
    # b_tree.create_root(1)
    # b_tree.append_left_node(2, b_tree.root)
    # b_tree.append_left_node(3, b_tree.root)
    # b_tree.pre_order(b_tree.root)
    
    root = BinaryTree(1)
    root.append_left_node(2)
    root.append_left_node(3)
    root.append_right_node(4)
    print("preorder:")
    preorder(root)
    print("inorder:")
    inorder(root)
    print("postorder")
    postorder(root)





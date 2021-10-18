'''
-- Tree has a root, branches, leaves.
-- all children of one node are independent of children of another node
-- each leaf node is unique

-- Node : fundamental part of tree. It has:
    1. name: called "key"
    2. additional information : called "payload"
-- Edge : connects 2 nodes
-- Every node(except root) is connected by exactly one incoming edge, but several outgoing edges
-- path : ordered list of nodes connected by edges 
-- leaf node : node with no children
-- level of node : number of edges between node and rootnode
-- height of tree : maximum level of any node
-- if each node in the tree has maximum of 2 children, the tree is called "binary tree"
-- A tree can be pictured as "a root" and "many subtrees", each of which is also a tree
'''
#implementation
class BinaryTree(object):
    def __init__(self,rootobj) -> None:
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None
    def insertleft(self,newnode):
        if self.leftchild == None:
            self.leftchild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.leftchild = self.leftchild
            self.leftchild = t
    def insertright(self,newnode):
        if self.rightchild == None:
            self.rightchild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.rightchild = self.rightchild
            self.rightchild = t
    def getrightchild(self):
        return self.rightchild
    def getleftchild(self):
        return self.leftchild
    def setrootvalue(self, obj):
        self.key = obj
    def getrootvalue(self):
        return self.key
r = BinaryTree("a")
r.insertleft("b")
r.getrootvalue() #-------> a
r.getleftchild().getrootvalue() #-------> b

#Tree Traversal :
'''
1) Preorder traversal : visit root node, then recursively do preorder traversal of left subtree, then a recursive preorder traversal of right subtree
2) Inorder traversal : recursive inorder traversal on left subtree then visit root node, then a recursive inorder traversal of right subtree
3) Post transversal : recursive post order traversal on left subtree, then recursive post order traversal on right subtree, then visit root node
'''
#Pre-order:
def preorder(tree):
    if tree:
        print(tree.getrootvalue())
        preorder(tree.getleftchild())
        preorder(tree.getrightchild())
#Post-order:
def postorder(tree):
    if tree != None:
        postorder(tree.getleftchild())
        postorder(tree.getrightchild())
        print(tree.getrootvalue())
#In-order:
def inorder(tree):
    if tree != None:
        inorder(tree.getleftchild())
        print(tree.getrootvalue())
        inorder(tree.getrightchild())

#Binary Search Tree(BST)
'''
-- keys that are left than parent are in left subtree, keys greater than parent found in right subtree (the BST property)
'''
class TreeNode:
    def __init__(self, key,val,left=None, right=None, parent=None) -> None:
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent
    def has_left_child(self):
        return self.leftchild
    def has_right_child(self):
        return self.rightchild
    def is_left_child(self):
        return self.parent and self.parent.leftchild==self
    def is_right_child(self):
        return self.parent and self.parent.rightchild == self
    def is_root(self):
        return not self.parent
    def is_leaf(self):
        return not (self.rightchild or self.leftchild)
    def has_any_children(self):
        return self.rightchild or self.leftchild
    def has_both_children(self):
        return self.rightchild and self.leftchild
    def replace_node_data(self, key, value,lchild,rchild):
        self.key = key
        self.payload = value
        self.leftchild = lchild
        self.rightchild = rchild
        if self.has_left_child():
            self.leftchild.parent = self
        if self.has_right_child():
            self.rightchild.parent = self
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.size = 0
        def length(self):
            return self.size
        def __len__(self):
            return self.size
        def put(self,key,val):
            if self.root:
                self._put(key,val,self.root)
            else:
                self.root = TreeNode(key,val)
            self.size = self.size + 1
        def _put(self, key,val,currentnode):
            if key < currentnode.key:
                if currentnode.has_left_child():
                    self._put(key,val,currentnode.leftchild)
                else:
                    currentnode.leftchild = TreeNode(key,val,parent=currentnode)
            else:
                if currentnode.has_right_child():
                    self._put(key,val,currentnode.rightchild)
                else:
                    currentnode.rightchild = TreeNode(key,val,parent=currentnode)
        def __setitem__(self,key,val):
            self.put(key,val)
        def get(self,key):
            if self.root:
                res = self._get(key,self.root)
                if res:
                    return res.payload
                else:
                    return None
            else:
                return None
        def _get(self,key,currentnode):
            if not currentnode:
                return None
            elif currentnode.key == key:
                return currentnode
            elif key<currentnode.key:
                return self._get(key,currentnode.leftchild)
            else:
                return self._get(key,currentnode.rightchild)
        def __getitem__(self,key):
            return self.get(key)
        def __contains__(self,key):
            if self._get(key,self.root):
                return True
            else:
                return False
        def findmin(self):
            current = self
            while current.has_left_child():
                current = current.leftchild
            return current
        def find_successor(self):
            succ = None
            if self.has_right_child():
                succ = self.rightchild.findmin()
            else:
                if self.parent:
                    if self.is_left_child():
                        succ = self.parent
                    else:
                        self.parent.rightchild = None
                        succ = self.parent.find_successor()
                        self.parent.rightchild = self
            return succ
        def spliceout(self):
            if self.is_leaf():
                if self.is_left_child():
                    self.parent.leftchild = None
                else:
                    self.parent.rightchild = None
            elif self.has_any_children():
                if self.has_left_child():
                    if self.is_left_child():
                        self.parent.leftchild = self.leftchild
                    else:
                        self.parent.rightchild = self.leftchild
                        self.leftchild.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.leftchild = self.rightchild
                else:
                    self.parent.rightchild = self.rightchild
                    self.rightchild.parent = self.parent
        def remove(self,currentnode):
            if currentnode.is_leaf():
                if currentnode == currentnode.parent.leftchild:
                    currentnode.parent.leftchild = None
                else:
                    currentnode.parent.rightchild = None
            elif currentnode.has_both_children():
                succ = currentnode.findsuccessor()
                succ.spliceout()
                currentnode.key = succ.key
                currentnode.payload = succ.payload
            else:
                if currentnode.has_left_child():
                    if currentnode.is_left_child():
                        currentnode.leftchild.parent = currentnode.parent
                        currentnode.parent.leftchild = currentnode.leftchild
                    elif currentnode.is_right_child():
                        currentnode.leftchild.parent = currentnode.parent
                        currentnode.parent.rightchild = currentnode.leftchild
                    else:
                        currentnode.replace_node_data(
                            currentnode.leftchild.key,
                            currentnode.leftchild.payload,
                            currentnode.leftchild.leftchild,
                            currentnode.leftchild.rightchild
                        )
                else:
                    if currentnode.is_left_child():
                        currentnode.rightchild.parent = currentnode.parent
                        currentnode.parent.leftchild = currentnode.rightchild
                    elif currentnode.is_right_child():
                        currentnode.rightchild.parent = currentnode.parent
                        currentnode.parent.leftchild = currentnode.rightchild
                    else:
                        currentnode.replace_node_data(
                            currentnode.rightchild.key,
                            currentnode.rightchild.payload,
                            currentnode.rightchild.leftchild,
                            currentnode.rightchild.righchild
                        )
        def delete(self,key):
            if self.size > 1:
                nodetoremove = self._get(key,self.root)
                if nodetoremove:
                    self.remove(nodetoremove)
                    self.size -= 1
                else:
                    raise KeyError ("Error, key not in tree")
            elif self.size == 1 and self.root.key==key:
                self.root = None
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        def __delitem__(self,key):
            self.delete(key)  
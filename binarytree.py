class node:
    def __init__(self,v):
        self.value=v
        self.left=None
        self.right=None
class stack:
    def __init__(self):
        self.list=[]
    def push(self,val):
        self.list.append(val)

    def pop(self):
        x=self.list.pop(0)
        return x
    def size(self):
        return len(self.list)
class binarytree:
    def __init__(self,root):
        self.root=node(root)
    def inorder(self,start,traversal):
        if start:
            traversal=self.inorder(start.left,traversal)
            traversal+=str(start.value)+"-"
            traversal=self.inorder(start.right,traversal)
        return traversal
    def preorder(self,start,traversal):
        if start:
            traversal+=str(start.value)+"-"
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return traversal
    def postorder(self,start,traversal):
        if start:
            traversal=self.postorder(start.left,traversal)
            traversal=self.postorder(start.right,traversal)
            traversal+=str(start.value)+"-"
        return traversal
    def levelorder(self,start,traversal):
        if start:
            s=stack()
            s.push(start)
            while s.size()>0:
                k=s.pop()
                traversal+=str(k.value)+"-"
                if k.left != None:
                    s.push(k.left)
                if k.right != None:
                    s.push(k.right)
        return traversal
    def height(self,start):
        if start == None:
            return -1
        leftheight=self.height(start.left)
        rightheight=self.height(start.left)

        return 1+max(leftheight,rightheight)

    def leftView(self,start,traversal):
        if start is None:
            return

        s=stack()
        s.push(start)
        while s.size()>0:
            l=s.size()
            i=0
            while i<l:
                i=i+1
                k=s.pop()
                if i==1:# for left view 1st node in each level
                    traversal+=str(k.value)+"-"
                if k.left != None:
                    s.push(k.left)
                if k.right != None:
                    s.push(k.right)

        return traversal

    def rightView(self,start,traversal):
        if start is None:
            return

        s=stack()
        s.push(start)
        while s.size()>0:
            l=s.size()
            i=0
            while i<l:
                i=i+1
                k=s.pop()
                if i==l:## for left view last node in each level
                    traversal+=str(k.value)+"-"
                if k.left != None:
                    s.push(k.left)
                if k.right != None:
                    s.push(k.right)

        return traversal
                

                    
                    
                

tree=binarytree(5)

tree.root.left=node(2)
tree.root.right=node(3)
tree.root.left.left=node(6)
tree.root.left.right=node(7)

print("inorder:"+tree.inorder(tree.root,""))
print("preorder:"+tree.preorder(tree.root,""))
print("postorder:"+tree.postorder(tree.root,""))
print("levelorder:"+tree.levelorder(tree.root,""))
print("height:"+ str(tree.height(tree.root)))
print("leftview:"+ str(tree.leftView(tree.root,"")))
print("rightview:"+ str(tree.rightView(tree.root,"")))

        

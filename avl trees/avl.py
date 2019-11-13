class Node(object):
    def __init__(self,data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVL(object):
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.insertNode(data, self.root)

    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def insertNode(self,data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleViolation(data, node)

    def settleViolation(self,data, node):
        balance = self.calcBalance(node)

        # case 1 -> left left heavy situation
        if balance > 1 and node.leftChild.data:
            print("left left heavy situation")
            return self.rotateRight(node)
        #case 2 -> right right heavy sitation 
        if balance < - 1 and data > node.rightChild.data:
            print("right right heavy sitation ")
            return self.rotateLeft(node)

        if balance > 1 and data > node.leftChild.data:
            print("left right heavy situation")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and data < node.rightChild.data:
            print("right left heavy situation")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

       

    def removeNode(self, data, node):
        if not node:
            return node
        
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)

        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)

        else:
            if not node.leftChild and not node.rightChild:
                print("Removing leaf node")
                del node
                return None

            if not node.leftChild:
                print("Removing a node with  right child")
                tempNode = node.rightChild
                del node
                return tempNode

            elif not node.rightChild:
                print("Removing a node with left child")
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing node with two children")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        if not node:
            return node

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        balance = self.calcBalance(node)

        # case 1 -> left left heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            print("left left heavy situation")
            return self.rotateRight(node)
        #case 2 -> right right heavy sitation 
        if balance > 1 and  self.calcBalance(node.leftChild) < 0:
            print("right right heavy sitation ")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance <  -1 and  self.calcBalance(node.rightChild <=0):
            return self.rotateLeft(node)

        if balance < -1 and  self.calcBalance(node.rightChild) > 0:
          
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

         


    def calcHeight(self,node):
        if not node:
            return -1
        return node.height

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self,node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
            print(" ",node.data)
        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    #if it return value > than 1 it means it is a left heavy tree --> right rotation
    #                   < right heavy tree --> left rotation
    def calcBalance(self,node):
        if not node:
            return 0
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def rotateRight(self,node):
        print("rotating to right ", node.data)
        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node

        node.leftChild = t
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1

        return tempLeftChild

    def rotateLeft(self,node):
        print("rotating to left ", node.data)
        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node

        node.rightChild = t
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1

        return tempRightChild

avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(6)
avl.insert(15)


avl.remove(15)
avl.remove(20)

avl.traverse()
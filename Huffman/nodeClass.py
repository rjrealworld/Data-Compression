class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setLeftChild(self, left):
        self.left = left

    def setRightChild(self, right):
        self.right = right

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def hasLeftChild(self):
        return self.left != None

    def hasRightChild(self):
        return self.right != None

    def __repr__(self):
        return Node({self.getValue()})

    def __str__(self):
        return Node({self.getValue()})
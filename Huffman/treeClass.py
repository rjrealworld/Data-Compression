from queue import Queue

class Tree:

    def __init__(self):
        self.root = None

    def setRoot(self, value):
        self.root = Node(value)

    def getRoot(self):
        return self.root

    def __repr__(self):
        level = 0
        q = Queue()
        visitOrder = list()
        node = self.getRoot()
        q.enq((node, level))
        while (len(q) > 0):
            node, level = q.deq()
            if node == None:
                visitOrder.append(("<empty>", level))
                continue
            visitOrder.append((node, level))
            if node.hasLeftChild():
                q.enq((node.getLeftChild(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.hasRightChild():
                q.enq((node.getRightChild(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previousLevel = -1
        for i in range(len(visitOrder)):
            node, level = visitOrder[i]
            if level == previousLevel:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previousLevel = level

        return s
import sys
from nodeClass import Node
from treeClass import Tree

"""
Pseudocode:
1. Take a string and determine the relevant frequencies of the characters
2. Build and sort a list of tuples from lowest to highest frequencies
3. Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters
4. Trim the Huffman Tree (remove the frequencies from the previously built tree)
5. Encode the text into its compressed form
"""

def returnFrequency(data):
    # Take a string and determine the relevant frequencies of the characters
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    lst = [(v, k) for k, v in frequency.items()]
    # Build and sort a list of tuples from lowest to highest frequencies
    lst.sort(reverse=True)
    print("Frequency array is: ", end="")
    print(lst)
    return lst


# A helper function to the buildTree()
def sortValues(nodesList, node):
    nodeValue, char1 = node.value
    index = 0
    maxIndex = len(nodesList)
    while True:
        if index == maxIndex:
            nodesList.append(node)
            return
        currentVal, char2 = nodesList[index].value
        if currentVal <= nodeValue:
            nodesList.insert(index, node)
            return
        index += 1


# Build a Huffman Tree: nodes are stored in list with their values (frequencies) in descending order.
# Two nodes with the lowest frequencies form a tree node. That node gets pushed back into the list and the process repeats
def buildTree(data):
    lst = returnFrequency(data)
    nodesList = []
    for nodeValue in lst:
        node = Node(nodeValue)
        nodesList.append(node)
    
    while len(nodesList) != 1:
        firstNode = nodesList.pop()
        secondNode = nodesList.pop()
        val1, char1 = firstNode.value
        val2, char2 = secondNode.value
        node = Node((val1 + val2, char1 + char2))
        node.setLeftChild(secondNode)
        node.setRightChild(firstNode)
        sortValues(nodesList, node)

    root = nodesList[0]
    tree = Tree()
    tree.root = root
    return tree

# the function traverses over the huffman tree and returns a dictionary with letter as keys and binary value and value.
# function getCodes() is for encoding purposes
def getCodes(root):
    if root is None:
        return {}
    frequency, characters = root.value
    charDict = dict([(i, '') for i in list(characters)])

    leftBranch = getCodes(root.getLeftChild())

    for key, value in leftBranch.items():
        charDict[key] += '0' + leftBranch[key]

    rightBranch = getCodes(root.getRightChild())

    for key, value in rightBranch.items():
        charDict[key] += '1' + rightBranch[key]
    return charDict


# when we've got the dictionary of binary values and huffman tree, tree encoding is simple
def huffmanEncodingFunc(data):
    if data == '':
        return None, ''
    tree = buildTree(data)
    dict = getCodes(tree.root)
    codes = ''
    print("Encoded elements are: ", end="")
    print(dict)
    for char in data:
        codes += dict[char]
    return tree, codes


# The function traverses over the encoded data and checks if a certain piece of binary code could actually be a letter
def huffmanDecodingFunc(data, tree):
    if data == '':
        return ''
    dict = getCodes(tree.root)
    reversedDict = {}
    for value, key in dict.items():
        reversedDict[key] = value
    startIndex = 0
    endIndex = 1
    maxIndex = len(data)
    s = ''

    while startIndex != maxIndex:
        if data[startIndex : endIndex] in reversedDict:
            s += reversedDict[data[startIndex : endIndex]]
            startIndex = endIndex
        endIndex += 1

    return s

sentencesFile = open("data.txt", "r")
sentences = sentencesFile.readlines()
for number, senctence in enumerate(sentences, 1):
    print("This is test case number {}\n".format(str(number)))
    print("The size of the data is: {}".format(sys.getsizeof(senctence)))
    print("The content of the data is: {}".format(senctence))

    print("Encoding process: ")
    tree, encodedData = huffmanEncodingFunc(senctence)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encodedData, base=2))))
    print("The content of the encoded data is: {}".format(encodedData))
    print("\nDecoding process: ")
    decodedData = huffmanDecodingFunc(encodedData, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decodedData)))
    print("The content of the encoded data is: {}".format(decodedData))

sentencesFile.close()
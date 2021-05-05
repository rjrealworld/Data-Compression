from collections import defaultdict
import operator
import sys

class Node:
	def __init__(self, symbol, frequency, left = None, right = None):
		self.symbol = symbol
		self.frequency = frequency
		self.left = left
		self.right = right
		self.huffman = ''

def getCodes(node: Node, val = "", codes = defaultdict(int)) -> {str: str} :
    newVal = val + str(node.huffman)
    if(node.left):
        getCodes(node.left, newVal, codes)
    if(node.right):
        getCodes(node.right, newVal, codes)
    if(not node.left and not node.right):
        codes[node.symbol] = newVal
    return dict(codes)

def freqCounter(s: str) -> [(str, int)] :
    frequency = defaultdict(int)
    for i in s:
        frequency[i] += 1
    return sorted(frequency.items(), key = operator.itemgetter(1))

def charAndFreq(freqList: [(str, int)]) -> ([str], [int]):
    chars = [i[0] for i in freqList]
    freqs = [i[1] for i in freqList]
    return chars, freqs

def probabiltyCounter(freq: [(str, int)], totalElements: int) -> [int] :
    probability = {}
    for i in freq:
        probability[i[0]] = i[1] / totalElements
    return probability

def avgLengthOutput(probability: {str: int}, codes: {str: str}) -> int : 
    avgLen = 0
    for i in probability:
        avgLen += probability[i] * len(codes[i])
    return avgLen

if __name__ == "__main__":
    input = "she sells sea shells"
    n = len(input)
    frequencyList = freqCounter(input)
    chars, freq = charAndFreq(frequencyList)
    probability = probabiltyCounter(frequencyList, n)
    nodes = []

    for x in range(len(chars)):
        nodes.append(Node(chars[x], freq[x]))

    while len(nodes) > 1:
        nodes = sorted(nodes, key = lambda x : x.frequency)
        left = nodes[0]
        right = nodes[1]
        left.huffman = 0
        right.huffman = 1
        newNode = Node(left.symbol + right.symbol, left.frequency + right.frequency, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    codes = getCodes(nodes[0])
    output = ''
    for i in input:
        output += codes[i]

    print ("Input message is : ", input)
    print("Probability of symbols are : ", probability)
    print()
    print("Codes are : ", codes)
    print ("Encoded message is : ", output)
    print ("Average length after encoding : ", avgLengthOutput(probability, codes))
    print("The size of the input message is : ", sys.getsizeof(input))
    print("The size of the encoded message is : ", sys.getsizeof(int(output, base = 2)))
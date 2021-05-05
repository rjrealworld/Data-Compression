from functools import total_ordering
from math import log2
from collections import defaultdict
import operator
import sys

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

@total_ordering
class Char:
    def __init__(self, name, freq) -> None:
        self._name = name
        self._freq = freq
        self._code = ""

    def __lt__(self, other):
        return True if self._freq < other.get_freq() else False

    def __eq__(self, other):
        return True if self._name == other.get_name() and self._freq == other.get_freq() else False

    def __str__(self):
        return "{0}\t {1}\t {2}".format(self._name, str(self._freq), self._code)

    def __iter__(self):
        return self

    def get_name(self):
        return self._name

    def get_freq(self):
        return self._freq

    def get_code(self):
        return self._code

    def append_code(self, code):
        self._code += str(code)


def findMid(lst, chars):
    if len(chars) == 1: return None
    s = k = b = 0
    for p in chars: s += lst[p]
    s /= 2
    for p in range(len(chars)):
        k += lst[chars[p]]
        if k == s: 
            return p
        elif k > s:
            j = len(chars) - 1
            while b < s:
                b += lst[chars[j]]
                j -= 1
            if abs(s - k) < abs(s - b):
                return p 
            return j
    return None


def shannonFano(lst, chars, codes):
    middle = findMid(lst, chars)
    if middle is None: 
        return codes
    for i in chars[: middle + 1]:
        codes[i] += "0"
    shannonFano(lst, chars[: middle + 1], codes)
    for i in chars[middle + 1:]:
        codes[i] += "1"
    shannonFano(lst, chars[middle + 1:], codes)

if __name__ == "__main__":
    input = "she sells sea shells"
    n = len(input)
    frequencyList = freqCounter(input)
    chars, freq = charAndFreq(frequencyList)
    print(chars, freq)
    probability = probabiltyCounter(frequencyList, n)

    codes = defaultdict(str)
    shannonFano(probability, chars, codes)
    codes = dict(codes)

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
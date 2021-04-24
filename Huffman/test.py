import sys
from huffmanEncodingAndDecoding import huffmanEncodingFunc, huffmanDecodingFunc

sentencesFile = open("data.txt", "r")
sentences = sentencesFile.readlines()
for number, senctence in enumerate(sentences, 1):
    print("This is test case number {}\n".format(str(number)))
    print("Encoding process: ")
    print("The size of the data is: {}".format(sys.getsizeof(senctence)))
    print("The content of the data is: {}".format(senctence))

    print("Decoding process: ")
    tree, encodedData = huffmanEncodingFunc(senctence)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encodedData, base=2))))
    print("The content of the encoded data is: {}".format(encodedData))
    decodedData = huffmanDecodingFunc(encodedData, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decodedData)))
    print("The content of the encoded data is: {}".format(decodedData))

sentencesFile.close()
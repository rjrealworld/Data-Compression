import sys

def LZWCompression(uncompressed):
    #LZW Compression on a string
 
    # Building the dictionary
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
 
    p = ""
    result = [] #output symbols after compression
    for c in uncompressed:
        pc = p + c
        if pc in dictionary:
            p = pc
        else:
            result.append(dictionary[p])
            # Add pc to the dictionary
            dictionary[pc] = dict_size
            dict_size += 1
            p = c
    #print(dictionary) 
    # Output the code for p
    if p:
        result.append(dictionary[p])
    return result

if __name__ == "__main__":
    input = "she sells sea shells"

    compressed = LZWCompression(input)

    output = ""
    for i in compressed:
        output += str(i)
    
    print ("Input message is : ", input)        
    print ("Encoded message is : ", output)
    print("The size of the input message is : ", sys.getsizeof(input))
    print("The size of the encoded message is : ", sys.getsizeof(int(output,base = 2)))

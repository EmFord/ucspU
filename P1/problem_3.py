import sys
from typing import ForwardRef


class Node():

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children_nodes(self):
        return (self.left, self.right)

    def parent_node(self):
        return (self.left, self.right)


def huffman_encoding(data):
    # Phase 1: build the huffman tree

    if data is None or data == "":
        return None, None

    #1
    frequencies = {}
    for char in data:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    #2
    frequencies = sorted(frequencies.items(), key=lambda x:x[1])
    if len(frequencies) > 1:
        #3
        i = 0
        while i <= len(frequencies):
            min_frq_1 = frequencies.pop(i)
            min_frq_1_num = list(min_frq_1)[1]
            min_frq_2 = frequencies.pop(i)
            min_frq_2_num = list(min_frq_2)[1]

            #4
            internal_node = Node(min_frq_1_num + min_frq_2_num)
            internal_node.left = min_frq_1
            internal_node.right = min_frq_2

            frequencies[i] = internal_node

            i += 1
            if i >= len(frequencies):
                break
    else:
        min_frq_1 = frequencies.pop(0)
        min_frq_1_num = list(min_frq_1)[1]
        internal_node = Node(min_frq_1)
        frequencies = [internal_node]

    # Phase 2: generate encoded data

    code = ""
    for i in frequencies:
        if i.left:
            code += "0"
        if i.right:
            code += "1"

    return code, frequencies


def huffman_decoding(data, tree):
    if data is None or tree is None:
        return -1

    decoded = ""
    
    for i in data:
        for t in tree:
            if i == "0":
                decoded += list(t.left)[0]
            if i == "1":
                decoded += list(t.right)[0]
    return decoded


if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(encoded_data, tree)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 1

    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(encoded_data, tree)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 2

    a_great_sentence = "AAAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(encoded_data, tree)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
import heapq
from collections import Counter

class Node: 
    def __init__(self, frequencia, simbolo, esquerda=None, direita=None): 
        self.frequencia = frequencia
        self.simbolo = simbolo 
        self.esquerda = esquerda
        self.direita = direita
        self.peso = '' 

    def __lt__(self, nxt): 
        return self.frequencia < nxt.frequencia 

    def __repr__(self):
        return f"Node(simbolo='{self.simbolo}', frequencia={self.frequencia})"

class Huffman:
    def HuffmanEncoder(self, mensagem):
        print(f"Original Message: {mensagem}")
        
        charsArray, freqChars = counterOfChars(mensagem)
        print("\nCharacter Frequencies:")
        for char, freq in zip(charsArray, freqChars):
            print(f"Character: '{char}' Frequency: {freq}")

        nodes = []
        print("\nInitializing heap with nodes:")
        for i in range(len(charsArray)):
            node = Node(freqChars[i], charsArray[i])
            heapq.heappush(nodes, node)
            print(f"Pushed to heap: {node}")

        print("\nBuilding the Huffman tree:")
        while len(nodes) > 1:
            no1 = heapq.heappop(nodes)  # Pop the two nodes with the smallest frequencies
            no2 = heapq.heappop(nodes)

            # Assign nodes to left and right
            noEsquerda = no1
            noDireita = no2

            # Combine nodes
            novoNo = Node(noEsquerda.frequencia + noDireita.frequencia, noEsquerda.simbolo + noDireita.simbolo, noEsquerda, noDireita)
            heapq.heappush(nodes, novoNo)
            print(f"Combined nodes: {noEsquerda.simbolo} and {noDireita.simbolo}, new node: {novoNo.simbolo} with freq: {novoNo.frequencia}")

        # The remaining node is the root of the Huffman tree
        raiz = nodes[0]
        print(f"\nFinal Huffman Tree Root: {raiz}")

        # Generate Huffman codes
        huffmanCode = {}
        print("\nGenerating Huffman Codes:")
        self.gerarCodigo(raiz, '', huffmanCode)
        for char in huffmanCode:
            print(f"Character: '{char}' Code: {huffmanCode[char]}")

        # Display the Huffman Tree with 0s and 1s
        print("\nDisplaying Huffman Tree:")
        self.printStyledTree(raiz, "", True)

        # Encode the message
        encodedMessage = ''.join([huffmanCode[char] for char in mensagem])
        print(f"\nEncoded Message: {encodedMessage}")

        return encodedMessage, raiz

    def gerarCodigo(self, node, currentCode, huffmanCode):
        # If it's a leaf node, assign the code
        if not node.esquerda and not node.direita:
            huffmanCode[node.simbolo] = currentCode or '0'
            return

        # Traverse left
        if node.esquerda:
            self.gerarCodigo(node.esquerda, currentCode + '0', huffmanCode)
        
        # Traverse right
        if node.direita:
            self.gerarCodigo(node.direita, currentCode + '1', huffmanCode)

    def printStyledTree(self, node, indent="", last=True):
        if node is not None:
            # Draw the tree with frequency and symbol for each node
            if last:
                print(indent + "└── ", end="")
                indent += "    "
            else:
                print(indent + "├── ", end="")
                indent += "│   "

            if node.simbolo and len(node.simbolo) == 1:  # Leaf node
                print(f"Symbol: '{node.simbolo}', Freq: {node.frequencia}")
            else:
                print(f"Freq: {node.frequencia}")

            # Traverse left and right children
            self.printStyledTree(node.esquerda, indent, False)
            self.printStyledTree(node.direita, indent, True)

    def HuffmanDecoder(self, encodedMessage, raiz):
        decodedMessage = ''
        currentNode = raiz

        for bit in encodedMessage:
            if bit == '0':
                currentNode = currentNode.esquerda
            else:
                currentNode = currentNode.direita

            if not currentNode.esquerda and not currentNode.direita:
                decodedMessage += currentNode.simbolo
                currentNode = raiz  # Return to the root to decode the next character

        return decodedMessage

def counterOfChars(mensagem):
    freq_dict = Counter(mensagem)
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1])
    chars, freq = zip(*sorted_freq)
    return list(chars), list(freq)

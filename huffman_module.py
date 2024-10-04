import heapq
from collections import Counter

class Node: 
    def __init__(self, frequencia, simbolo, esquerda=None, direita=None): 
        # Frequency of symbol 
        self.frequencia = frequencia 

        # Symbol name (character). For internal nodes, this can be None or a combined string
        self.simbolo = simbolo 

        # Node left of current node 
        self.esquerda = esquerda 

        # Node right of current node 
        self.direita = direita 

        # Tree direction (0/1) 
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

        # Initialize the heap with leaf nodes
        print("\nInitializing heap with nodes:")
        for i in range(len(charsArray)):
            node = Node(freqChars[i], charsArray[i])
            heapq.heappush(nodes, node)
            print(f"Pushed to heap: {node}")
        print("\nHeap after initialization:")
        print(nodes)

        isFirstTimeRunning = True

        # Build the Huffman tree
        print("\nBuilding the Huffman tree:")
        while len(nodes) > 1:
            no1 = heapq.heappop(nodes)
            no2 = heapq.heappop(nodes)

            if(isFirstTimeRunning):
                if no1.frequencia > no2.frequencia:
                    noEsquerda = no1
                    noDireita = no2
                else:
                    noEsquerda = no2
                    noDireita = no1
                isFirstTimeRunning = False
            else:
                noEsquerda = no1
                noDireita = no2

            print(f"\nPopped from heap: Left Node: {noEsquerda}, Right Node: {noDireita}")

            # Assign weights based on direction
            noEsquerda.peso = '0'
            noDireita.peso = '1'
            print(f"Assigned peso '0' to {noEsquerda.simbolo} and '1' to {noDireita.simbolo}")

            # Combine nodes
            novoNo = Node(noEsquerda.frequencia + noDireita.frequencia, noEsquerda.simbolo + noDireita.simbolo, noEsquerda, noDireita)
            heapq.heappush(nodes, novoNo)
            print(f"Created new node: {novoNo} and pushed to heap")
            print(f"Current heap: {nodes}")

        # The remaining node is the root of the Huffman tree
        raiz = nodes[0]
        print(f"\nFinal Huffman Tree Root: {raiz}")

        # Generate Huffman codes
        huffmanCode = {}
        print("\nGenerating Huffman Codes:")
        self.gerarCodigo(raiz, '', huffmanCode)
        for char in huffmanCode:
            print(f"Character: '{char}' Code: {huffmanCode[char]}")

        # Encode the message
        encodedMessage = ''.join([huffmanCode[char] for char in mensagem])
        print(f"\nEncoded Message: {encodedMessage}")

        return encodedMessage, raiz

    def gerarCodigo(self, node, currentCode, huffmanCode):
        # If it's a leaf node, assign the code
        if not node.esquerda and not node.direita:
            huffmanCode[node.simbolo] = currentCode or '0'  # Assign '0' if tree has only one character
            return

        # Traverse left
        if node.esquerda:
            self.gerarCodigo(node.esquerda, currentCode + '0', huffmanCode)
        
        # Traverse right
        if node.direita:
            self.gerarCodigo(node.direita, currentCode + '1', huffmanCode)

    def HuffmanDecoder(self, encodedMessage, raiz):
        decodedMessage = ''
        currentNode = raiz

        for bit in encodedMessage:
            if bit == '0':
                currentNode = currentNode.esquerda
            else:
                currentNode = currentNode.direita
            
            # Se estivermos em uma folha, adicionamos o caractere à mensagem decodificada
            if not currentNode.esquerda and not currentNode.direita:
                decodedMessage += currentNode.simbolo
                currentNode = raiz  # Retorna para a raiz para decodificar o próximo caractere

        return decodedMessage

def counterOfChars(mensagem):
    freq_dict = Counter(mensagem)
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1])
    chars, freq = zip(*sorted_freq)
    return list(chars), list(freq)

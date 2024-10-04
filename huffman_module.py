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

class Huffman:
    def HuffmanEncoder(self, mensagem):
        
        charsArray, freqChars = counterOfChars(mensagem)

        nodes = []

        for i in range(len(charsArray)):
            node = Node(freqChars[i], charsArray[i])
            heapq.heappush(nodes, node)

        while len(nodes) > 1:
            noEsquerda = heapq.heappop(nodes)  # Pop the two nodes with the smallest frequencies
            noDireita = heapq.heappop(nodes)

            # Combine nodes
            novoNo = Node(noEsquerda.frequencia + noDireita.frequencia, noEsquerda.simbolo + noDireita.simbolo, noEsquerda, noDireita)
            heapq.heappush(nodes, novoNo)

        # The remaining node is the root of the Huffman tree
        raiz = nodes[0]

        huffmanCode = {}
        self.gerarCodigo(raiz, '', huffmanCode)

        encodedMessage = ''.join([huffmanCode[char] for char in mensagem])

        return encodedMessage, raiz

    def gerarCodigo(self, node, currentCode, huffmanCode):
        if not node.esquerda and not node.direita:
            huffmanCode[node.simbolo] = currentCode or '0'
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

            if not currentNode.esquerda and not currentNode.direita:
                decodedMessage += currentNode.simbolo
                currentNode = raiz  # Return to the root to decode the next character

        return decodedMessage

def counterOfChars(mensagem):
    freq_dict = Counter(mensagem)
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1])
    chars, freq = zip(*sorted_freq)
    return list(chars), list(freq)

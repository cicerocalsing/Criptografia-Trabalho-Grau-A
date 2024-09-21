import heapq
from collections import Counter

class Node: 
    def __init__(self, frequencia, simbolo, esquerda=None, direita=None): 
        # frequency of symbol 
        self.frequencia = frequencia 
  
        # symbol name (character) 
        self.simbolo = simbolo 
  
        # node left of current node 
        self.esquerda = esquerda 
  
        # node right of current node 
        self.direita = direita 
  
        # tree direction (0/1) 
        self.peso = '' 
  
    def __lt__(self, nxt): 
        return self.frequencia < nxt.frequencia 

class Huffman:
    def HuffmanEncoder(self, mensagem):
        charsArray, freqChars = counterOfChars(mensagem)
        nodes = []

        # aqui vamos colocar todos os nos para dentro do heap, com sua respectiva frequencia na palavra que queremos codificar
        for i in range(len(charsArray)):
            heapq.heappush(nodes, Node(freqChars[i], charsArray[i]))

        # agora precisamos ajustar essa arvore/heap baseando-se na frequencia de cada letra na palavra
        # enquanto a lista de nos tiver algo, precisamos trabalhar
        # ao final deste while, teremos diversos nos (objetos) interligados atraves dos rights and lefts de cada objeto
        while len(nodes) > 1:
            # vamos buscar a menor frequencia (atraves da funcao __lt__ que definimos na classe)
            noEsquerda = heapq.heappop(nodes)
            noDireita = heapq.heappop(nodes)
            
            # baseando-se na regra de que esquerda sempre terá caminho 0 e direita caminho 1, vamos assignar esses valores para os nos que pegamos acima
            noEsquerda.peso = '0'
            noDireita.peso = '1'

            # agora vamos combinar os 2 nos para formar um novo node como pai destes e adicionar no array de nós que temos
            novoNo = Node(noEsquerda.frequencia + noDireita.frequencia, noEsquerda.simbolo + noDireita.simbolo, noEsquerda, noDireita)
            heapq.heappush(nodes, novoNo)
        
        # Geração dos códigos de Huffman para cada caractere
        raiz = nodes[0]
        huffmanCode = {}
        self.gerarCodigo(raiz, '', huffmanCode)

        # Codificação da mensagem original usando os códigos gerados
        encodedMessage = ''.join([huffmanCode[char] for char in mensagem])
        
        return encodedMessage, raiz
    
    def gerarCodigo(self, node, currentCode, huffmanCode):
        # Se não houver filhos, estamos em uma folha
        if not node.esquerda and not node.direita:
            huffmanCode[node.simbolo] = currentCode
            return
        
        # Recursão para esquerda e direita da árvore
        if node.esquerda:
            self.gerarCodigo(node.esquerda, currentCode + '0', huffmanCode)
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

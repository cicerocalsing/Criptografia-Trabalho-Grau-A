import heapq
from collections import Counter

class node: 
    def __init__(self, freq, symbol, left=None, right=None): 
        # frequency of symbol 
        self.freq = freq 
  
        # symbol name (character) 
        self.symbol = symbol 
  
        # node left of current node 
        self.left = left 
  
        # node right of current node 
        self.right = right 
  
        # tree direction (0/1) 
        self.weight = '' 
  
    def __lt__(self, nxt): 
        return self.freq < nxt.freq 

class Huffman():
    def HuffmanEncoder(self, mensagem):
        nodes = [] #nodes nao usados
        array1, array2 = counterOfChars(mensagem)
        
        for i in range(len(array1)):
            heapq.heappush(nodes, node(array1[i], array2[i])) 
        
        while len(nodes) > 1:
            left = heapq.heappop(nodes) 
            right = heapq.heappop(nodes) 

            left.huff = 0
            right.huff = 1

            newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right) 
            heapq.heappush(nodes, newNode) 

        return "Codifica em Huffman"
    
    def HuffmanDecoder(self, mensagem):
        return "Decodifica em Huffman"
    

def counterOfChars(mensagem):
    freq_dict = Counter(mensagem)
    
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1])
        
    chars, freq = zip(*sorted_freq)
        
    return list(chars), list(freq)
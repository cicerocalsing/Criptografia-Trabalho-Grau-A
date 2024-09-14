import numpy as np

class Golomb():

    def golombEncoder(self, mensagem):
        encodedMensage = ""
        stopBit = "1"
        ascii = []
        ascii = [ord(i) for i in mensagem]
        ascii = [ord(i) for i in mensagem] #criando lista com todos os valores ascii da mensagem
        k = int(np.mean(ascii) * 0.2) # escolhendo k como 20% da média, ex: se os números da lista forem [10,10] o k será 2
        print(f"O K usado para essa codificação será: {k}")
        for i in ascii:
            if i < k:
                prefixo = ""
            else:
                quantidadeZerosPrefixo = int(i/k) # calculando a quantidade de zeros que terei no meu prefixo, fazendo a divisão do número ascii pelo k
                prefixo = quantidadeZerosPrefixo * "0" # criando string com  a quantidade de zeros
            tamanhoSufixo = int(np.log2(k))
            sufixo = str(bin(int(i%k))[2:]) # pegando o resto da divisão do número ascii por k e transformando ele em binário com a função bin. o [2:] é pq essa função deixa o prefixo "0b" antes de todas as transformações, por isso coloco [2:] para tirar o prefixo. Por fim, uso  a função str para transformar em string
            if len(sufixo) < tamanhoSufixo:
                while len(sufixo) < tamanhoSufixo:
                    sufixo = "0" + sufixo
            mensagemParcial = prefixo + stopBit + sufixo
            encodedMensage += mensagemParcial

        return encodedMensage
    
    def golombDecoder(self, mensagem):
        return "Decodifica em golomb"

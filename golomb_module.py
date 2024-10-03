import numpy as np

class Golomb():

    def escolherK(self, ascii_list):
        # Calcula a média dos valores ASCII da mensagem
        media_ascii = np.mean(ascii_list)
        # Escolhe k como a potência de 2 mais próxima da média ASCII
        k = 2 ** int(np.log2(media_ascii))
        return k

    def golombEncoder(self, mensagem):
        encodedMensage = ""
        stopBit = "1"
        ascii = []
        ascii = [ord(i) for i in mensagem] #criando lista com todos os valores ascii da mensagem
        
        k = self.escolherK(ascii) # chamando a função para escolher o k
        for i in ascii:
            if i < k:
                prefixo = ""
            else:
                quantidadeZerosPrefixo = int(i/k) # calculando a quantidade de zeros que terei no meu prefixo, fazendo a divisão do número ascii pelo k
                prefixo = quantidadeZerosPrefixo * "0" # criando string com  a quantidade de zeros
            
            tamanhoSufixo = int(np.log2(k)) #calcula o tamanho do sufixo
            sufixo = str(bin(int(i%k))[2:]) # pegando o resto da divisão do número ascii por k e transformando ele em binário com a função bin. o [2:] é pq essa função deixa o prefixo "0b" antes de todas as transformações, por isso coloco [2:] para tirar o prefixo. Por fim, uso  a função str para transformar em string
            sufixo = sufixo.zfill(tamanhoSufixo) #preenche a string com zeros se ela for menor que o tamanhoSufixo

            mensagemParcial = prefixo + stopBit + sufixo
            encodedMensage += mensagemParcial

        return encodedMensage, k
    
    def golombDecoder(self, mensagemCodificada, k):
        decodedMessage = ""
        tamanhoSufixo = int(np.log2(k))
        i = 0

        while i < len(mensagemCodificada):
            #conta o número de zeros no prefixo
            zerosPrefixo = 0
            while mensagemCodificada[i] == "0":
                zerosPrefixo += 1
                i += 1

            i += 1 #ignora o stopbit

            sufixo = mensagemCodificada[i:i + tamanhoSufixo] #le o sufixo
            i += tamanhoSufixo #adianta o i no while para continuar depois do sufixo
           
            # calcula o valor original
            sufixo_valor = int(sufixo, 2)
            valor_ascii = (zerosPrefixo * k) + sufixo_valor

            # converte de ASCII para caractere
            decodedMessage += chr(valor_ascii)

        return decodedMessage

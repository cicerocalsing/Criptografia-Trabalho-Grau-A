import numpy as np

class EliasGamma():

    def EliasGammaEncoder(self, mensagem):
        encodedMensage = ""
        stopBit = "1"
        ascii = []
        ascii = [ord(simbolo) for simbolo in mensagem] #cria lista ascii

        for simbolo in ascii:
            n = int(np.log2(simbolo)) #maior potencia de 2 menor que que o int
            prefixo = n * "0"

            resto = simbolo - (np.power(2, n)) 
            sufixo = str(bin(resto)[2:]) #transforma o resto em binario

            mensagemParcial = prefixo + stopBit + sufixo #codifica o simbolo
            encodedMensage += mensagemParcial

        return encodedMensage
    
    def EliasGammaDecoder(self, mensagemCodificada):
        decodedMessage = ""
        i = 0

        while i < len(mensagemCodificada):
            #conta o número de zeros no prefixo
            n = 0
            while mensagemCodificada[i] == "0":
                n += 1
                i += 1
                simbolo = np.power(2, n)

            i += 1 #ignora o stopbit
            sufixo = mensagemCodificada[i:i + n] #le o sufixo
            i += n #adianta o i no while para continuar depois do sufixo
           
            sufixo_valor = int(sufixo, 2) #converte de binario pra int
            valor_ascii = simbolo + sufixo_valor #soma potencia de 2

            decodedMessage += chr(valor_ascii) #converte de ascii pra char

        return decodedMessage

            

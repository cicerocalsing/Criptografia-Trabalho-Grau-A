class RepeticaoRi():

    def string_para_binario(self, texto):
        return ' '.join(format(ord(char), '08b') for char in texto)
    
    def triplicar_bits(self, binario):
        # Processa cada bloco de 8 bits separado por espaço
        resultado = []
        for bloco in binario.split():
            # Para cada bit no bloco, triplica o bit (0 -> '000' e 1 -> '111')
            triplicado = ''.join('000' if bit == '0' else '111' for bit in bloco)
            resultado.append(triplicado)
        # Junta os blocos triplicados com um espaço entre cada letra
        return ' '.join(resultado)

    def Encoder(self, mensagem):
        binario = self.string_para_binario(mensagem)
        triplicado = self.triplicar_bits(binario)
        return triplicado


    
    def Decoder(self, mensagem_triplicada):
        # Divide a string triplicada em blocos separados por espaços (cada bloco representa um caractere)
        blocos = mensagem_triplicada.split()
        resultado = []
        
        for bloco in blocos:
            # Divide o bloco de 24 bits em 8 conjuntos de 3 bits cada
            bits = [
                bloco[i:i+3] for i in range(0, 24, 3)
            ]
            # Aplica votação majoritária para reconstruir cada bit
            bit_reconstruido = ''
            for triplo in bits:
                if triplo.count('0') == 2 and triplo.count('1') == 1:
                    print("Erro detectado em:", triplo, "- votação decidiu o resultado como '0'")
                    bit_reconstruido += '0'
                elif triplo.count('1') == 2 and triplo.count('0') == 1:
                    print("Erro detectado em:", triplo, "- votação decidiu o resultado como '1'")
                    bit_reconstruido += '1'
                else:
                    # Caso normal sem erro detectado
                    bit_reconstruido += '0' if triplo.count('0') >= 2 else '1'
            # Converte o byte reconstruído em um caractere ASCII
            caractere = chr(int(bit_reconstruido, 2))
            resultado.append(caractere)
        
        return ''.join(resultado)
        
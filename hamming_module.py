class HammingEncoder:
    def encode_4bit_block(self, data):
        """
        Codifica um bloco de 4 bits em um código Hamming (7,4).
        """
        if len(data) != 4:
            raise ValueError("Somente blocos de 4 bits são suportados para o código Hamming (7,4)")

        # Converte a mensagem de 4 bits em uma lista para facilitar a manipulação
        data = list(map(int, data))
        
        # Cria uma lista de 7 bits com espaços para os bits de paridade e dados
        encoded = [0] * 7

        # Insere os bits de dados nas posições corretas (3, 5, 6 e 7)
        encoded[0] = data[0]
        encoded[1] = data[1]
        encoded[2] = data[2]
        encoded[3] = data[3]

        # Calcula os bits de paridade
        encoded[4] = encoded[0] ^ encoded[1] ^ encoded[2]  # Paridade P1
        encoded[5] = encoded[1] ^ encoded[2] ^ encoded[3]  # Paridade P2
        encoded[6] = encoded[0] ^ encoded[2] ^ encoded[3]  # Paridade P4

        print(encoded)

        return ''.join(map(str, encoded))

    def encode_message(self, mensagem):
        """
        Codifica uma mensagem ASCII usando o código Hamming (7,4) para cada caractere.
        """
        encoded_message = ""
        
        for char in mensagem:
            # Converte o caractere em ASCII binário de 8 bits
            ascii_bin = format(ord(char), '08b')
            print(ascii_bin)
            
            # Divide o byte ASCII de 8 bits em dois blocos de 4 bits
            block1 = ascii_bin[:4]
            block2 = ascii_bin[4:]
            
            # Codifica cada bloco de 4 bits usando Hamming (7,4)
            encoded_block1 = self.encode_4bit_block(block1)
            encoded_block2 = self.encode_4bit_block(block2)
            
            # Adiciona os blocos codificados à mensagem final
            encoded_message += encoded_block1 + encoded_block2

        return encoded_message

# Exemplo de uso
encoder = HammingEncoder()
mensagem = "Hello"  # Mensagem original
encoded_message = encoder.encode_message(mensagem)
print("Mensagem codificada em Hamming:", encoded_message)

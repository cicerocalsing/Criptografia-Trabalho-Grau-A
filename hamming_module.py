class HammingModule:
    def text_to_ascii_bin(self, mensagem):
        """Converte cada caractere da string em ASCII e depois em binário de 8 bits"""
        ascii_bin_list = []
        for char in mensagem:
            ascii_val = ord(char)  # Converte caractere para ASCII
            bin_val = format(ascii_val, '08b')  # Converte ASCII para binário de 8 bits
            ascii_bin_list.append(bin_val)
        return ascii_bin_list

    def calculate_parity_bits(self, bits):
        """Calcula os bits de paridade baseando-se no diagrama de Venn fornecido"""
        t1, t2, t3, t4 = map(int, bits)
        # Cálculo de paridade para cada região do diagrama de Venn
        t5 = t1 ^ t3 ^ t4  # t5 cobre s1, s3, s4
        t6 = t2 ^ t3 ^ t4  # t6 cobre s2, s3, s4
        t7 = t1 ^ t2 ^ t4  # t7 cobre s1, s2, s4
        return f"{t5}{t6}{t7}"

    def encode(self, mensagem):
        """Codifica a string em binário com bits de paridade"""
        encoded_text = []
        ascii_bin_list = self.text_to_ascii_bin(mensagem)

        for bin_val in ascii_bin_list:
            # Divide o binário em blocos de 4 bits
            for i in range(0, 8, 4):
                data_bits = bin_val[i:i+4]
                # Calcula os bits de paridade para o bloco de 4 bits
                parity_bits = self.calculate_parity_bits(data_bits)
                # Concatena os 4 bits de dados com os 3 bits de paridade
                encoded_text.append(data_bits + parity_bits)

        return " ".join(encoded_text)

    def verify_and_correct(self, encoded_bits):
        """Verifica e corrige um erro simples usando o diagrama de Venn"""
        data_bits = encoded_bits[:4]
        parity_bits = encoded_bits[4:]
        calculated_parity = self.calculate_parity_bits(data_bits)

        # Identificar os erros de paridade
        error_position = 0
        for i in range(3):
            if parity_bits[i] != calculated_parity[i]:
                error_position += 2 ** (2 - i)

        # Se error_position é diferente de 0, há um erro no bit correspondente
        if error_position > 0:
            # Corrige o erro invertendo o bit com problema
            encoded_bits = list(encoded_bits)
            encoded_bits[error_position - 1] = '1' if encoded_bits[error_position - 1] == '0' else '0'
            encoded_bits = "".join(encoded_bits)

        # Retorna os 4 bits de dados corrigidos
        return encoded_bits[:4], error_position > 0

    def decode(self, encoded_text):
        """Decodifica a mensagem corrigindo erros e convertendo de volta para ASCII"""
        decoded_text = []
        error_positions = []

        # Divide o texto codificado em blocos de 7 bits
        encoded_blocks = encoded_text.split()

        for encoded_bits in encoded_blocks:
            # Verifica e corrige erros, se necessário
            data_bits, has_error = self.verify_and_correct(encoded_bits)
            if has_error:
                error_positions.append(encoded_bits)

            decoded_text.append(data_bits)

        # Converte cada bloco de 4 bits corrigidos em bytes de 8 bits e depois para ASCII
        ascii_text = ""
        for i in range(0, len(decoded_text), 2):
            byte = decoded_text[i] + decoded_text[i + 1]  # Junta dois blocos de 4 bits
            ascii_char = chr(int(byte, 2))  # Converte para caractere ASCII
            ascii_text += ascii_char

        return ascii_text, error_positions

# Exemplo de uso
text = "Hello"  # Exemplo de entrada
encoder = HammingModule()
encoded_text = encoder.encode(text)
print("Texto codificado com Hamming:", encoded_text)

# Decodificação e correção de erros
decoded_text, errors = encoder.decode(encoded_text)
print("Texto decodificado:", decoded_text)
if errors:
    print("Erros corrigidos nas posições:", errors)
else:
    print("Nenhum erro encontrado.")

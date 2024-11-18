class Hamming:
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
        t5 = t1 ^ t3 ^ t2  # t5 cobre s1, s3, s4
        t6 = t2 ^ t3 ^ t4  # t6 cobre s2, s3, s4
        t7 = t1 ^ t3 ^ t4  # t7 cobre s1, s2, s4
        return f"{t5}{t6}{t7}"

    def HammingEncoder(self, mensagem):
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
        #Verifica e corrige um erro simples usando o diagrama de Venn
        data_bits = list(encoded_bits[:4])
        parity_bits = list(encoded_bits[4:])
        calculated_parity = self.calculate_parity_bits(data_bits)
        calculated_parity = list(calculated_parity)

        #Identifica erros duplos ou superiores
        mismatch_positions = [i for i in range(3) if parity_bits[i] != calculated_parity[i]]
        if len(mismatch_positions) > 1:
            return '', -1

        erro = True 
        
        #Sem erros
        if (parity_bits == calculated_parity):
            erro = False
            return data_bits, erro
        
        #Erro no primeiro bit de paridade
        if (parity_bits[0] != calculated_parity[0]) & (parity_bits[1] == calculated_parity[1]) & (parity_bits[2] == calculated_parity[2]):
            parity_bits[0] = calculated_parity[0]

        #Erro no segundo bit de paridade
        if (parity_bits[0] == calculated_parity[0]) & (parity_bits[1] != calculated_parity[1]) & (parity_bits[2] == calculated_parity[2]):
            parity_bits[1] = calculated_parity[1]
       
       #Erro no terceiro bit de paridade
        if (parity_bits[0] == calculated_parity[0]) & (parity_bits[1] == calculated_parity[1]) & (parity_bits[2] != calculated_parity[2]):
            parity_bits[2] = calculated_parity[2]
       
       #Erro no primeiro bit de dados
        if (parity_bits[0] != calculated_parity[0]) & (parity_bits[1] == calculated_parity[1]) & (parity_bits[2] != calculated_parity[2]):
            if data_bits[0] == '0':
                data_bits[0] = '1'
            else:
                data_bits[0] = '0' 

        #Erro no segundo bit de dados
        if (parity_bits[0] != calculated_parity[0]) & (parity_bits[1] != calculated_parity[1]) & (parity_bits[2] == calculated_parity[2]):
            if data_bits[1] == '0':
                data_bits[1] = '1'
            else:
                data_bits[1] = '0' 

        #Erro no quarto bit
        if (parity_bits[0] == calculated_parity[0]) & (parity_bits[1] != calculated_parity[1]) & (parity_bits[2] != calculated_parity[2]):
            if data_bits[3] == '0':
                data_bits[3] = '1'
            else:
                data_bits[3] = '0' 

        return data_bits, erro

    def HammingDecoder(self, encoded_text):
        """Decodifica a mensagem corrigindo erros e convertendo de volta para ASCII"""
        decoded_text = []

        # Divide o texto codificado em blocos de 7 bits
        encoded_blocks = encoded_text.split()
        mensagemDeErro = ''

        for encoded_bits in encoded_blocks:
            # Verifica e corrige erros, se necessário
            data_bits, erro = self.verify_and_correct(encoded_bits)
            if erro == -1:  # Erro múltiplo identificado
                return "Erro: Erro múltiplo detectado, impossível decodificar a mensagem.", erro

            decoded_text.append(data_bits)

        # Converte cada bloco de 4 bits corrigidos em bytes de 8 bits e depois para ASCII
        ascii_text = ""
        for i in range(0, len(decoded_text), 2):
            #byte = decoded_text[i] + decoded_text[i + 1]  # Junta dois blocos de 4 bits
            byte = ''.join(decoded_text[i] + decoded_text[i + 1])  # Junta dois blocos de 4 bits em uma string
            ascii_char = chr(int(byte, 2))  # Converte para caractere ASCII
            ascii_text += ascii_char

        return ascii_text, erro

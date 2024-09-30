class Fibonacci:

    def sequenciaFibonacci(self, limite):
        # Gera a sequência de Fibonacci até o limite (ex: 255)
        fibonacci = [1, 2]
        primeiroNumero = 1
        segundoNumero = 2
        
        while True:
            soma = primeiroNumero + segundoNumero
            if soma <= limite:
                fibonacci.append(soma)
                primeiroNumero = segundoNumero
                segundoNumero = soma
            else:
                break
            
        return fibonacci

    def FibonacciEncoder(self, mensagem):
        encodedMessage = ""  
        ascii_values = [ord(i) for i in mensagem]  # Converte cada letra da mensagem em seu valor ASCII

        for i in ascii_values:
            encodedWord = [] #Fiz uma lista, pois como a soma é feita de trás para frente, os números tem que ser colocados no início da lista a cada rodada, por isso o insert(0,)
            listaFibonacciLetra = self.sequenciaFibonacci(i)  # Obtém a sequência Fibonacci até o valor i
            soma_restante = i  
            print(listaFibonacciLetra)
            print(i)
            
            # Processa a lista de Fibonacci em ordem decrescente
            for fib in reversed(listaFibonacciLetra):
                if fib <= soma_restante:
                    encodedWord.insert(0,1)  # Adiciona 1 se o número conseguir somar
                    soma_restante -= fib  
                else:
                    encodedWord.insert(0,0)  # Adiciona 0 caso contrário
            
            encodedWord.append(1)  # Adiciona o stopBit (bit de parada)
            print(encodedWord)
            newEncodedWord = ""
            for i in encodedWord:
                newEncodedWord += str(i) # Esse for basicamente pega cada elemento da lista, transforma em string e junta tudo em uma string com a palavra inteira
            encodedMessage += newEncodedWord # Salva o resultado de cada letra à mensagem codificada
        
        return encodedMessage  # Retorna a mensagem codificada sem espaços


    def FibonacciDecoder(self, mensagemCodificada):
        decodedMessage = ""
        listaFibonacci = self.sequenciaFibonacci(255)  # Gera sequência Fibonacci até o limite do valor ASCII (255)
        word = ''
        i = 0

        while i < len(mensagemCodificada):
            soma = 0
            

            # Verifica se o stop bit "11" foi encontrado
            if i > 0 and mensagemCodificada[i] == '1' and mensagemCodificada[i-1] == '1':
                # Remove o último "1" do stop bit e processa o restante da palavra
                #word = word[:-1]
                
                # Decodifica a palavra Fibonacci
                for j in range(len(word)):
                    if word[j] == '1' and j < len(listaFibonacci): #Entra na palavra e onde for 1 ele vai pegar o index equivalente na lista de fibonacci e fazer a soma
                        soma += listaFibonacci[j]
                
                decodedMessage += chr(soma)  # Converte a soma para o caractere ASCII
                word = ''  # Reseta a palavra para o próximo caractere
                if i >= len(mensagemCodificada)-1: #Controla para não exceder o index
                    pass
                else:
                     i += 1
                
            word += mensagemCodificada[i]
            i += 1  # Avança para o próximo bit
        
        return decodedMessage

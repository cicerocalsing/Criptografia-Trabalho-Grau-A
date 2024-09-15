from eliasgamma_module import EliasGamma
from fibonacci_module import Fibonacci
from golomb_module import Golomb
from huffman_module import Huffman

#Funções
def menu():
    print("--------------------------------------------------\n")
    print("BEM VINDO AO CODIFICADOR\n")
    print("DIGITE O NÚMERO CORRESPONDENTE A OPÇÃO DESEJADA\n")
    opcao = int(input("1- CODIFICAR MENDAGEM EM GOLOMB\n2- CODIFICAR MENSAGEM EM ELIAS-GAMMA\n3- CODIFICAR MENSAGEM EM FIBONACCI\n4- CODIFICAR MENSAGEM EM HUFFMAN\n5- SAIR\n\nOPÇÃO DESEJADA:"))
    print("--------------------------------------------------")
    
    return opcao

def opcoes(golomb, EliasGamma,Fibonacci, Huffman, opcao):
    if opcao == 1:
        # Codificação Golomb
        mensagem = input("\nDigite a mensagem que você gostaria de codificar em Golomb: ")
        golombMensage, k = golomb.golombEncoder(mensagem)
        print(f"Mensagem codificada: {golombMensage}")
        
        while True:
            escolha = int(input("\n\nDIGITE O NÚMERO CORRESPONDENTE A OPÇÃO DESEJADA:\n1- DECODIFICAR MENSAGEM\n2- VOLTAR PARA O MENU\n"))
            if escolha == 1:
                golombDecodedMensage = golomb.golombDecoder(golombMensage, k)
                print(f"Mensagem decodificada: {golombDecodedMensage}")
            elif escolha == 2:
                return True  # Voltar ao menu principal
            else:
                print("Opção inválida. Tente novamente.")
    elif opcao == 2:
        #Codificação Elias-gamma
        mensagem = input("\nDigite a mensagem que você gostaria de codificar em Elias-Gamma: ")
        eliasGammaMensage = EliasGamma.EliasGammaEncoder(mensagem)
        return eliasGammaMensage
    elif opcao == 3:
        #Codificação Fibonacci/Zeckendorf
        mensagem = input("\nDigite a mensagem que você gostaria de codificar em Fibonacci: ")
        fibonacciMensage = Fibonacci.FibonacciEncoder(mensagem)
        return fibonacciMensage
    elif opcao == 4:
        #codificação de Huffman
        mensagem = input("\nDigite a mensagem que você gostaria de codificar em Huffman: ")
        huffmanMensage = Huffman.HuffmanEncoder(mensagem)
        return huffmanMensage
    elif opcao == 5:
        exit = False
        print("\nOBRIGADO PELA PREFERÊNCIA!\n")
        return exit
    else:
        #erro
        return -1

eliasgamma = EliasGamma()
fibonacci = Fibonacci()
golomb = Golomb()
huffman = Huffman()



exit=True
while(exit):
    opcao = menu()
    exit = opcoes(golomb, eliasgamma, fibonacci, huffman, opcao)


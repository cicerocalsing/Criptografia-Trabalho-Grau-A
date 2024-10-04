import tkinter as tk
from tkinter import messagebox
from eliasgamma_module import EliasGamma
from fibonacci_module import Fibonacci
from golomb_module import Golomb
from huffman_module import Huffman

# Create instances of the encoding classes
golomb = Golomb()
elias = EliasGamma()
huff = Huffman()
fibo = Fibonacci()

# Global variables to store the encoded message and required info for decoding
encoded_message = ""
current_algorithm = None
golomb_k = None
huffman_root = None

# Function for encoding/decoding and updating history
def executar_opcao(algoritmo, acao):
    global encoded_message, current_algorithm, golomb_k, huffman_root

    mensagem = entrada_mensagem.get().strip()

    if not mensagem:
        messagebox.showerror("Erro", "Por favor, digite uma mensagem.")
        return

    resultado_codificado = ""
    resultado_decodificado = ""

    # Initialize k if needed
    k = None
    if algoritmo == "Golomb" and acao == "decodificar":
        k_str = entrada_k.get().strip()
        if not k_str:
            messagebox.showerror("Erro", "Por favor, forneça o valor de k para decodificação.")
            return
        try:
            k = int(k_str)
            if k <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "O valor de k deve ser um número inteiro positivo.")
            return

    # Check the action: encoding or decoding
    if acao == "codificar":

        # Encode the message using the selected algorithm
        if algoritmo == "Golomb":
            resultado_codificado, golomb_k = golomb.golombEncoder(mensagem)
        elif algoritmo == "Elias-Gamma":
            resultado_codificado = elias.EliasGammaEncoder(mensagem)
        elif algoritmo == "Fibonacci":
            resultado_codificado = fibo.FibonacciEncoder(mensagem)
        elif algoritmo == "Huffman":
            resultado_codificado, huffman_root = huff.HuffmanEncoder(mensagem)

        # Store the encoded message and algorithm for later decoding
        encoded_message = resultado_codificado

        # Update history with encoded message and k if Golomb
        if algoritmo == "Golomb":
            historico.append(f"Codificado ({algoritmo}, k={golomb_k}): {resultado_codificado}")
        else:
            historico.append(f"Codificado ({algoritmo}): {resultado_codificado}")

    elif acao == "decodificar":

        # Check if Huffman root exists for Huffman decoding
        if algoritmo == "Huffman" and not huffman_root:
            messagebox.showerror("Erro", "Você deve codificar com Huffman antes de decodificar.")
            return
    
        # Decode the message using the stored algorithm-specific data
        if algoritmo == "Golomb":
            resultado_decodificado = golomb.golombDecoder(mensagem, k)
        elif algoritmo == "Elias-Gamma":
            resultado_decodificado = elias.EliasGammaDecoder(mensagem)
        elif algoritmo == "Fibonacci":
            resultado_decodificado = fibo.FibonacciDecoder(mensagem)
        elif algoritmo == "Huffman":
            resultado_decodificado = huff.HuffmanDecoder(mensagem, huffman_root)

        historico.append(f"Decodificado ({algoritmo}): {resultado_decodificado}")

        # Reset after decoding
        encoded_message = ""
        golomb_k = None
        huffman_root = None

    # Update the history in the interface
    historico_texto.config(state=tk.NORMAL)
    historico_texto.delete(1.0, tk.END)
    for entrada in historico:
        historico_texto.insert(tk.END, entrada + "\n")
    historico_texto.config(state=tk.DISABLED)

# Function to update the state of k_entry based on algorithm and action
def atualizar_interface(*args):
    algoritmo = algoritmo_var.get()
    acao = acao_var.get()

    if algoritmo == "Golomb" and acao == "decodificar":
        entrada_k_label.config(state=tk.NORMAL)
        entrada_k.config(state=tk.NORMAL)
    else:
        entrada_k_label.config(state=tk.DISABLED)
        entrada_k.delete(0, tk.END)
        entrada_k.config(state=tk.DISABLED)

# Create the Tkinter interface
janela = tk.Tk()
janela.title("Codificador e Decodificador")

# Message entry field
entrada_label = tk.Label(janela, text="Digite sua mensagem:")
entrada_label.pack(pady=(10, 0))

entrada_mensagem = tk.Entry(janela, width=50)
entrada_mensagem.pack(pady=(0, 10))

# Buttons to choose the algorithm and action
algoritmo_var = tk.StringVar(value="Golomb")
algoritmo_menu = tk.OptionMenu(janela, algoritmo_var, "Golomb", "Elias-Gamma", "Fibonacci", "Huffman")
algoritmo_menu.pack()

acao_var = tk.StringVar(value="codificar")
acao_menu = tk.OptionMenu(janela, acao_var, "codificar", "decodificar")
acao_menu.pack(pady=(5, 10))

# Label and entry for k (initially disabled)
entrada_k_label = tk.Label(janela, text="Digite o valor de k:")
entrada_k_label.pack()
entrada_k = tk.Entry(janela, width=20, state=tk.DISABLED)
entrada_k.pack(pady=(0, 10))

# Execute button
executar_button = tk.Button(janela, text="Executar", command=lambda: executar_opcao(algoritmo_var.get(), acao_var.get()))
executar_button.pack()

# Widget to display history
historico_label = tk.Label(janela, text="Histórico:")
historico_label.pack(pady=(10, 0))
historico_texto = tk.Text(janela, wrap=tk.WORD, height=10, width=50, state=tk.DISABLED)
historico_texto.pack(pady=(0, 10))

# List to store history
historico = []

# Bind the update function to changes in algorithm and action
algoritmo_var.trace_add('write', atualizar_interface)
acao_var.trace_add('write', atualizar_interface)

# Initialize the interface loop
janela.mainloop()

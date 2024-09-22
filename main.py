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

# Function to copy text to the clipboard
def copiar_para_clipboard(text):
    janela.clipboard_clear()
    janela.clipboard_append(text)
    messagebox.showinfo("Copiado!", "Mensagem copiada para a área de transferência.")

# Function for encoding/decoding and updating history
def executar_opcao(algoritmo, acao):
    global encoded_message, current_algorithm, golomb_k, huffman_root

    mensagem = entrada_mensagem.get().strip()

    if not mensagem:
        messagebox.showerror("Erro", "Por favor, digite uma mensagem.")
        return

    resultado_codificado = ""
    resultado_decodificado = ""

    # Check the action: encoding or decoding
    if acao == "codificar":
        # Ensure the user is only allowed to decode after encoding
        if current_algorithm:
            messagebox.showerror("Erro", "Você precisa decodificar a mensagem antes de codificar uma nova.")
            return

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
        current_algorithm = algoritmo

        historico.append(f"Codificado ({algoritmo}): {resultado_codificado}")
        copiar_button.config(command=lambda: copiar_para_clipboard(resultado_codificado))

    elif acao == "decodificar":
        # Ensure the user decodes using the same algorithm
        if current_algorithm is None:
            messagebox.showerror("Erro", "Nenhuma mensagem foi codificada.")
            return
        if algoritmo != current_algorithm:
            messagebox.showerror("Erro", f"Você precisa decodificar com o algoritmo {current_algorithm}.")
            return

        # Decode the message using the stored algorithm-specific data
        if current_algorithm == "Golomb":
            resultado_decodificado = golomb.golombDecoder(mensagem, golomb_k)
        elif current_algorithm == "Elias-Gamma":
            resultado_decodificado = elias.EliasGammaDecoder(mensagem)
        elif current_algorithm == "Fibonacci":
            resultado_decodificado = fibo.FibonacciDecoder(mensagem)
        elif current_algorithm == "Huffman":
            resultado_decodificado = huff.HuffmanDecoder(mensagem, huffman_root)

        historico.append(f"Decodificado ({algoritmo}): {resultado_decodificado}")

        # Reset after decoding
        encoded_message = ""
        current_algorithm = None
        golomb_k = None
        huffman_root = None

    # Update the history in the interface
    historico_texto.config(state=tk.NORMAL)
    historico_texto.delete(1.0, tk.END)
    for entrada in historico:
        historico_texto.insert(tk.END, entrada + "\n")
    historico_texto.config(state=tk.DISABLED)

# Create the Tkinter interface
janela = tk.Tk()
janela.title("Codificador e Decodificador")

# Message entry field
entrada_label = tk.Label(janela, text="Digite sua mensagem:")
entrada_label.pack()

entrada_mensagem = tk.Entry(janela, width=50)
entrada_mensagem.pack()

# Buttons to choose the algorithm and action
algoritmo_var = tk.StringVar(value="Golomb")
algoritmo_menu = tk.OptionMenu(janela, algoritmo_var, "Golomb", "Elias-Gamma", "Fibonacci", "Huffman")
algoritmo_menu.pack()

acao_var = tk.StringVar(value="codificar")
acao_menu = tk.OptionMenu(janela, acao_var, "codificar", "decodificar")
acao_menu.pack()

# Execute button
executar_button = tk.Button(janela, text="Executar", command=lambda: executar_opcao(algoritmo_var.get(), acao_var.get()))
executar_button.pack()

# Button to copy results
copiar_button = tk.Button(janela, text="Copiar", state=tk.NORMAL)
copiar_button.pack()

# Widget to display history
historico_label = tk.Label(janela, text="Histórico:")
historico_label.pack()
historico_texto = tk.Text(janela, wrap=tk.WORD, height=10, width=50, state=tk.DISABLED)
historico_texto.pack()

# List to store history
historico = []

# Initialize the interface loop
janela.mainloop()

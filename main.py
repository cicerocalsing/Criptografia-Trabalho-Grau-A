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

# Function to copy text to the clipboard
def copiar_para_clipboard(text):
    janela.clipboard_clear()
    janela.clipboard_append(text)
    messagebox.showinfo("Copiado!", "Mensagem copiada para a área de transferência.")

# Function for encoding/decoding and updating history
def executar_opcao(algoritmo, acao):
    mensagem = entrada_mensagem.get().strip()
    k = k_entry.get().strip() if algoritmo == "Golomb" else None

    if not mensagem:
        messagebox.showerror("Erro", "Por favor, digite uma mensagem.")
        return
    if algoritmo == "Golomb" and (not k or not k.isdigit()):
        messagebox.showerror("Erro", "Por favor, insira um número válido para K.")
        return

    k = int(k) if k else None
    resultado_codificado = ""
    resultado_decodificado = ""

    if acao == "codificar":
        if algoritmo == "Golomb" and k is not None:
            resultado_codificado = golomb.golombEncoder(mensagem, k)
        elif algoritmo == "Elias-Gamma":
            resultado_codificado = elias.EliasGammaEncoder(mensagem)
        elif algoritmo == "Fibonacci":
            resultado_codificado = fibo.FibonacciEncoder(mensagem)
        elif algoritmo == "Huffman":
            resultado_codificado, _ = huff.HuffmanEncoder(mensagem)

        historico.append(f"Codificado ({algoritmo}): {resultado_codificado}")
        copiar_button.config(command=lambda: copiar_para_clipboard(resultado_codificado))

    elif acao == "decodificar":
        if algoritmo == "Golomb" and k is not None:
            resultado_decodificado = golomb.golombDecoder(mensagem, k)
        elif algoritmo == "Elias-Gamma":
            resultado_decodificado = elias.EliasGammaDecoder(mensagem)
        elif algoritmo == "Fibonacci":
            resultado_decodificado = fibo.FibonacciDecoder(mensagem)
        elif algoritmo == "Huffman":
            _, raiz = huff.HuffmanEncoder(mensagem)
            resultado_decodificado = huff.HuffmanDecoder(mensagem, raiz)

        historico.append(f"Decodificado ({algoritmo}): {resultado_decodificado}")

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

# Entry field for K (Golomb)
k_label = tk.Label(janela, text="Valor de K (Golomb):")
k_label.pack()
k_entry = tk.Entry(janela, width=5)
k_entry.pack()

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

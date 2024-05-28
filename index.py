# Importa os módulos necessários
from tkinter import *  # Importa todos os elementos do tkinter
from tkinter import messagebox  # Importa a caixa de mensagens do tkinter
from tkinter.filedialog import asksaveasfilename, askopenfilename  # Importa as funções de diálogo para abrir e salvar arquivos
import subprocess  # Importa o módulo subprocess para executar comandos do sistema
import os  # Importa o módulo os para interações com o sistema operacional

# Cria a janela principal do aplicativo
root = Tk()
root.title("IDLE")  # Define o título da janela
root.geometry("1280x720+150+80")  # Define o tamanho e a posição da janela
root.configure(bg="#323846")  # Define a cor de fundo da janela
root.resizable(False, False)  # Impede que a janela seja redimensionada

file_path = ''  # Variável global para armazenar o caminho do arquivo

# Função para definir o caminho do arquivo
def set_file_path(path):
    global file_path
    file_path = path

# Função para abrir um arquivo
def open_file():
    path = askopenfilename(filetypes=[('Arquivos Python', '*.py')])  # Abre a janela de diálogo para selecionar um arquivo
    with open(path, 'r') as file:  # Abre o arquivo selecionado em modo leitura
        code = file.read()  # Lê o conteúdo do arquivo
        code_input.delete('1.0', END)  # Limpa o conteúdo atual do widget de entrada de código
        code_input.insert('1.0', code)  # Insere o conteúdo do arquivo no widget de entrada de código
        set_file_path(path)  # Define o caminho do arquivo

# Função para salvar o arquivo
def save():
    if file_path == '':  # Verifica se o caminho do arquivo está vazio (novo arquivo)
        path = asksaveasfilename(filetypes=[('Arquivos Python', '*.py')])  # Abre a janela de diálogo para salvar um novo arquivo
    else:
        path = file_path  # Usa o caminho do arquivo existente

    with open(path, 'w') as file:  # Abre o arquivo em modo escrita
        code = code_input.get('1.0', END)  # Obtém o conteúdo do widget de entrada de código
        file.write(code)  # Escreve o conteúdo no arquivo
        set_file_path(path)  # Define o caminho do arquivo

# Função para executar o código Python
def run():
    if file_path == '':  # Verifica se o caminho do arquivo está vazio
        messagebox.showerror("IDLE", "Salve seu código")  # Exibe uma mensagem de erro se o arquivo não estiver salvo
        return
    command = f'python {file_path}'  # Cria o comando para executar o arquivo Python
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)  # Executa o comando em um subprocesso
    output, error = process.communicate()  # Captura a saída e os erros do subprocesso
    code_output.insert('1.0', output)  # Insere a saída no widget de saída de código
    code_output.insert('1.0', error)  # Insere os erros no widget de saída de código

# Widget de entrada de código
code_input = Text(root, font="consolas 18")  # Cria um widget de texto para entrada de código
code_input.place(x=180, y=0, width=680, height=720)  # Define a posição e o tamanho do widget

# Widget de saída de código
code_output = Text(root, font="consolas 15", bg="#323846", fg="lightgreen")  # Cria um widget de texto para saída de código
code_output.place(x=860, y=0, width=420, height=720)  # Define a posição e o tamanho do widget

# Carrega as imagens dos botões
Open = PhotoImage(file="open.png")  # Carrega a imagem do botão de abrir arquivo
Save = PhotoImage(file="save.png")  # Carrega a imagem do botão de salvar arquivo
Run = PhotoImage(file="run.png")  # Carrega a imagem do botão de executar código

# Cria os botões e associa as funções correspondentes
Button(root, image=Open, bg="#323846", bd=0, command=open_file).place(x=30, y=30)  # Botão de abrir arquivo
Button(root, image=Save, bg="#323846", bd=0, command=save).place(x=30, y=145)  # Botão de salvar arquivo
Button(root, image=Run, bg="#323846", bd=0, command=run).place(x=30, y=260)  # Botão de executar código

# Inicia o loop principal da interface gráfica
root.mainloop()
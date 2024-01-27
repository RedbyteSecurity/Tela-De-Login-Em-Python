import customtkinter
import tkinter as tk
from tkinter import messagebox

# Configuração inicial do modo noturno
modo_noturno = False

def toggle_modo_noturno():
    global modo_noturno
    modo_noturno = not modo_noturno
    if modo_noturno:
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")

# Função para mostrar ou ocultar a senha
def toggle_mostrar_senha():
    if mostrar_senha.get():
        senha_entry.configure(show="")
    else:
        senha_entry.configure(show="*")

# Função para lidar com o clique na frase "Esqueci minha senha"
def esqueci_minha_senha():
    messagebox.showinfo("Esqueci minha senha", "Em breve, você receberá instruções para recuperar sua senha por e-mail.")

# Criar a janela principal
janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Sistema de Login")

# Criar e configurar widgets
texto = customtkinter.CTkLabel(janela, text="Realizar Login")

email = customtkinter.CTkEntry(janela, placeholder_text="E-mail")

# Usar um Entry padrão para a senha
senha_entry = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")

# Variável para controlar se a senha deve ser mostrada ou não
mostrar_senha = tk.BooleanVar()

# Adicionar checkbox para mostrar a senha
checkbox_mostrar_senha = customtkinter.CTkCheckBox(janela, text="Mostrar Senha", variable=mostrar_senha, command=toggle_mostrar_senha)

botao_login = customtkinter.CTkButton(janela, text="Login", command=lambda: print("Login realizado com sucesso!"))

# Adicionar frase clicável "Esqueci minha senha"
fonte_esqueci_senha = customtkinter.CTkFont(family="Arial", size=10, underline=True)
frase_esqueci_senha = customtkinter.CTkLabel(janela, text="Esqueci minha senha", font=fonte_esqueci_senha, cursor="hand2")
frase_esqueci_senha.bind("<Button-1>", lambda event: esqueci_minha_senha())

# Adicionar menu de opções
menu_opcoes = tk.Menu(janela)

# Adicionar opção de modo noturno ao menu
menu_opcoes.add_checkbutton(label="Modo Noturno", command=toggle_modo_noturno)

# Configurar menu na janela
janela.config(menu=menu_opcoes)

# Posicionar os widgets na janela
texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha_entry.pack(padx=10, pady=10)
checkbox_mostrar_senha.pack(pady=5)
botao_login.pack(padx=10, pady=10)
frase_esqueci_senha.pack(pady=5)

# Iniciar o loop principal da interface gráfica
janela.mainloop()

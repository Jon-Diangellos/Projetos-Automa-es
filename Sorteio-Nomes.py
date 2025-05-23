# Interface gráfica criada com a biblioteca CustomTkinter para simular um sistema de sorteio de nomes.
# Contém botões para adicionar nomes, embaralhar e retirar um nome, além de uma checkbox de verificação.

import customtkinter
import random

nomes = []

def adicionar_nome():
    nome = entry.get().strip()
    if nome:
        nomes.append(nome)
        entry.delete(0, 'end')
        atualizar_lista()
        resultado_label.configure(text="Nome adicionado com sucesso.")
    else:
        resultado_label.configure(text="Digite um nome válido.")

def atualizar_lista():
    lista_nomes.configure(state='normal')
    lista_nomes.delete("1.0", "end")
    for nome in nomes:
        lista_nomes.insert("end", nome + "\n")
    lista_nomes.configure(state='disabled')

def embaralhar():
    if nomes:
        random.shuffle(nomes)
        atualizar_lista()
        resultado_label.configure(text="Lista embaralhada!")
    else:
        resultado_label.configure(text="Nenhum nome para embaralhar.")

def retirar_nome():
    if nomes:
        nome_sorteado = nomes.pop(random.randint(0, len(nomes) - 1))
        atualizar_lista()
        resultado_label.configure(text=f"Nome sorteado: {nome_sorteado}")
    else:
        resultado_label.configure(text="Nenhum nome disponível para sortear.")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Teste da sorte!")
app.geometry("550x500")

entry = customtkinter.CTkEntry(app, placeholder_text="Digite um nome")
entry.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")

botao_adicionar = customtkinter.CTkButton(app, text="Adicionar Nome", command=adicionar_nome)
botao_adicionar.grid(row=0, column=2, padx=10, pady=(20, 10))

botao_embaralhar = customtkinter.CTkButton(app, text="EMBARALHAR", command=embaralhar)
botao_embaralhar.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

botao_retirar = customtkinter.CTkButton(app, text="Retirar um nome", command=retirar_nome)
botao_retirar.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="ew")

lista_nomes = customtkinter.CTkTextbox(app, height=150, width=500)
lista_nomes.grid(row=2, column=0, columnspan=3, padx=20, pady=10)
lista_nomes.configure(state='disabled')


resultado_label = customtkinter.CTkLabel(app, text="")
resultado_label.grid(row=4, column=0, columnspan=3, padx=20, pady=20)

app.mainloop()



# Este script organiza automaticamente os arquivos de uma pasta escolhida pelo usuário.
# Os arquivos são movidos para subpastas como "imagens", "planilhas" e "arquivos"
# com base em suas extensões, utilizando a biblioteca os e a interface de seleção de pasta do tkinter.

import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".pdf", ".docx", ".pptx", ".odt"],
    "arquivos": [".exe"],
}

for arquivos in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivos}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivos}", f"{caminho}/{pasta}/{arquivos}")

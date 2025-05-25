# Este script converte todos os arquivos .txt de uma pasta selecionada pelo usuário em arquivos .pdf,
# salvando os PDFs na mesma pasta, com o mesmo nome base.
# Instalação do fpdf: pip install fpdf

import os
from tkinter.filedialog import askdirectory
from fpdf import FPDF

caminho = askdirectory(title="Selecione a pasta com os arquivos .txt")

arquivos_txt = [arq for arq in os.listdir(caminho) if arq.endswith(".txt")]

for arquivo in arquivos_txt:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(os.path.join(caminho, arquivo), "r", encoding="utf-8") as f:
        for linha in f:
            pdf.cell(200, 10, txt=linha.strip(), ln=1)

    nome_pdf = arquivo.replace(".txt", ".pdf")
    pdf.output(os.path.join(caminho, nome_pdf))

print("Conversão concluída com sucesso.")

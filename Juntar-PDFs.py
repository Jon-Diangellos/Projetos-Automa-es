# Script em Python que combina todos os arquivos PDF da pasta "arquivos" 
# em um único arquivo chamado "PDF_Final.pdf", usando a biblioteca PyPDF2.
# Para executar este script, você deve ter a biblioteca PyPDF2 instalada.
# Você pode instalar a biblioteca usando o seguinte comando:
# pip install PyPDF2
# Certifique-se de que a pasta "arquivos" contém os arquivos PDF que você deseja combinar.

import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivos in lista_arquivos:
    if ".pdf" in arquivos:
        merger.append(f"arquivos/{arquivos}")

merger.write("PDF_Final.pdf")
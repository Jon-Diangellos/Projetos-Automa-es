# Este script automatiza o preenchimento de um formulário online.
# O usuário informa o caminho do navegador e a URL do formulário.
# O programa abre o navegador e preenche automaticamente os campos usando pyautogui.
# Tenha o pyautogui instalado
# pip install pyautogui


import pyautogui
import subprocess
import time

caminho_navegador = input("Cole aqui o caminho do navegador (ex: C:/.../chrome.exe): ")

url_formulario = input("Cole aqui a URL do formulário: ")

subprocess.run(caminho_navegador)

time.sleep(1)
pyautogui.write(url_formulario)
pyautogui.press('enter')

time.sleep(2)
pyautogui.write('seu nome')
pyautogui.press('tab')

time.sleep(1)
pyautogui.write('cachorro')
pyautogui.press('tab')

time.sleep(1)
pyautogui.write('Vira-lata')
pyautogui.press('tab')

time.sleep(1)
pyautogui.press('enter')

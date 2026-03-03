#login in system 
#login
#base de dados
#cadastrar produto
#n++ até acabar

#bibliotecas
#automatização - pyautogui 
#   pyautogui.clik (clica no botao)
#   pyautogui.write (escreve)
#   pyautogui.press(Aperta tecla)
#   pyautogui.hotkey (aperta um atalho)

# pip install pandas openpyxl - mexer com excel arquivos


import pyautogui
import time

#variavel  = não precisa dizer o tipo

link = "google docs"
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter") 
time.sleep(1) #computador espera o tempo passado
pyautogui.click(484, 911) #posição do campo x, y da tela. Auxiliado com o auxi.py
pyautogui.write(link)  
pyautogui.press("enter")

#pyautogui.press("tab") #ele passa pro prox campo do formulario

pyautogui.click(x=362, y=393)

import pandas

tabela = pandas.read_csv("produtos.csv")
#pandas.read_excel(sheet_name=) abre a aba do excel
print (tabela)

for linha in tabela.index: #ele sabe que é linha devido a tabela.INDEX devido a posição de cada linha na table
    pyautogui.press()
    pyautogui.write("Produto 01")
    pyautogui.press("tab")



#voltar para o inicio da tela - telca HOME ou 
pyautogui.scroll # positivo ele sobe, negativo desce
#cadastrando um produto no primeiro campo, igual para os outros 
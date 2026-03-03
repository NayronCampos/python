import pyautogui
import time
import pandas

#booting SIGO
time.sleep(4)

#Enter the new revenue
pyautogui.click(x=1848, y=379) 

tabela = pandas.read_csv("Dados.csv", sep=";")

for linha in tabela.index:

    #Número da nf
    Nota = str(tabela.loc[linha, "NF"])
    #Nome da obra
    Obra = str(tabela.loc[linha, "SECRETARIA"])
    #nº do contrato
    Contrato = str(tabela.loc[linha, "CONTRATO"])
    #dia da emissão da nota
    emissao = str(tabela.loc[linha, "DATA EMISSÃO NOTA FISCAL"])

    time.sleep(2)
    #first field
    pyautogui.click(x=626, y=272)

    #Add data
    pyautogui.write("Nota: " + Nota + " - Contrato: " + Contrato + " Obra: " + Obra, interval=0.2)

    #next fields
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")

    #add category
    pyautogui.press("enter")
    #name
    pyautogui.write("deposito")
    pyautogui.press("enter")

    #next field bank
    pyautogui.click(x=934, y=348)

    #name
    pyautogui.write("btg")
    pyautogui.press("enter")

    #enter field maturity
    pyautogui.click(x=1327, y=346)

    #add date
    pyautogui.write(emissao)

    #Next field value
    pyautogui.press("tab")


    '''
    Impostos:

    

    '''




    



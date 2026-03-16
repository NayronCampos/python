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
    #centro de custo da nota
    centro = tabela.loc[linha, "SECRETARIA"]
    #valor
    pryce = str(tabela.loc[linha, " VALOR BRUTO "])

    time.sleep(2)
    #first field
    pyautogui.click(x=626, y=272)

    #Add data
    pyautogui.write("Nota: " + Nota + " - Contrato: " + Contrato + " Obra: " + Obra, interval=0.1)

    #next fields
    pyautogui.press("tab")
    pyautogui.write(emissao)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")

    #add category
    pyautogui.press("enter")

    #name category
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

    #Next field = pryce
    pyautogui.write(pryce)

    pyautogui.click(x=1834, y=480)

    time.sleep(3)

    
    #Enter impost
    #Confins
    Cofins = str(tabela.loc[linha, " PIS/COFINS "])
    #csll
    csll = str(tabela.loc[linha, " PIS/COFINS "])
    #iss
    iss = str(tabela.loc[linha, " ISS "])
    #pis - está junto ao confins
    #pis = str(tabela.loc[linha, " PIS/COFINS "])


    #field Center Cust
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")

    #confins
    pyautogui.press("enter")
    pyautogui.press("down")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.write(Cofins)
    
    #csll
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("down")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.write(csll)
    
    #iss
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("down")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.write(iss)

    '''
    #pis - junto ao confins
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("down")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.write(pis)
    '''
    pyautogui.press(x=29, y=582)
    time.sleep(10)
    '''
    pyautogui.press("tab")
    pyautogui.write(centro)
    pyautogui.press("enter")
    '''
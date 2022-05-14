import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 1

pyautogui.hotkey("win", "s")
pyperclip.copy("google chrome")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(7)
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(20)
pyautogui.click(x=363, y=261)
pyautogui.press("enter")
time.sleep(7)
pyautogui.click(x=373, y=349, button="right")
pyautogui.click(x=523, y=639)
pyautogui.click(button="left")

tabela = pd.read_excel(r"C:\Users\Josther Sampaio\Downloads\Vendas - Dez.xlsx")

Faturamento = tabela["Valor Final"].sum()
Quantidade = tabela["Quantidade"].sum()

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/1/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=70, y=172)

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/1/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(20)
pyautogui.click(x=70, y=172)
time.sleep(10)
pyautogui.write("seugmail+diretoria@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("relatório de vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
texto = f"""Olá amigos, segue aqui o relatorio do dia anterior
faturamento:{Faturamento}
quantidade:{Quantidade}
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")
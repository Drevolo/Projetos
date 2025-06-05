#Automação ultilizada para Pegar informações do Excel e Lançar no Departamento Contabil do Sistema Dominio

import pyautogui
import time
import PySimpleGUI as sg

sg.theme('Topanga')

pyautogui.PAUSE = 0.45

X = sg.popup_get_text('Quantidade')
M = int(X)
time.sleep(10)

for i in range(M):

    pyautogui.click(240,198) #pega na planilha
    pyautogui.hotkey('Ctrl','a')
    pyautogui.hotkey('Ctrl','c')
    pyautogui.hotkey('Alt','Tab')
    pyautogui.doubleClick(106,237) #data no sistema
    pyautogui.hotkey('Ctrl','v')
    pyautogui.hotkey('Alt','Tab')
    pyautogui.click(142,196) #fechar seleção
    pyautogui.press(['right', 'right'])
    pyautogui.click(245,198) #selecionar
    pyautogui.hotkey('Ctrl','a')
    pyautogui.hotkey('Ctrl','c')
    pyautogui.hotkey('Alt','Tab')
    pyautogui.press(['Tab','Tab']) #debitar
    pyautogui.hotkey('Ctrl','v')
    pyautogui.press('Tab')
    pyautogui.write('4')
    pyautogui.press('Enter')
    pyautogui.hotkey('Alt','Tab')
    pyautogui.click(142,196) #fechar seleção
    pyautogui.press('right')
    pyautogui.click(245,198) #selecionar
    pyautogui.hotkey('Ctrl','a')
    pyautogui.hotkey('Ctrl','c')
    pyautogui.hotkey('Alt','Tab')
    pyautogui.hotkey('Ctrl','v')
    pyautogui.press('Enter')
    pyautogui.hotkey('Alt','Tab')
    pyautogui.click(142,196) #fechar seleção
    pyautogui.press('right')
    pyautogui.click(245,198) #selecionar
    pyautogui.hotkey('Ctrl','a')
    pyautogui.hotkey('Ctrl','c')
    pyautogui.hotkey('Alt','Tab')
    pyautogui.hotkey('Ctrl','v')
    pyautogui.press('Enter')
    pyautogui.click(682,646) #gravar
    pyautogui.hotkey('Alt','Tab')
    pyautogui.click(142,196) #fechar seleção
    pyautogui.press('right')
    pyautogui.write('ok')
    pyautogui.press('Enter')
    pyautogui.press(['left', 'left', 'left', 'left', 'left'])

sg.popup('Finalizado')
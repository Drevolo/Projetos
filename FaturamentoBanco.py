import secrets
import PySimpleGUI as sg
import pyautogui
import time

pyautogui.PAUSE = 0.5

FF = []

sg.theme('Topanga')

layout = [

    [sg.Text('Qual o Último Mês? (M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11, M12)')],
    [sg.InputText('', key='RR')],
    
    [sg.Text('Digite o Valor para começar a Variação do Faturamento à Vista')],
    [sg.InputText('', key='IR')],
    
    [sg.Text('Digite o Valor para finalizar a Variação do Faturamento à Vista')],
    [sg.InputText('', key='FR')],
    
    [sg.Text('Digite o Valor para começar a Variação do Faturamento à Prazo')],
    [sg.InputText('', key='IR1')],
    
    [sg.Text('Digite o Valor para finalizar a Variação do Faturamento à Prazo')],
    [sg.InputText('', key='FR1')],
    
    [sg.Button('OK'), sg.Button('Cancelar')]
]

window = sg.Window('Entrada de Dados', layout)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break
    
    if event == 'OK':
        RR = values['RR']
        IR = values['IR']
        FR = values['FR']
        IR1 = values['IR1']
        FR1 = values['FR1']
        window.close()
        
window.close()

VIR = int(IR)
VFR = int(FR)
VIR1 = int(IR1)
VFR1 = int(FR1)

M01 = ['022024', '032024', '042024', '052024', '062024', '072024', '082024', '092024', '102024', '112024', '122024', '012025']
M02 = ['032024', '042024', '052024', '062024', '072024', '082024', '092024', '102024', '112024', '122024', '012025', '022025']
M03 = ['042024', '052024', '062024', '072024', '082024', '092024', '102024', '112024', '122024', '012025', '022025', '032025']
M04 = ['052024', '062024', '072024', '082024', '092024', '102024', '112024', '122024', '012025', '022025', '032025', '042025']
M05 = ['062024', '072024', '082024', '092024', '102024', '112024', '122024', '012025', '022025', '032025', '042025', '052025']
M06 = ['072024', '082024', '092024', '102024', '112024', '122024', '012025', '022025', '032025', '042025', '052025', '062025']
M07 = ['082024', '092024', '102024', '112024', '122024', '012025', '022025', '032025', '042025', '052025', '062025', '072025']
M08 = ['092024', '102024', '112024', '122024', '012025', '022025', '032025', '042025', '052025', '062025', '072025', '082025']
M09 = ['102024', '112024', '122024', '012025', '022025', '032025', '042025', '052025', '062025', '072025', '082025', '092025']
M10 = ['112024', '122024', '012025', '022025', '032025', '042025', '052025', '062025', '072025', '082025', '092025', '102025']
M11 = ['122024', '012025', '022025', '032025', '042025', '052025', '062025', '072025', '082025', '092025', '102025', '112025']
M12 = ['012025', '022025', '032025', '042025', '052025', '062025', '072025', '082025', '092025', '102025', '112025', '122025']

listas = { 
    'M01': M01,
    'M02': M02,
    'M03': M03,
    'M04': M04,
    'M05': M05,
    'M06': M06,
    'M07': M07,
    'M08': M08,
    'M09': M09,
    'M10': M10,
    'M11': M11,
    'M12': M12,
}

if RR in listas:
    RE = listas[RR]

else:
    sg.popup('Invalido')

time.sleep(5)

for i in range(12):

    TT = RE[i]

    pyautogui.write(TT)

    F = str(secrets.choice(range(VIR, VFR)))
    FF = f'{F},00'
    
    pyautogui.write(FF)
    pyautogui.press('Tab')

    G = str(secrets.choice(range(VIR1, VFR1)))
    GG = f'{G},00'
    
    pyautogui.write(GG)
    pyautogui.press('Tab')

sg.popup('Finalizado')
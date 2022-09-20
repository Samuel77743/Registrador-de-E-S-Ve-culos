from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime

def registrador():
    a = datetime.today().strftime('%H:%M')
    b = int()
    c = 'R$ 0,00'
    sg.theme('DarkPurple7')
    linha = [
        [sg.Text('Placa'), sg.Text('          Modelo/cor'), sg.Text('             Entrada'), sg.Text('  Saída'), sg.Text('  Valor do Serviço')],
        [sg.Input('',size=(9, 1)), sg.Input('',size=(20, 1)), sg.Input(a,size=(5, 1)), sg.Input(b,size=(5,1)), sg.Input(c,size=(14, 1))],
    ]
    layout2 = [
        [sg.Frame('Registrador', layout=linha, key='container')],
        [sg.Button('Adicionar Registro'), sg.Button('Resetar Registros')]
    ]
    return sg.Window('Registro de Veículos', layout=layout2, finalize=True)


janela2 = registrador()
# Regras da Janela
while True:
    eventos2, valores2 = janela2.read()
    if eventos2 == sg.WINDOW_CLOSED: #Permitindo que sja encerrado programa
        break
    elif eventos2 == 'Adicionar Registro':
        a = datetime.today().strftime('%H:%M')
        b = int()
        c = 'R$ 0,00'
        janela2.extend_layout(janela2['container'], [[sg.Input('',size=(9, 1)), sg.Input('',size=(20, 1)), sg.Input(a,size=(5, 1)), sg.Input(b,size=(5,1)), sg.Input(c,size=(14, 1))]])
    elif eventos2 == 'Resetar Registros':
        janela2.close()
        janela2 = registrador()
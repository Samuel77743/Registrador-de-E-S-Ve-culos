from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime as dt

def registrador():
    layout_menu = [['Arquivo', ['Gerar Relatório', 'Encaminha para E-mail']],
                   ['Opções', ['Alterar Tema', 'Voltar a Tela de Login']],
                   ['Ajuda', ['Manual do Software', 'Contato Desenvolvedor',['E-mail: samuel0100wanderson@gmail.com', 'higor_scosta@outlook.com']]]]

    hh_entrada = int(dt.today().strftime('%H'))
    mm_entrada = int(dt.today().strftime('%M'))
    hh_saida = int()
    mm_saida = int()
    valor_servico = 0

    padrao = 'DarkPurple7'
    cor2 = 'SystemDefaultForReal'
    cor3 = 'Black'
    tema = sg.theme(padrao)
    tema
    btd_background = ['Options'], ['Adicionar Registro']
    btd_txt = ['Copiar', 'Colar', 'Recortar']
    linha = [
        [sg.Menu(layout_menu, background_color="white", text_color="black", key='aba')],
        [sg.Text('Placa'), sg.Text('          Modelo/cor'), sg.Text('               Entrada'), sg.Text('    Saída'), sg.Text('  Valor do Serviço')],
        [sg.Input('',size=(9, 1)), sg.Input('',size=(20, 1)), sg.Input(hh_entrada, size=(2, 1)), sg.Input(mm_entrada, size=(2, 1)),
         sg.VerticalSeparator(), sg.Input(hh_saida, size=(2, 1), key= 'update1'), sg.Input(mm_saida, size=(2, 1), key= 'update2'),
         sg.Button('※', button_color=("Grey")), sg.Input(valor_servico, size=(14, 1))],
    ]
    layout2 = [
        [sg.Frame('Registrador', layout=linha, key='container')],
        [sg.Button('Adicionar Registro'), sg.Button('Resetar Registros'), sg.Button("⁜ $$ Pagar via PIX $$ ⁜", button_color=('Dark Green'), font="Roboto")]
    ]
    return sg.Window('Registro de Veículos', layout=layout2, resizable=True, finalize=True, auto_size_buttons=True, auto_size_text=True, right_click_menu = btd_background, right_click_menu_background_color='White', right_click_menu_text_color='Black', icon='.\icon.ico')
janela2 = registrador()
# Regras da Janela
while True:
    eventos2, valores2 = janela2.read(timeout=1)

    btd_background = ['Adicionar Registro'], ['Adicionar Registro']

    if eventos2 == sg.WINDOW_CLOSED: #Permitindo que seja encerrado programa
        break
    elif (eventos2 == 'Adicionar Registro') or (eventos2 == btd_background):
        hh_entrada = int(dt.today().strftime('%H'))
        mm_entrada = int(dt.today().strftime('%M'))
        hh_saida = int()
        mm_saida = int()
        valor_servico = 0
        eventos2 = janela2.extend_layout(janela2['container'], [[sg.Input('',size=(9, 1)), sg.Input('',size=(20, 1)),
                                                                 sg.Input(hh_entrada, size=(2, 1)), sg.Input(mm_entrada, size=(2, 1)),
                                                                 sg.VerticalSeparator(), sg.Input(hh_saida, size=(2, 1), key= 'update2'),
                                                                 sg.Input(mm_saida, size=(2, 1), key= 'update1'),  sg.Button('※', button_color=("Grey")),
                                                                 sg.Input(valor_servico, size=(14, 1))]]),
    elif eventos2 == "⁜ $$ Pagar via PIX $$ ⁜":
        sg.theme('Purple')
        sg.popup(title="Efetue escaneamento para efetuar o pagamento", image=".\Pix1.png", custom_text=("Pagamento Efetuado", "Cancelar"))

        sg.theme('Dark Purple 7')
    elif eventos2 == 'Resetar Registros':
        sg.theme('DarkPurple5')
        sim = 'Sim'
        nao = 'Não'
        answer = sg.popup('Se confirmar isso irá apagar todos os registros!\nTem certeza?', font='Arial', custom_text=(sim, nao), background_color= 'Brown', title='Aviso')
        sg.theme('DarkPurple7')
        if answer == nao:
            ()
        elif answer == sim:
            janela2.close()
            janela2 = registrador()
        else: ()
    elif eventos2 == '※':
        janela2['update1'].update(int(dt.today().strftime('%H')))
        janela2['update2'].update(int(dt.today().strftime('%M')))






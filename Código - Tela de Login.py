from PySimpleGUI import PySimpleGUI as sg
import os
#Janela 1
#Layout
def login():
    sg.theme('DarkPurple7')
    menu = [['Ajuda', ['Acessar Manual', 'Contato Desenvolvedor',['E-mails:', 'samuel0100wanderson@gmail.com', 'higor_scosta@outlook.com']]]]

    layout = [
        #Estrura de inputs, textos e botões
        [sg.Menu(menu, background_color='White', text_color="Black")],
        [sg.Text('Usuário'), sg.Input(key='usuario', size=(30,1))],
        [sg.Text('  Senha'), sg.Input(key='senha',password_char='*', size=(30,1))],
        [sg.Checkbox('Salvar Login')],
        [sg.Button('Entrar')],
        [sg.Text(key='msg')],
    ]
    #Para invocar a Janela com layout descrito acima:
    janela = sg.Window('Tela de Login', layout, icon=('.\icon.ico'))

    #Ler eventos:

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            telinha = sg.popup('Deseja encerrar o processo de Login?', custom_text=('Sim', 'Não'), title= 'Aviso')
            if telinha == 'Sim':
                break
            else: return login()
        #AUTENTICAÇÃO DE USUÁRIOS
        elif eventos == 'Entrar': #SENHA: 19062012 POIS É A DATA DE INAUGURAÇÃO DA LOJA
            valores['usuario'] = valores['usuario'].upper()
            #Credenciais Disponíveis:
            if ((((valores['usuario'] == 'ALBANO DIAS')) or ((valores['usuario'] == 'ANDRÉ DIAS'))
            or ((valores['usuario'] == 'ANDRE DIAS')) or ((valores['usuario'] == 'CRISTIANO DIAS')))
            and (valores['senha'] == '19062012'))\
            or ((valores['usuario'] == 'CONVIDADO') and (valores['senha'] == '12345678')):
                janela['msg'].update('Login realizado com sucesso!')
                os.startfile('.\executaveis\Registrador Stop Car.exe')
                break

            elif (valores['usuario'] == ('')) or (valores['senha'] == ('')):
                janela['msg'].update('Preencha todas as Lacunas!')

            else: janela['msg'].update('Senha ou Usuário incorreto')
login()

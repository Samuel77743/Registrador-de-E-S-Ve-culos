from PySimpleGUI import PySimpleGUI as sg

#Janela 1
#Layout
def login():
    sg.theme('DarkPurple7')
    menu = [['Ajuda', ['Acessar Manual', 'Contator Desenvolvedor',['E-mail: samuel0100wanderson@gmail.com', 'higor_scosta@outlook.com']]]]
    layout = [

        [sg.Menu(menu)],
        [sg.Text('Usuário'), sg.Input(key='usuario', size=(30,1))],
        [sg.Text('  Senha'), sg.Input(key='senha',password_char='*', size=(30,1))],
        [sg.Checkbox('Salvar Login')],
        [sg.Button('Entrar')],
        [sg.Text(key='msg')],
    ]
    #Para invocar a Janela com layout descrito acima:
    janela = sg.Window('Tela de Login', layout)

    #Ler eventos:

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            telinha = sg.popup('Deseja encerrar o processo de Login?', custom_text=('Sim', 'Não'), title= 'Aviso')
            if telinha == 'Sim':
                break
            else: return login()

        elif eventos == 'Entrar': #SENHA: 19062012 POIS É A DATA DE INAUGURAÇÃO DA LOJA
            if (((valores['usuario'] == 'Albano Dias')) or ((valores['usuario'] == 'André Dias')) or ((valores['usuario'] == 'Cristiano Dias'))) and (valores['senha'] == '19062012'):
                janela['msg'].update('Login realizado com sucesso!')
            elif (valores['usuario'] == ('')) or (valores['senha'] == ('')):
                janela['msg'].update('Preencha todas as Lacunas!')
            else: janela['msg'].update('Senha ou Usuário incorreto')
login()

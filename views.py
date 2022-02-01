import PySimpleGUI as sg

def get_interface(price_bitcoin):
    sg.theme('SystemDefaultForReal')

    col_1 =[
            [sg.Text('', key='-priceBit-')],
            ]
    col_2 =[
            [sg.Text('', key='-USD-')],
            ]
    col_image = [[sg.Image('new_img.png', key='-image-',visible=False)]]

    layout = [[sg.Frame(layout=col_image, title='Уровень страха/жадности')],
              [sg.Frame(layout=col_1, title='Курс Bitcoin '), sg.Frame(layout=col_2, title='Курс доллар ')],
              [sg.Button('Обновить',button_color='#3fb54b')]]


    window = sg.Window('Sebastian', layout, size=(700, 530), icon='logo.ico', resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        elif event == 'Обновить':
            window['-priceBit-'].update(price_bitcoin)
            window ['-image-'].update(visible=True)
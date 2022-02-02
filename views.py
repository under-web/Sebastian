import PySimpleGUI as sg
import parser


sg.theme('SystemDefaultForReal')

col_1 = [
    [sg.Text('', key='-priceBit-')],
]
col_2 = [
    [sg.Text('', key='-USD-')],
]
col_image = [[sg.Image('img.png', key='-image-', visible=False)]]

layout = [[sg.Frame(layout=col_image, title='Уровень страха/жадности')],
          [sg.Frame(layout=col_1, title='Bitcoin '), sg.Frame(layout=col_2, title='Dollar ')],
          [sg.Button('Обновить', button_color='#3fb54b')]]

window = sg.Window('Sebastian', layout, size=(700, 530), icon='logo.ico', resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    elif event == 'Обновить':
        result = parser.get_busines_logic()
        window['-priceBit-'].update(result[0])
        window['-USD-'].update(result[1])
        window['-image-'].update(filename='img.png', visible=True)
        window.enable()
window.close()
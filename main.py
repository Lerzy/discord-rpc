import PySimpleGUI as sg
import subprocess
from rpc import RPCRunner

sg.theme('Black')


layout = [  
            
            [sg.Text('Application id:'), sg.InputText()],
            [sg.Text('State:'), sg.InputText()],
            [sg.Text('Details:'), sg.InputText()],
            [sg.Text('Large img text:'), sg.InputText(), sg.Text('Large img key:'), sg.InputText()],
            [sg.Text('Small img text:'), sg.InputText(), sg.Text('Small img key:'), sg.InputText()],
            [sg.Checkbox('Enabled', default=False), sg.Text('Button1 text:'), sg.InputText(), sg.Text('Button1 URL:'), sg.InputText()],
            [sg.Checkbox('Enabled', default=False), sg.Text('Button2 text:'), sg.InputText(), sg.Text('Button2 URL:'), sg.InputText()],
            [sg.Button('Run RPC'), sg.Button('Cancel')] 
            
        ]


window = sg.Window('Discord rich presence', layout)

buttons = None


"""
indexes go like this:
0: id
1: state
2: details
3: l img text
4: l img key
5: s img text
6: s img key
7: b1 checkbox
8: b1 text
9: b1 url
10: b2 checkbox
11: b2 text
12: b2 url

"""

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break

    if values[7] and values[10] == True:
        buttons = [{"label": values[8], "url": values[9]}, {"label": values[11], "url": values[12]}]
    elif values[7] or values[10] == True:
        buttons = [{"label": values[8] if values[7] == True else values[11], "url": values[9] if values[7] == True else values[12]}]

    RPCRunner(values[0], values[1], values[2], values[3], values[4], values[5], values[6], buttons)

window.close()
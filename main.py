import PySimpleGUI as sg
from rpc import RPCRunner

sg.theme('Black')


layout = [  
            
            [sg.Text('Application id:'), sg.InputText(k="-APP-ID-")],
            [sg.Text('Details:'), sg.InputText(k="-DETAILS-")],
            [sg.Text('State:'), sg.InputText(k="-STATE-")],
            [sg.Text('Party size:'), sg.InputText(k="-P-SIZE-F-"), sg.Text('/'), sg.InputText(k="-P-SIZE-S-")], #  f stands for first, s for second bruh
            [sg.Text('Large img text:'), sg.InputText(k="-L-IMG-TEXT-"), sg.Text('Large img key:'), sg.InputText(k="-L-IMG-KEY-")],
            [sg.Text('Small img text:'), sg.InputText(k="-S-IMG-TEXT-"), sg.Text('Small img key:'), sg.InputText(k="-S-IMG-KEY-")],
            [sg.Checkbox('Enabled', default=False, k="-B1-CHECK-"), sg.Text('Button1 text:'), sg.InputText(k="-B1-TEXT-"), sg.Text('Button1 URL:'), sg.InputText(k="-B1-URL-")],
            [sg.Checkbox('Enabled', default=False, k="-B2-CHECK-"), sg.Text('Button2 text:'), sg.InputText(k="-B2-TEXT-"), sg.Text('Button2 URL:'), sg.InputText(k="-B2-URL-")],
            [sg.Text("Clicking on 'Run RPC' multiple times will spawn new rpc processes and they will show up as individual games on discord, it's not a bug it's a feature:D")],
            [sg.Button('Run RPC'), sg.Button('Cancel')],
            [sg.Output(size=(150, 5), k="-RPC-STATUS-")]
            
        ]


window = sg.Window('Discord rich presence', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break

    if event == "Run RPC":

        if values["-P-SIZE-F-"] and values["-P-SIZE-S-"] is not None:
            party_size = [int(values["-P-SIZE-F-"]), int(values["-P-SIZE-S-"])]
        else:
            party_size = None



        buttons = None

        if values["-B1-CHECK-"] and values["-B2-CHECK-"] == True:
            buttons = [{"label": values["-B1-TEXT-"], "url": values["-B1-URL-"]}, {"label": values["-B2-TEXT-"], "url": values["-B2-URL-"]}]
        elif values["-B1-CHECK-"] == True:
            buttons = [{"label": values["-B1-TEXT-"], "url": values["-B1-URL-"]}]
        elif values["-B2-CHECK-"] == True:
            buttons = [{"label": values["-B2-TEXT-"], "url": values["-B2-URL-"]}]
       
        

        """def RPCRunner(client_id, state, details, large_text, large_image, small_text, small_image, buttons, party_size):"""
        rpc_status = RPCRunner(
            values["-APP-ID-"],
            values["-STATE-"],
            values["-DETAILS-"],
            values["-L-IMG-TEXT-"],
            values["-L-IMG-KEY-"],
            values["-S-IMG-TEXT-"],
            values["-S-IMG-TEXT-"],
            buttons,
            party_size)
        print(f"Running RPC, check your discord activity:D\n{rpc_status}")
        

window.close()

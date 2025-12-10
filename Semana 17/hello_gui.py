import FreeSimpleGUI as sg

layout = [
    [sg.Text("¡FreeSimpleGUI funciona perfectamente!")],
    [sg.Button("OK")]
]

window = sg.Window("Prueba GUI", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "OK":
        break

window.close()

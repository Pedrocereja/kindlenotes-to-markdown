from kindle2md import kindle2md
import os
import PySimpleGUI as sg

sg.theme('LightBlue1')

layout =    [[sg.Text('Escolha o arquivo kindle a ser convertido:')],      
            [sg.Input(key='-IN-'), sg.FileBrowse()],      
            [sg.Submit('Converter'), sg.Cancel('Cancelar')]]      

window = sg.Window('Kindle2md', layout)    

event, values = window.read()    
window.close()

if event!='Converter':
    quit()

resultado = kindle2md(values['-IN-'])

sg.popup(resultado)
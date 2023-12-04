#interface gráfica

import PySimpleGUI as psg

import calc2
from calc2 import sub

layout =     [
                 [psg.Text('Informe o Primeiro Número: '), psg.InputText(key='num1')],
                 [psg.Text('Informe o Primeiro Número: '), psg.InputText(key='num2')],
                 [psg.Text('Adição:'), psg.Text('', key='adição')],
                 [psg.Text('Subtração:'), psg.Text('', key='subtração')],
                 [psg.Text('Multiplicação:'), psg.Text('', key='multiplicação')],
                 [psg.Text('Divisão:'), psg.Text('', key='divisão')],
                 [psg.Button('calcular:'), psg.Button('limpar')],
             ]

janela = psg.Window('calculadora simples', layout)

while True:
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'limpar':
        janela['num1'].update('')
        janela['num2'].update('')
        janela['adição'].update('')
        janela['subtração'].update('')
        janela['multiplicação'].update('')
        janela['divisão'].update('')
        janela['num1'].set_focus()
    else:
        num1 = float(valores['num1'])
        num2 = float(valores['num2'])
        janela ['adição'].update(calc2.soma(num1, num2))
        janela ['subtração'].update(calc2.sub(num1, num2))
        janela ['multiplicação'].update(calc2.multi(num1, num2))
        janela ['divisão'].update(calc2.div(num1, num2))

janela.close()
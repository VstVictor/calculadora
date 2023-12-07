# Interface Gráfica
import PySimpleGUI as psg
from calc2 import soma, sub, multi, div

layout = [
    [psg.Text('Escolha a Operação:')],
    [psg.Radio('Adição', 'operacao', key='adição'), psg.Radio('Subtração', 'operacao', key='subtracao')],
    [psg.Radio('Multiplicação', 'operacao', key='multiplicacao'), psg.Radio('Divisão', 'operacao', key='divisao')],
    [psg.Text('Informe o Primeiro Número: '), psg.InputText(key='num1')],
    [psg.Text('Informe o Segundo Número: '), psg.InputText(key='num2')],
    [psg.Text('Resultado:'), psg.Text('', key='resultado')],
    [psg.Button('Calcular'), psg.Button('Limpar'), psg.Button('Sair', button_color=('white', 'red'))],
]

janela = psg.Window('Calculadora Simples', layout)

while True:
    evento, valores = janela.read()

    if evento == psg.WIN_CLOSED or evento == 'Sair':
        break
    elif evento == 'Limpar':
        for key in ['num1', 'num2', 'resultado']:
            janela[key].update('')
        janela['num1'].set_focus()
    elif evento == 'Calcular':
        num1_str = valores['num1']
        num2_str = valores['num2']

        if not num1_str or not num2_str:
            psg.popup_error("Informe valores para os dois números.")
            continue

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            psg.popup_error("Os valores informados não são números válidos.")
            continue

        operacao = None

        for op in ['adição', 'subtracao', 'multiplicacao', 'divisao']:
            if valores[op]:
                operacao = op
                break

        if operacao is not None:
            if operacao == 'adição':
                resultado = soma(num1, num2)
                janela['resultado'].update(f'{num1} + {num2} = {resultado}')
            elif operacao == 'subtracao':
                resultado = sub(num1, num2)
                janela['resultado'].update(f'{num1} - {num2} = {resultado}')
            elif operacao == 'multiplicacao':
                resultado = multi(num1, num2)
                janela['resultado'].update(f'{num1} * {num2} = {resultado}')
            elif operacao == 'divisao':
                if num2 != 0:
                    resultado = div(num1, num2)
                    janela['resultado'].update(f'{num1} / {num2} = {resultado}')
                else:
                    janela['resultado'].update(f'{num1} / {num2} = 0')
        else:
            psg.popup_error("Escolha uma operação antes de calcular!")

janela.close()

import requests
import json
import pandas as pd
from time import sleep
import PySimpleGUI as sg
import threading

def janela():

    sg.theme('Python')

    layout = [[sg.Text('Eleições 2022')],
              [sg.Text('DADOS')],
              [sg.Image('ladrao.png', size=(500, 150))],
              [sg.Output(size=(70, 6), key='saida')],
              [sg.Image('mito.png', size=(500, 150))],
              [sg.Button('Iniciar'), sg.Exit()]]

    window = sg.Window('ELEIÇÕES 20*22*', layout, element_justification='c')

    while True:  # The Event Loop
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Iniciar':
            window.perform_long_operation(pega_dados_exibe, 's')
            window.refresh() if window else None
            window.FindElement('saida').Update('')
            window.refresh() if window else None

    window.close()


def pega_dados_exibe():

    data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')

    json_data = json.loads(data.content)

    candidato2 = []
    partido2 = []
    votos2 = []
    porcentagem2 = []

    candidato1 = []
    partido1 = []
    votos1 = []
    porcentagem1 = []

    while True:

        sleep(5)

        for informacoes in json_data['cand']:

            if informacoes['n'] in ['13']:
                candidato2.append('LULA LADRAOOO')
                votos2.append(informacoes['vap'])
                porcentagem2.append(informacoes['pvap'])

            if informacoes['n'] in ['22']:
                candidato1.append("BOLSONARO MITO")
                votos1.append(informacoes['vap'])
                porcentagem1.append(informacoes['pvap'])

        df_eleicao1 = pd.DataFrame(list(zip(candidato1, votos1, porcentagem1)), columns=[
            'Candidato', 'Votos', 'Porcentagem'
        ])
        df_eleicao2 = pd.DataFrame(list(zip(candidato2, votos2, porcentagem2)), columns=[
            'Candidato', 'Votos', 'Porcentagem'
        ])

        print(df_eleicao1)
        print('')
        print(df_eleicao2)

        candidato2 = []
        partido2 = []
        votos2 = []
        porcentagem2 = []

        candidato1 = []
        partido1 = []
        votos1 = []
        porcentagem1 = []


janela()

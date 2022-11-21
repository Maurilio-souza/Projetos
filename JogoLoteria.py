'''
Faça um programa que pergunta qual loteria, quantos jogos e quantos números o
usuário quer jogar,com as informações preenchidas faça o jogo marcando os 
numeros aleatoriamente com random e informe o valor total da aposta.
usar o conteudo estudado no modulo 1: if, elif, else while e for.
'''

import random
import os
while True:
    
    print('SEJA BEM VINDO A LOTERICA GANHE E SEJA MILIONARIO!')
    print('\nTEMOS DISPONIVEL PARA APOSTA:')
    print('| MS-MEGA-SENA | LF-LOTOFÁCIL | QN-QUINA | LM-LOTOMANIA | DS-DUPLA SENA |')
    loteria = input('\n DIGITE AS INICIAIS DA LOTERIA QUE QUER APOSTAR: ').upper()
    os.system('clear')
    if loteria == 'MS':
        loteria = 'MEGA-SENA'
        print('Loteria escolhida: MEGA SENA')
        qtde_jogos = int(input('Digite a quantidade de aposta que quer apostar: '))
        
        while True:
            qtde_bolas = int(input('Digite a quantidade de números que que marcar por aposta de 06 a 20: '))
            os.system('clear')
            if qtde_bolas == 6:
                valor_aposta = qtde_jogos* 4.50
                break
            elif qtde_bolas == 7:
                valor_aposta = qtde_jogos* 31.50
                break
            elif qtde_bolas == 8:
                valor_aposta = qtde_jogos* 126
                break
            elif qtde_bolas == 9:
                valor_aposta = qtde_jogos* 378
                break
            elif qtde_bolas == 10:
                valor_aposta = qtde_jogos* 945
                break
            elif qtde_bolas == 11:
                valor_aposta = qtde_jogos* 2079
                break
            elif qtde_bolas == 12:
                valor_aposta = qtde_jogos* 4158
                break
            elif qtde_bolas == 13:
                valor_aposta = qtde_jogos* 7222
                break
            elif qtde_bolas == 14:
                valor_aposta = qtde_jogos* 13513.50
                break
            elif qtde_bolas == 15:
                valor_aposta = qtde_jogos* 22522.50
                break
            elif qtde_bolas == 16:
                valor_aposta = qtde_jogos* 36036
                break
            elif qtde_bolas == 17:
                valor_aposta = qtde_jogos* 55692
                break
            elif qtde_bolas == 18:
                valor_aposta = qtde_jogos* 83538
                break
            elif qtde_bolas == 19:
                valor_aposta = qtde_jogos* 122094
                break
            elif qtde_bolas == 20:
                valor_aposta = qtde_jogos* 174420
                break
            else:
                print('Opção inválida só é possivel marcar de 6 a 20 números por aposta.')
         
        range_loteria_a = (1)
        range_loteria_b = (60)
        break

    elif loteria == 'LF':
        loteria = 'LOTOFÁCIL'
        print('Loteria escolhida: LOTOFÁCIL')
        qtde_jogos = int(input('Digite a quantidade de aposta que quer apostar: '))
        
        while True:
            qtde_bolas = int(input('Digite a quantidade de números que que marcar por aposta de 15 a 20: '))
            os.system('clear')
            if qtde_bolas == 15:
                valor_aposta = qtde_jogos* 2.50
                break
            elif qtde_bolas == 16:
                valor_aposta = qtde_jogos* 40
                break
            elif qtde_bolas == 17:
                valor_aposta = qtde_jogos* 340
                break
            elif qtde_bolas == 18:
                valor_aposta = qtde_jogos* 2040
                break
            elif qtde_bolas == 19:
                valor_aposta = qtde_jogos* 9690
                break
            elif qtde_bolas == 20:
                valor_aposta = qtde_jogos* 38760
                break
            else:
                print('Opção inválida só é possivel marcar de 15 a 20 números por aposta.')

        range_loteria_a = (1)
        range_loteria_b = (25)
        break

    elif loteria == 'QN':
        print('Loteria escolhida: QUINA')
        loteria = 'QUINA'
        qtde_jogos = int(input('Digite a quantidade de aposta que quer apostar: '))
        
        while True:
            qtde_bolas = int(input('Digite a quantidade de números que que marcar por aposta de 06 a 15: '))
            os.system('clear')
            if qtde_bolas == 5:
                valor_aposta = qtde_jogos* 2.00
                break
            elif qtde_bolas == 6:
                valor_aposta = qtde_jogos* 12
                break
            elif qtde_bolas == 7:
                valor_aposta = qtde_jogos* 42
                break
            elif qtde_bolas == 8:
                valor_aposta = qtde_jogos* 112
                break
            elif qtde_bolas == 9:
                valor_aposta = qtde_jogos* 252
                break
            elif qtde_bolas == 10:
                valor_aposta = qtde_jogos* 504
                break
            elif qtde_bolas == 11:
                valor_aposta = qtde_jogos* 924
                break
            elif qtde_bolas == 12:
                valor_aposta = qtde_jogos* 1584
                break
            elif qtde_bolas == 13:
                valor_aposta = qtde_jogos* 2574
                break
            elif qtde_bolas == 14:
                valor_aposta = qtde_jogos* 4004
                break
            elif qtde_bolas == 15:
                valor_aposta = qtde_jogos* 6006
                break
 
            else:
                print('Opção inválida só é possivel marcar de 5 a 15 números por aposta.')
                
        range_loteria_a = (1)
        range_loteria_b = (80)
        break
            
    elif loteria == 'LM':
        loteria = 'LOTOMANIA'
        print('Loteria escolhida: LOTOMANIA')
        qtde_jogos = int(input('Digite a quantidade de aposta que quer apostar: '))
        valor_aposta = qtde_jogos* 2.50
        qtde_bolas = 50
        range_loteria_a = (0)
        range_loteria_b = (99)
        break

    elif loteria == 'DS':
        loteria = 'DUPLA SENA'
        print('Loteria escolhida: DUPLA SENA')
        qtde_jogos = int(input('Digite a quantidade de aposta que quer apostar: '))
        
        while True:
            qtde_bolas = int(input('Digite a quantidade de números que que marcar por aposta de 06 a 15: '))
            os.system('clear')
         
            if qtde_bolas == 6:
                valor_aposta = qtde_jogos* 2.5
                break
            elif qtde_bolas == 7:
                valor_aposta = qtde_jogos* 17.5
                break
            elif qtde_bolas == 8:
                valor_aposta = qtde_jogos* 70
                break
            elif qtde_bolas == 9:
                valor_aposta = qtde_jogos* 210
                break
            elif qtde_bolas == 10:
                valor_aposta = qtde_jogos* 525
                break
            elif qtde_bolas == 11:
                valor_aposta = qtde_jogos* 1155
                break
            elif qtde_bolas == 12:
                valor_aposta = qtde_jogos* 2310
                break
            elif qtde_bolas == 13:
                valor_aposta = qtde_jogos* 4290
                break
            elif qtde_bolas == 14:
                valor_aposta = qtde_jogos* 7207.50
                break
            elif qtde_bolas == 15:
                valor_aposta = qtde_jogos* 12512.50
                break
 
            else:
                print('Opção inválida só é possivel marcar de 6 a 15 números por aposta.')
                
        range_loteria_a = (1)
        range_loteria_b = (50)
        break
            
    else:
        print('Opção inválida digite a inicial da loteria conforme exemplo:  digite "MS" para apostar na MEGA-SENA.\n')

valor_jogo = valor_aposta/qtde_jogos

print(F'Apostas registradas na loteria "{loteria}"!!!')
print(f'\nForam registradas {qtde_jogos} apostas de {qtde_bolas} números')
print(f'Cada aposta custa R${valor_jogo:.2f} custo total das apostas R${valor_aposta:.2f}.\n')

pacote_jogos = []
while len(pacote_jogos) < qtde_jogos:
    jogo = []
    while len(jogo) < qtde_bolas:
        bola = random.randint(range_loteria_a,range_loteria_b)
        if bola not in jogo:
            jogo.append(bola)
        jogo.sort()
    if jogo not in pacote_jogos:
        pacote_jogos.append(jogo)
    pacote_jogos.sort()
for i in range (len(pacote_jogos)):
    print(f'\n{i+1}º Jogo: {pacote_jogos[i]}')
print('\nBoa Sorte!!!')    
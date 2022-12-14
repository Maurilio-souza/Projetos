# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
# ou em galões de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#a- comprar apenas latas de 18 litros;
#B- comprar apenas galões de 3,6 litros;
#C- misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area_pintada = float(input('\nDigite a área a ser pintada em m²: '))
margem_10_porcento = 1.1 
area_litro = 6 
litros = area_pintada/area_litro 
lata = 18 
galao = 3.6 
resto_lata = litros % lata
custo_lata = 80
custo_galao = 25
resto_galao = litros % galao

#A Apenas lata:
latas = litros/lata
if litros%lata != 0:
    latas = litros//lata + 1
print('\nAlternativa A')
print(f'\nSerá preciso {litros:.2f}l de tinta.')
print(f'Comprando só latas irá precisar de {latas:.0f} latas de tinta.')
print(f'Irá sobrar {(lata*latas -litros):.2f}l de tinta.')
print(f'custo total de R${latas*custo_lata:.2f}.')


#B Apenas galão
galoes = litros/galao
if litros%galao != 0:
    galoes = litros//galao + 1
print('\nAlternativa B')
print(f'\nSerá preciso {litros:.2f}l de tinta.')
print(f'Comprando só galoes irá precisar de {galoes:.0f} galões de tinta.')
print(f'Irá sobrar {(galao*galoes-litros):.2f}l de tinta.')
print(f'custo total de R${galoes*custo_galao:.2f}.')


#C Latas e galoes
litros = (area_pintada/area_litro)*margem_10_porcento
resto_lata = litros % lata
qtde_lata = litros//lata
qtde_galao = resto_lata//galao + 1
custo_total = qtde_lata*custo_lata + qtde_galao*custo_galao

if int(resto_lata) == 0:
    resto_lata = litros % lata
    qtde_galao = 0

if area_pintada < 6:
    qtde_galao = 1

sobra_tinta = ((qtde_galao*galao)+(qtde_lata*lata))-litros
if sobra_tinta < 0:
    sobra_tinta = 0

print('\nAlternativa C')
print(f'\nSerá preciso {(litros):.2f}l de tinta.')
print(f'Será preciso comprar {qtde_lata:.0f} lata(s) e {qtde_galao:.0f} galão(ões) de tinta.')
print(f'Irá sobrar {sobra_tinta:.2f}l de tinta.')
print(f'O custo total é: R${custo_total:.2f}.')

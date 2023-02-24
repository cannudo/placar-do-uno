'''
[PLACAR DO UNO]: script que ajuda a contar o placar do UNO.

O placar do UNO é contado somando-se os valores das cartas que sobraram 
nas mão dos outros jogadores após o ganhador se livrar de todas as cartas.

Defina o placar que deve parar a execução do programa na variável FINAL.
'''

FINAL = 500

qtd = int(input(f'...\nQuantos jogadores participarão? ~~> '))
plural = 'jogadores' if qtd > 1 else 'jogador'

print(f'[{qtd} {plural}]... OK\n')

high = 0

lista = []

for i in range(qtd):
    nome = input(f'Digite o nome do jogador {i} ~~> ')
    lista.append(
        {"nome": nome, "pontos": 0}
    )
print(f'[nomes coletados]... OK\n')

cont = 0
while high < FINAL - 1:
    ganhador = input(f'[RODADA {cont}]: quem ganhou? ~~> ')
    pontos = int(input(f'[{ganhador}] fez quantos pontos? ~~> '))
    print(f'[ganhador coletado]... OK\n[pontos coletados]... OK\n')

    for i in range(qtd):
        if lista[i]['pontos'] > high:
            high = lista[i]['pontos']

    for i in range(qtd):
        if lista[i]['nome'] == ganhador:
            lista[i]['pontos'] = lista[i]['pontos'] + pontos

    print(f'[PLACAR]')
    for i in range(qtd):
        print(f'\t{lista[i]["nome"]}: {lista[i]["pontos"]} pontos')
    print(f'')

    cont = cont + 1

print(f'[ganhador]: jogador {lista[i]["nome"]}, com {lista[i]["pontos"]} pontos.')
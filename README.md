# placar-do-uno
Script CLI, feito em Python, para registrar o placar do UNO

## Curiosidade

Em um caso de teste, o programa tem a seguinte interação com o usuário:

```console
➜ placar-do-uno (main) ✗ python3 script.py 
----------------------------------------------

Quantos jogadores participarão? ~~> 2
[2 jogadores]... OK

----------------------------------------------

Digite o nome do jogador 0 ~~> ex1

Digite o nome do jogador 1 ~~> ex2

[nomes coletados]... OK

----------------------------------------------

[RODADA 0]: quem ganhou? ~~> ex2
[ex2] fez quantos pontos? ~~> 40

[ganhador coletado]... OK
[pontos coletados]... OK

----------------------------------------------
[                   PLACAR                   ]

ex1: 0 pontos

ex2: 40 pontos
----------------------------------------------

[RODADA 1]: quem ganhou? ~~> ex1
[ex1] fez quantos pontos? ~~> 5+9+2
Traceback (most recent call last):
  File "script.py", line 33, in <module>
    pontos = int(input(f'[{ganhador}] fez quantos pontos? ~~> '))
ValueError: invalid literal for int() with base 10: '5+9+2'
```
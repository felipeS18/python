from random import randint

cabecalio = '''

      ░░███          ░░███                                             
       ░███   ██████  ░███ █████  ██████  ████████   ████████   ██████ 
       ░███  ███░░███ ░███░░███  ███░░███░░███░░███ ░░███░░███ ███░░███
       ░███ ░███ ░███ ░██████░  ░███████  ░███ ░███  ░███ ░███░███ ░███
 ███   ░███ ░███ ░███ ░███░░███ ░███░░░   ░███ ░███  ░███ ░███░███ ░███
░░████████  ░░██████  ████ █████░░██████  ████ █████ ░███████ ░░██████ 
 ░░░░░░░░    ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░ ░░░░░  ░███░░░   ░░░░░░  
                                                     ░███              
                                                     █████             
                                                    ░░░░░                  
'''
menu = '''
[1] Pedra
[2] Papel
[3] Tesoura
qual você joga?
'''
valor = randint(1, 3)
print(cabecalio)
opcao = int(input(menu))

if opcao >= 1 and opcao <= 3:
    print('Jogada Valida')
    if opcao == valor:
        print('Empate!')
    elif (opcao == 1 and valor == 3 or opcao == 2 and valor == 1 or opcao == 3 and valor == 2):
        print('Você Venceu!')
    else:
        print('Você Perdeu!')

else:
    print('Jogada Invalida')

if opcao == 1:
    print('Você jogou Pedra')
elif opcao == 2:
    print('Você jogou Papel')
elif opcao == 3:
    print('Você jogou Tesoura')

if valor == 1:
    print('Adversario jogou Pedra')
elif valor == 2:
    print('Adversario jogou Papel')
elif valor == 3:
    print('Adversario jogou Tesoura')


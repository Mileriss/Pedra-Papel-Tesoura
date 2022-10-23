import os

os.system('cls')

print("PEDRA - PAPEL - TESOURA") 
pedra = 1
papel = 2
tesoura = 3


print("Selecione o NUMERO correspondente a opção!\n")
#Selecionando a opção para o jogo (Jogador 1)
jogador1 = int(input("Jogador 1 \nSelecione um item: \n1 - PEDRA\n2 - PAPEL\n3 - TESOURA\n\nDigite aqui: "))

if (jogador1 == 1):
    print("Jogador 1 selecionou: PEDRA\n")
elif (jogador1 == 2):
        print("Jogador 1 selecionou: PAPEL\n")
elif (jogador1 == 3):
    print("Jogador 1 selecionou: TESOURA\n")
else:
    print("Operacao invalida!\n")
os.system('pause'),os.system('cls')


print("Selecione o NUMERO correspondente a opção!\n")
#Selecionando a opção para o jogo (Jogador 2)
jogador2 = int(input("Jogador 2 \nSelecione um item: \n1 - PEDRA\n2 - PAPEL\n3 - TESOURA\n\nDigite aqui: "))

if (jogador2 == 1):
    print("Jogador 2 selecionou: PEDRA\n")
elif (jogador2 == 2):
        print("Jogador 2 selecionou: PAPEL\n")
elif (jogador2 == 3):
    print("Jogador 2 selecionou: TESOURA\n")
else:
    print("Operacao invalida!\n")
os.system('pause'),os.system('cls')


#Condições para VITÓRIA (JOGADOR 1)
if (jogador1 == pedra and jogador2 == tesoura
    or jogador1 == tesoura and jogador2 == papel 
        or jogador1 == papel and jogador2 == pedra):
    print("Jogador 1 venceu!\n")

#Condições para VITÓRIA (JOGADOR 2)
elif (jogador2 == pedra and jogador1 == tesoura
    or jogador2 == tesoura and jogador1 == papel
        or jogador2 == papel and jogador1 == pedra):
    print("Jogador 2 venceu!\n")
else:
    print("\nEmpate!")
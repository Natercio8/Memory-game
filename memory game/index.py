import random

r = random.random
print("Jogo da Memória\n")

print("Digite todos os números que forem informados pelo computador\n")
nome = str(input("Digite o seu nome: "))

print("\n"*100)
escolha = int(10*r())

print("Computador: {}".format(escolha))
a = str(escolha)

user = str(int(input("{}: ".format(nome))))

while user == a:
    escolha = int(10*r())
    
    print("Computador: {}".format(escolha))
    a = a + str(escolha)

    user = str(int(input("{}: ").format(nome)))
    print("\n"*100)

print("Você perdeu!")
print("Seu saldo: ",len(a))

arq = open("Classificação.txt",'a')
arq.write("\n{} \n".format(nome))
arq.write("Pontos: {}".format(len(a)))
arq.write("\n-----------------------\n")
arq.close()

input("\nPressiona Enter")
"""
Um mini sistema de criptografia desenvolvido em Python para fins de estudo e prática de lógica de programação.
"""

from crypto import criptografar, descriptografar


print("==== MINI COFRE ====")
print("1 - Criptografar arquivo")
print("2 - Descriptografar arquivo")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    nome = input("Digite o nome do arquivo: ")
    criptografar(nome)

elif opcao == "2":
    nome = input("Digite o nome do arquivo: ")
    descriptografar(nome)

else:
    print("Opção inválida.")


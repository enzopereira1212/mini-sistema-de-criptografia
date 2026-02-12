"""
sistema criado apenas para estudo de criptografia de dados e nada mais
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

from cryptography.fernet import Fernet
import os

VAULT_DIR = "vault"
KEY_FILE = "vault/key.txt"

def gerar_chave():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def carregar_chave():
    with open(KEY_FILE, "rb") as f:
        return f.read()

def criptografar(arquivo):


    if not os.path.exists(VAULT_DIR):
        os.makedirs(VAULT_DIR)

    key = gerar_chave()
    print("Sua chave é:")
    print(key.decode())

    fernet = Fernet(key)

    if not os.path.exists(arquivo):
        print("Arquivo não encontrado.")
        return

    with open(arquivo, "rb") as f:
        dados = f.read()

    dados_criptografados = fernet.encrypt(dados)

    nome_arquivo = os.path.basename(arquivo)
    caminho_vault = os.path.join(VAULT_DIR, nome_arquivo)

    with open(caminho_vault, "wb") as f:
        f.write(dados_criptografados)

    os.remove(arquivo)

    print("Arquivo criptografado com sucesso!")
    print("Chave salva em key.txt")

def descriptografar(arquivo):

    nome_arquivo = os.path.basename(arquivo)
    caminho_vault = os.path.join(VAULT_DIR, nome_arquivo)

    if not os.path.exists(caminho_vault):
        print("Arquivo não encontrado no vault.")
        return

    key = carregar_chave()

    chave_digitada = input("Digite a chave: ").encode()

    if chave_digitada != key:
        print("Chave incorreta!")
        return

    fernet = Fernet(key)

    with open(caminho_vault, "rb") as f:
        dados = f.read()

    dados_originais = fernet.decrypt(dados)

    with open(arquivo, "wb") as f:
        f.write(dados_originais)

    os.remove(caminho_vault)

    print("Arquivo restaurado com sucesso!")


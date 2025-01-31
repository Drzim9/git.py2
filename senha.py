import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho = int(input("Digite o tamanho da senha que deseja: "))
senha_gerada = gerar_senha(tamanho)
print(f"Sua senha gerada é: {senha_gerada}")

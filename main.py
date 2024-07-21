import random
from time import sleep
import string

maiusculas = ["a", "e", "i", "o", "u", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
minusculas = [ "A", "E", "I", "O", "U", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
especiais = ["!", "@", "#", "$", "%", "^", "&", "*"]
senha = ""
sorteio_itens = [maiusculas,minusculas,numeros,especiais]

valido_maiuscula = 0
valido_minuscula = 0
valido_numero = 0
valido_especial = 0


def erro(text_erro):
    print(text_erro)
    criar_senha()


def sortear(item):
    global senha
    item_sorteado = random.choices(item)
    senha += item_sorteado[0]
    

def identificar_tipo_caractere(char):
    global valido_maiuscula, valido_minuscula, valido_numero, valido_especial
    if char.isupper():
        print("Letra Maiúscula")
        valido_maiuscula = 1
    elif char.islower():
        print("Letra Minúscula")
        valido_minuscula = 1
    elif char.isdigit():
        print("Número")
        valido_numero = 1
    elif char in string.punctuation:
        print("Caracter Especial")
        valido_especial = 1
    else:
        print("Outro Tipo")


def alterar_senha():
    alt_senha = int(input("Digite 1 para alterar sua senha. \nDigite 2 se deseja pular \n"))
    if alt_senha == 1:
        criar_senha()
    elif alt_senha == 2:
        print("Muito obrigada! Áte outra hora.")
        exit
    else:
        print("Opção não valida!")
        alterar_senha()


def gerar_senha():
    global senha
    senha = "" 
    sortear(maiusculas)
    sortear(minusculas)
    sortear(numeros)
    sortear(especiais)
    for x in range(4):
        item = random.choices(sorteio_itens)
        sortear(item[0])        
    print(f"Sua senha é: {senha}")
    sleep(3)
    alterar_senha()
    

def criar_senha():
    global senha, valido_maiuscula, valido_minuscula, valido_numero, valido_especial
    valida = input("Digite a senha antiga: ")
    if valida == senha:
        nova = input("Digite a senha nova: ")
        rep_nova = input("Digite a senha novamente: ")
        if nova == rep_nova:
            for char in nova:
                identificar_tipo_caractere(char)
                print(char)
            if(
                valido_maiuscula == 1 and 
                valido_minuscula == 1 and 
                valido_numero == 1 and 
                valido_especial == 1
                ):
                print("Senha modificada com sucesso!")
                senha = nova
            else:
                erro("Sua senha nova precisa ter Letras maiusculas e minusculas, números e caracteres especiais")
        else:
            erro("As senhas novas não coicidêm")
    else:
        erro("A senha antiga está incorreta")


gerar_senha()
import random
def jogar():
    apresentacao()

    palavra_secreta = determinando_palavra()

    enforcou = False
    acertou = False
    erros = 0

    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            aparece_letra_certa(palavra_secreta, chute, letras_acertadas)

        else:
            erros += 1
            desenha_forca(erros)
            enforcou = contabiliza_erros(erros)

        acertou = venceu(letras_acertadas)








def apresentacao():
    print("------------")
    print("Bem vindo ao jogod e forca!")
    print("------------\n")



def determinando_palavra():
    palavras = []
    tema = int(input("Escolha um tema: (1)Times de futebol (2)Países (3)Frutas"))

    if tema == 1:
        palavras = ["palmeiras", "barcelona", "liverpool", "santos", "fortaleza", "corinthians", "newcastle", "arsenal",
                    "napoli", "bahia", "vasco"]
    if tema == 2:
        palavras = ["luxemburgo", "marrocos", "coreia", "espanha", "portugal", "holanda", "irlanda", "cazaquistao",
                    "paquistao", "india", "islandia"]
    if tema == 3:
        palavras = ["melancia", "banana", "kiwi", "morango", "damasco", "lixia", "jaca", "maracuja"]
    posicao_da_palavra = random.randrange(0, len(palavras))
    palavra_secreta = palavras[posicao_da_palavra].upper()
    return palavra_secreta





def mostra_caracteres(palavra):
    return ["_" for letra in palavra]





def pede_chute():
    chute = input("Digite uma letra: ").upper()
    chute = chute.strip()
    return chute





def aparece_letra_certa(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
            print(letras_acertadas)
        index += 1





def venceu(letras_acertadas):
    acertou = "_" not in letras_acertadas
    if acertou:
        print("PARABENS AMOR, VC MERECE UM BEIJO MEU")
        print("╔══╗♥")
        print("╚╗╔╝♥")
        print("╔╝╚╗♥")
        print("╚══╝♥")
        print("╔╗ ♥ღ♥ღ♥ღ♥")
        print("║║╔═╦╦╦╔╗")
        print("║╚╣║║║║╔╣")
        print("╚═╩═╩═╩═╝")
        print("╔╗╔╗♥")
        print("║║║║♥")
        print("║║║║♥")
        print("╚══╝♥")
        #print("░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░")
        #print("░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░")
        #print("░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░")
        #print("░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░")
        #print("░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░")
        #print("░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██")
        #print("░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
        #print("░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██")
        #print("░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██")
        #print("██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██")
        #print("█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██")
        #print("██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░")
        #rint("░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░")
        #print("░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░")
        #print("░░████████████░░░█████████████████░░░░░░")
    return acertou





def contabiliza_erros(erros):
    print("Não existe essa letra, vc tem {} tentativas restantes".format(7 - erros))
    if erros >= 7:
        print("voce mamou")
        print("███████████████████████████")
        print("███████▀▀▀░░░░░░░▀▀▀███████")
        print("████▀░░░░░░░░░░░░░░░░░▀████")
        print("███│░░░░░░░░░░░░░░░░░░░│███")
        print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
        print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
        print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
        print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
        print("██▌░│██████▌░░░▐██████│░▐██")
        print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
        print("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
        print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
        print("████▄─┘██▌░░░░░░░▐██└─▄████")
        print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
        print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
        print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
        print("███████▄░░░░░░░░░░░▄███████")
        print("██████████▄▄▄▄▄▄▄██████████")
        enforcou = True
        return enforcou



def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")

jogar()




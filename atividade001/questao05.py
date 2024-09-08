import random

def pegar_palavras_arquivo(arquivo):

    try:
        with open(arquivo, 'r') as file:
            palavras = file.readlines()

        palavras = [palavra.strip().upper() for palavra in palavras]
        return palavras

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []


def escolher_palavra(palavras):

    return random.choice(palavras)


def mostrar_jogo(palavra, letras_certas):

    return ' '.join([letra if letra in letras_certas else '_' for letra in palavra])


def jogo_da_forca():

    arquivo = r'C:\Users\ENZO\Desktop\jogo_da_forca\jogo_da_forca.txt'

    palavras = pegar_palavras_arquivo(arquivo)
    if not palavras:
        return

    palavra_do_jogo = escolher_palavra(palavras)
    letras_certas = set()
    erros = 0
    tentativas = 6

    while erros < tentativas:
        print("\nPalavra da vez:", mostrar_jogo(palavra_do_jogo, letras_certas))
        letra = input("\nDigite uma letra: ").strip().upper()

        if letra in palavra_do_jogo:
            letras_certas.add(letra)
            print("Letra correta.")

            if set(palavra_do_jogo) == letras_certas:
                print("\nAcertou a palavra:", palavra_do_jogo)
                break

        else:
            erros += 1
            print(f"{erros}° erro. Tente novamente.!")

    if erros == tentativas:
        print("\nVocê perdeu! A palavra era:", palavra_do_jogo)


if __name__ == "__main__":
    jogo_da_forca()

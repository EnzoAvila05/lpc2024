def palindromo(texto):
    texto_sem_espacos = texto.replace(" ", "").lower()

    return texto_sem_espacos == texto_sem_espacos[::-1]


def main():

    texto = input("Digite uma frase: ")

    print(f"{texto}")
    if palindromo(texto):
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")


if __name__ == "__main__":
    main()

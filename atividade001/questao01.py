import random

def lancar_dados():

    return random.randint(1, 6)


def armazenar_lancamentos_dados(numero_lancamentos):

    lancamentos = []

    for i in range(numero_lancamentos):
        resultado = lancar_dados()
        lancamentos.append(resultado)

    contadores = [0, 0, 0, 0, 0, 0]

    for resultado in lancamentos:
        contadores[resultado - 1] += 1

    return contadores


def main():
    numero_lancamentos = 100
    contadores = armazenar_lancamentos_dados(numero_lancamentos)

    for i in range(6):
        print(f"Número {i + 1}: {contadores[i]} vezes")


if __name__ == "__main__":
    main()

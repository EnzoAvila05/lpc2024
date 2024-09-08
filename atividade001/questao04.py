def numero_por_extenso(numero):

    unidades = {
        0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco",
        6: "seis", 7: "sete", 8: "oito", 9: "nove"
    }

    diferentes = {
        10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "catorze",
        15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito",
        19: "dezenove"
    }

    dezenas = {
        20: "vinte", 30: "trinta", 40: "quarenta", 50: "cinquenta",
        60: "sessenta", 70: "setenta", 80: "oitenta", 90: "noventa"
    }

    if numero in unidades:
        return unidades[numero]
    elif numero in diferentes:
        return diferentes[numero]
    else:
        dezena = (numero // 10) * 10
        unidade = numero % 10
        if unidade == 0:
            return dezenas[dezena]
        else:
            return f"{dezenas[dezena]} e {unidades[unidade]}"


def main():

    numero = int(input("Digite um número de 1 à 99: "))

    print(numero_por_extenso(numero))


if __name__ == "__main__":
    main()

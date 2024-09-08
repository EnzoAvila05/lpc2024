def formato_cpf(cpf):

    if len(cpf) != 14:
        return False

    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False

    for i in range(len(cpf)):
        if i in [3, 7, 11]:
            continue
        if not cpf[i].isdigit():
            return False

    return True


def calcular_digitos_verificadores(cpf):

    somente_numeros_cpf = [int(char) for char in cpf if char.isdigit()]

    #Primeiro Dígito
    soma_primeiro = 0
    for i in range(9):
        soma_primeiro += somente_numeros_cpf[i] * (10 - i)


    primeiro_digito = 11 - (soma_primeiro % 11)
    if primeiro_digito > 9:
        primeiro_digito = 0

    #Segundo dígito
    soma_segundo = 0
    for i in range(10):
        soma_segundo += somente_numeros_cpf[i] * (11 - i)

    segundo_digito = 11 - (soma_segundo % 11)
    if segundo_digito > 9:
        segundo_digito = 0

    return primeiro_digito, segundo_digito


def validar_cpf(cpf):

    if not formato_cpf(cpf):
        return False

    digitos_verificadores = calcular_digitos_verificadores(cpf)
    digitos_usuario = (int(cpf[12]), int(cpf[13]))

    return digitos_verificadores == digitos_usuario


def main():

    cpf = input("Digite o CPF no formato xxx.xxx.xxx-xx: ")

    if validar_cpf(cpf):
        print("CPF válido.")
    else:
        print("CPF inválido.")


if __name__ == "__main__":
    main()

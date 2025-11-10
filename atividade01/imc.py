def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("altura deve ser maior que zero")
    if peso <= 0:
        raise ValueError("peso deve ser maior que zero")
    imc = peso / (altura ** 2)
    return round(imc, 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    if 18.5 <= imc < 25.0:
        return "Peso normal"
    if 25.0 <= imc < 30.0:
        return "Sobrepeso"
    if 30.0 <= imc < 35.0:
        return "Obesidade grau I"
    if 35.0 <= imc < 40.0:
        return "Obesidade grau II"
    return "Obesidade grau III"

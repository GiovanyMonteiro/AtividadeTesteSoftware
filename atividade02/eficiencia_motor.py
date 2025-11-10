def calcular_eficiencia(potencia_saida, potencia_entrada):
    if potencia_entrada <= 0:
        raise ValueError("potencia_entrada deve ser maior que zero")
    eficiencia = (potencia_saida / potencia_entrada) * 100
    return round(eficiencia, 1)


def classificar_eficiencia(eficiencia):
    if eficiencia < 80.0:
        return "IE1 - Baixa eficiência"
    if eficiencia < 90.0:
        return "IE2 - Eficiência média"
    return "IE3 - Alta eficiência"


def analise_motor(potencia_saida, potencia_entrada):
    eficiencia = calcular_eficiencia(potencia_saida, potencia_entrada)
    classificacao = classificar_eficiencia(eficiencia)
    return eficiencia, classificacao

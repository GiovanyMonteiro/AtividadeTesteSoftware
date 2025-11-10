import pytest
from imc import calcular_imc, classificar_imc


def test_calcular_imc_valor():
    assert calcular_imc(70, 1.75) == 22.86


def test_calculo_arredonda_duas_casas():
    assert calcular_imc(65, 1.7) == 22.49


def test_altura_zero_gera_value_error():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)


def test_classificar_abaixo_peso():
    assert classificar_imc(17.9) == "Abaixo do peso"


def test_classificar_peso_normal():
    assert classificar_imc(22.0) == "Peso normal"


def test_classificar_sobrepeso():
    assert classificar_imc(27.3) == "Sobrepeso"


def test_classificar_obesidade_grau_i():
    assert classificar_imc(33.0) == "Obesidade grau I"


def test_classificar_obesidade_grau_ii():
    assert classificar_imc(37.0) == "Obesidade grau II"


def test_classificar_obesidade_grau_iii():
    assert classificar_imc(45.0) == "Obesidade grau III"

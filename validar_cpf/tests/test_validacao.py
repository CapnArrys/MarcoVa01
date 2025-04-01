import pytest

from app.validacao import validar_cpf

def teste_cpf_valido():
    assert validar_cpf("529.982.247-25") == True

def teste_cpf_valido_sem_pontos():
    assert validar_cpf("12345678909") == True

def teste_cpf_letra():
    assert validar_cpf("abc.def.ghi-jk") == False 

def teste_cpf_vazio():
    with pytest.raises(ValueError):
        validar_cpf("")

def teste_cpf_int():
    with pytest.raises(TypeError):
        validar_cpf(123)

def teste_cpf_float():
    with pytest.raises(TypeError):
        validar_cpf(5.5)

def teste_cpf_invalido():
    assert validar_cpf("123.456.789-123") == False
    assert validar_cpf("!@#.$%^.&*-()")== False
    assert validar_cpf("123.456.789-00") == False

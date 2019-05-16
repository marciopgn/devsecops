import pytest
from teste_op import somar
from teste_op import subtrair

def teste_somar():
    assert somar(2,3) == 5

def teste_subtrair():
    assert subtrair(5,3) == 2

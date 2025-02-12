import re
from validate_docbr import CPF

def cpf_invalido(numero_cpf):
   cpf = CPF()
   result = cpf.validate(numero_cpf)
   return not result

def nome_invalido(nome):
   return not nome.isalpha()

def celular_invalido(celular):
   # 86 99999-9999
   pattern = '[0-9]{2} [0-9]{5}-[0-9]{4}'
   result = re.findall(pattern, celular)
   print(result)
   return not result
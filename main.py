from validacoes.validacao_cpf import Validacao_CPF
from validate_docbr import CPF
from validate_docbr import CNPJ

exemplo_cnpj = "35379838000112"
exemplo_cpf = "71455454036"

documento = Validacao_CPF(exemplo_cnpj,"cnpj")

print(documento)
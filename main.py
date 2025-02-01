from validacoes.validacao_cpf_cnpj import Documento
from validate_docbr import CPF
from validate_docbr import CNPJ

exemplo_cnpj = "35379838000112"
exemplo_cpf = "71455454036"

documento = Documento.cria_documento(exemplo_cnpj)

print(documento)
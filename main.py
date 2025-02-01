from validacoes.validacao_cpf_cnpj import Documento
from validacoes.validacao_telefones import validacao_telefones
import re

## Validação de CPF e CNPJ atráves de uma classe factory para realizar essa validação
# exemplo_cnpj = "35379838000112"
# exemplo_cpf = "71455454036"

# documento = Documento.cria_documento(exemplo_cnpj)
# print(documento)


## Validação de Telefone e Celular
tel = "1154454698"
telefone = validacao_telefones(tel)
print(telefone)
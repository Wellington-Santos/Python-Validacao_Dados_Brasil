from validacoes.validacao_cpf_cnpj import Documento
from validacoes.validacao_telefones import validacao_telefones
from validacoes.validacao_data import validacao_data
from validacoes.validacao_endereco import Validacao_endereco


## Validação de CPF e CNPJ atráves de uma classe factory para realizar essa validação
# exemplo_cnpj = "35379838000112"
# exemplo_cpf = "71455454036"

# documento = Documento.cria_documento(exemplo_cnpj)
# print(documento)

###############################################################################################

## Validação de Telefone e Celular
# tel = "1154454698"
# telefone = validacao_telefones(tel)
# print(telefone)
###############################################################################################

## Validação de Datas em formato brasileiro
# cadastro = validacao_data()
# print(cadastro.tempo_cadastro())
###############################################################################################

## Validação de CEP
cep = "01001000"
valida_cep = Validacao_endereco(cep)
print(valida_cep)
bairro, cidade, uf = valida_cep.consulta_cep()

print("CEP: {}, Bairro: {}, Cidade: {}, UF: {}".format(cep, bairro, cidade, uf))
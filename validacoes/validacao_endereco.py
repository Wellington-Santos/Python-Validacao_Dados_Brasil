import requests


class Validacao_endereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("Cep Invalido")
        
    def __str__(self):
        return self.format_cep()

    def cep_e_valido(self,cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def format_cep(self):
        return "{}-{}".format(self.cep[:4], self.cep[4:])
    
    def consulta_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )


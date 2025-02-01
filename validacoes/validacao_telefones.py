import re

class validacao_telefones:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto!!")
        
    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        num_tel = re.search(padrao, self.numero)

        cod_pais = num_tel.group(1)
        ddd = num_tel.group(2)
        parte1 = num_tel.group(3)
        parte2 = num_tel.group(4)

        if cod_pais:
            num_formatado = "+{} ({}) {}-{}".format(cod_pais, ddd, parte1, parte2)
        else:
            num_formatado = "({}) {}-{}".format(ddd, parte1, parte2)
        return num_formatado
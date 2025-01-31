from validate_docbr import CPF
from validate_docbr import CNPJ


class Validacao_CPF:

    def __init__(self, documento, tipo_documento):
        documento = str(documento)
        self.tipo_documento = tipo_documento
        if tipo_documento == "cpf":
            if self.cpf_valida(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido !!")
            
        elif self.tipo_documento == "cnpj":
            if self.cnpj_valida(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido !!")
            
        else:
            raise ValueError("Documento inválido !!")

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.format_cpf()
        elif self.tipo_documento == "cnpj":
            return self.format_cnpj()          

    def cpf_valida(self, cpf):
        if len(cpf) == 11:
            validate_cpf = CPF()
            return validate_cpf.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos invalida")
        
    def format_cpf(self):        
        mascara = CPF()
        return mascara.mask(self.cpf)

    def cnpj_valida(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos invalida")
    
    def format_cnpj(self):        
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
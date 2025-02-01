from datetime import datetime, timedelta

class validacao_data:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()
    
    def mes_cadastro(self):
        mes_do_ano = ["Janeiro", "Fevereiro", "Março", 
                      "Abril", "Maio", "Junho", 
                      "Julho", "Agosto", "Setembro", 
                      "Outubro", "Novembro", "Dezembro"]
        
        mes_cadastro =  self.momento_cadastro.month -1
        return mes_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dia_semana = ["Segunda", "Terça", "Quarta", 
                      "Quinta", "sexta", "Sabado", 
                      "Domingo"]
        
        dia_cadastro =  self.momento_cadastro.weekday()
        return dia_semana[dia_cadastro]
    
    def format_data(self):
        data_formata = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formata
    
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30))- self.momento_cadastro
        return tempo_cadastro
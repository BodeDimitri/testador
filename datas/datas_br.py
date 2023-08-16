from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()
        
    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dia_ano = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
        dia_cadastro = self.momento_cadastro.weekday()
        return dia_ano[dia_cadastro]
    
    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro
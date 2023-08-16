from datetime import datetime, timedelta
from datas_br import DatasBr

cadastro = DatasBr()
print(cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro.formata_data())
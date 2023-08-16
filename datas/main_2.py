from datetime import datetime, timedelta

hoje  = datetime.today()
hoje_formatada = hoje.strftime("%d/%m/%y %H:%M")
print(hoje)
print(hoje_formatada)
import re

padrao = "[9][0-9]{4}-[0-9]{4}"
texto = "95430-5769"

respos = re.search(padrao, texto)
print(respos.group())

padraoemail = "\w{4,30}@[a-z]{3,10}.com.br"
texto2 = "alunofaculdade@gmail.com.br"

resposta = re.search(padraoemail, texto2)
print(resposta.group())
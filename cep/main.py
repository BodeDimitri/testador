from acesso_api import BuscaEndereço
import requests 

cep = "07700660"

objeto = BuscaEndereço(cep)

a = objeto.acessa_cep()

print(a)
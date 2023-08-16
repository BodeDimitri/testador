import requests
class BuscaEndereço:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            ValueError("CEP invalido")

    def __str__(self):
        return self.formata_cep()

    def valida_cep(self,cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def formata_cep(self):
        return "{}-{}".format(self.cep[:4], self.cep[4:])
    
    def acessa_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
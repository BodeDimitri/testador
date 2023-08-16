from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documentos(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos esta incorreta")
        
class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("cpf invalido")

    def valida(self,documento):
        validador = CPF() 
        return validador.validate(documento)
    
    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
    def __str__(self):
        return self.formata_cpf()
    
class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("cnpj invalido")

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    
    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    
    def __str__(self):
        return self.formata_cnpj()
    
import requests


class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido!")

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format(self):
        return "{}-{}".format(self.cep[0:5],self.cep[5:])

    def __str__(self):
        return  self.format()

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        resposta = requests.get(url)
        dados = resposta.json()
        return (dados['bairro'],
                dados['localidade'],
                dados['uf']
                )

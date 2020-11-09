class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibe_nome_e_sobrenome(self):
        print("{0} {1}".format(self.nome, self.sobrenome))


pessoa = Pessoa("Chalita", "Steppat")
pessoa2 = Pessoa("Chad", "Steven")

pessoa.exibe_nome_e_sobrenome()
pessoa2.exibe_nome_e_sobrenome()


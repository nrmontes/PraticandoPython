class Data:
    def __init__(self, dia, mes, ano):
        print('Formatando data..... ')
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(self.dia, self.mes, self.ano, sep='/')
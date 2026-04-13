class Lescirc:

    def __init__(self, tamanho):
        self.tamanho_max = tamanho
        self.vetor = [None] * tamanho
        self.inicio = 0
        self.fim = 0
        self.quant = 0


    def ver_prim(self):
        return self.vetor[self.inicio]

    def ver_ultimo(self):
        return self.vetor[(self.fim - 1) % self.tamanho_max]  


    def show(self):
        if self.esta_vazia():
            print('A lista está vazia')
            return

        for i in range(self.quant):
            pos = (self.inicio + i) % self.tamanho_max
            print(self.vetor[pos], end=' ')
        print()


    def esta_cheia(self):
        return self.quant == self.tamanho_max  


    def inserir_fim(self, valor):
        if self.esta_cheia():
            print('A lista está cheia')
            return
        self.vetor[self.fim] = valor
        self.fim = (self.fim + 1) % self.tamanho_max
        self.quant += 1



   

    def inserir_inicio(self, valor):
        if self.esta_cheia():
            print('A lista está cheia')
            return     
        self.inicio = (self.inicio - 1) % self.tamanho_max
        self.vetor[self.inicio] = valor
        self.quant += 1 


    def esta_vazia(self):
        return self.quant == 0


    def remover_inicio(self):
        if self.esta_vazia():
            print('A lista está vazia')
            return
        self.inicio = (self.inicio + 1) % self.tamanho_max
        self.quant -= 1


    def remover_fim(self):
        if self.esta_vazia():
            print('A lista está vazia')
            return
        self.fim = (self.fim - 1) % self.tamanho_max
        self.quant -= 1
class Les:
    def __init__ (self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0
    

    def set (self,valor):
        self.info = valor       


    def inserir_fim (self,valor):
        self.vetor [self.quant] = valor
        self.quant += 1


    def esta_cheia (self): 
        return self.quant >= self.tam
    
    
    def remover_fim (self):
        self.quant -= 1

    
    def igual (valor1, valor2):
        return valor1 == valor2
            

    def par (self):
        return self.info % 2 == 0
    

    def impar (self):
        return self.info % 2 != 0


    def positivo (self):
        return self.info > 0
    

    def maior (self,valor):
        return self.info > valor.info  
    

    def get (self):
        return self.info
    

    def get_prim(self):
        return self.vetor[0]
    
    
    def get_ult(self):
        return self.vetor[self.quant -1]
    
    
    def get_quant(self):
        return self.quant
    
    
    def get_capacidade(self):
        return self.tam
    

    def remover (self,valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                for j in range(i, self.quant -1):
                    self.vetor[j] = self.vetor[j + 1]
                self.quant -= 1
                return True
        return False
    

    def inserir_apos (self,valor1,valor2):
        if self.quant < self.tam:
            for i in range(self.quant):
                if self.vetor[i] == valor1:
                    for j in range(self.quant -1, i, -1):
                        self.vetor[j + 1] = self.vetor[j]
                    self.vetor[i + 1] = valor2
                    self.quant += 1
                    return True
        return False
    

    def inserir_antes (self,valor1,valor2):
        if self.quant < self.tam:
            for i in range(self.quant):
                if self.vetor[i] == valor1:
                    for j in range(self.quant -1, i -1, -1):
                        self.vetor[j + 1] = self.vetor[j]
                    self.vetor[i] = valor2
                    self.quant += 1
                    return True
        return False
    

    def remover_anteriores (self,valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                cont = i
                for j in range(i, self.quant):
                    self.vetor[j - cont] = self.vetor[j]
                self.quant -= cont
                return True
        return False
    

    def remover_posteriores (self,valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                cont = 0
                for j in range(i, self.quant -1):
                    cont += 1
                self.quant -= cont
                return True
        return False


    def get_index (self,valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                return i
        return None


    def get_valor (self,indice):
        if 0 <= indice < self.quant:
            return self.vetor[indice]
        return None


    def show_reverso(self):
        for i in range(self.quant -1, -1, -1):
            print(self.vetor[i], end=" - ")
        print()


    def existe (self,valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                return True
        return False
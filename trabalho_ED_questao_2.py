class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def inicializar_pilha(self):
        self.top = -1
        self.stack = [None] * self.size

    def pilha_eh_vazia(self):
        return self.top == -1

    def pilha_eh_cheia(self):
        return self.top == self.size - 1

    def empilha(self, item):
        if not self.pilha_eh_cheia():
            self.top += 1
            self.stack[self.top] = item
            return True
        return False

    def desempilha(self):
        if not self.pilha_eh_vazia():
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return item
        return None

    def le_topo(self):
        if not self.pilha_eh_vazia():
            return self.stack[self.top]
        return None

    def imprimir(self):
        if self.pilha_eh_vazia():
            print("Pilha vazia")
        else:
            print("Elementos da pilha (do topo para a base):")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

    def imprimir_reversa(self):
        if self.pilha_eh_vazia():
            print("Pilha vazia")
        else:
            print("Elementos da pilha (da base para o topo):")
            for i in range(0, self.top + 1):
                print(self.stack[i])

    def liberar(self):
        self.inicializar_pilha()

    def palindromo(self, texto):
        self.liberar()
        texto = texto.lower().replace(" ", "")
        meio = len(texto) // 2
        for i in range(meio):
            self.empilha(texto[i])
        inicio = meio + 1 if len(texto) % 2 != 0 else meio
        for i in range(inicio, len(texto)):
            if self.desempilha() != texto[i]:
                return False
        return True

    def elimina(self, elemento):
        if self.pilha_eh_vazia():
            return False
        
        temp_stack = Stack(self.size)
        encontrado = False
        while not self.pilha_eh_vazia():
            atual = self.desempilha()
            if atual == elemento:
                encontrado = True
            else:
                temp_stack.empilha(atual)
        while not temp_stack.pilha_eh_vazia():
            self.empilha(temp_stack.desempilha())
            
        return encontrado

    @staticmethod
    def pares_e_impares():
        pilha_principal = Stack(100)
        pilha_pares = Stack(100)
        pilha_impares = Stack(100)
        
        while True:
            try:
                num = int(input("Digite um número inteiro positivo (0 para terminar): "))
                if num == 0:
                    break
                if num > 0:
                    pilha_principal.empilha(num)
            except ValueError:
                print("Por favor, digite um número válido.")

        while not pilha_principal.pilha_eh_vazia():
            num = pilha_principal.desempilha()
            if num % 2 == 0:
                pilha_pares.empilha(num)
            else:
                pilha_impares.empilha(num)
        
        print("\nNúmeros pares:")
        pilha_pares.imprimir()
        
        print("\nNúmeros ímpares:")
        pilha_impares.imprimir()

pilha = Stack(5)

pilha.empilha(10)
pilha.empilha(20)
pilha.empilha(30)
pilha.empilha(40)

pilha.imprimir()

print("É palíndromo 'ovo':", pilha.palindromo("ovo"))
print("É palíndromo 'python':", pilha.palindromo("python"))

pilha.empilha(1)
pilha.empilha(2)
pilha.empilha(3)
pilha.empilha(4)

print("\nPilha original:")
pilha.imprimir()

pilha.elimina(3)
print("\nPilha após eliminar o elemento 3:")
pilha.imprimir()

print("\nImpressão reversa:")
pilha.imprimir_reversa()

print("\nDistribuição de pares e ímpares:")
Stack.pares_e_impares()
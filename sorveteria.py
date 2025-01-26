#### Syanne Karoline Moreira Tavares - 202104940029
from abc import ABC, abstractmethod

# Classe componente
class Sorvete(ABC):
    @abstractmethod
    def getDescricao(self):
        pass

    @abstractmethod
    def getPreco(self):
        pass

# ConcreteComponent-> recipiente
class Recipiente(Sorvete):
    def __init__(self, tipo, preco):
        self.tipo = tipo
        self.preco = preco

    def getDescricao(self):
        return f"Sorvete no {self.tipo}"

    def getPreco(self):
        return self.preco


# Decorator -> bolas de sorvete
class Bola(Sorvete):
    def __init__(self, sorvete, sabor, preco):
        self.sorvete = sorvete
        self.sabor = sabor
        self.preco = preco

    def getDescricao(self):
        return f"{self.sorvete.getDescricao()} com bola de {self.sabor}"

    def getPreco(self):
        return self.sorvete.getPreco() + self.preco


# Decorator -> coberturas
class Cobertura(Sorvete):
    def __init__(self, sorvete, tipo, preco):
        self.sorvete = sorvete
        self.tipo = tipo
        self.preco = preco

    def getDescricao(self):
        return f"{self.sorvete.getDescricao()} com cobertura de {self.tipo}"

    def getPreco(self):
        return self.sorvete.getPreco() + self.preco

# Menu 
def menu():
    print("-=-=-=-=-= Bem-vindo à Sorveteria!=-=-=-=-=")

    # Escolha do recipiente
    recipientes = {
        "1": ("Copo", 0.20),
        "2": ("Taça", 0.00),
        "3": ("Casquinha", 1.50),
    }
    print("-=-=-=-=-= Escolha o recipiente:")
    for chave, (recipiente, preco) in recipientes.items():
        print(f"{chave}. {recipiente} - R$ {preco:.2f}")
    recipienteEscolhido = input("Digite o número do recipiente: ")
    sorvete = Recipiente(recipientes[recipienteEscolhido][0], recipientes[recipienteEscolhido][1])

    # Escolha das bolas
    sabores = {
        "1": ("Chocolate", 1.50),
        "2": ("Morango", 1.50),
        "3": ("Flocos", 1.50),
        "4": ("Pavê", 1.50),
        "5": ("Napolitano", 1.50),
        "6": ("Chocolate Diet", 2.00),
    }
    print("\n-=-=-=-=-= Adicione bolas de sorvete (digite 0 para finalizar):")
    for chave, (sabor, preco) in sabores.items():
        print(f"{chave}. {sabor} - R$ {preco:.2f}")
    while True:
        saborEscolhido = input("Digite o número do sabor: ")
        if saborEscolhido == "0":
            break
        sorvete = Bola(sorvete, sabores[saborEscolhido][0], sabores[saborEscolhido][1])

    # Escolha das coberturas
    coberturas = {
        "1": ("Chocolate", 0.50),
        "2": ("Morango", 0.50),
        "3": ("Caramelo", 0.50),
    }
    print("\n-=-=-=-=-= Adicione coberturas (digite 0 para finalizar):")
    for chave, (cobertura, preco) in coberturas.items():
        print(f"{chave}. {cobertura} - R$ {preco:.2f}")
    while True:
        coberturaEscolhida = input("Digite o número da cobertura: ")
        if coberturaEscolhida == "0":
            break
        sorvete = Cobertura(sorvete, coberturas[coberturaEscolhida][0], coberturas[coberturaEscolhida][1])

    # Exibindo o pedido final
    print("\n\033[32m-=-=-=-=-= Resumo do pedido -=-=-=-=-=")
    print(sorvete.getDescricao())
    print(f"Preço total: R$ {sorvete.getPreco():.2f}\033[0m")


if __name__ == "__main__":
    menu()

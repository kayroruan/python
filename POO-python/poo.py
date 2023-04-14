#Exemplo básico de classe e herança em Python

class pessoa:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None

class funcionario(pessoa):
    def __init__(self):
        self.matricula = None
        self.salario = None
    def baterPonto():
        #código da função
        pass
    def fazerLogin():
        #código da função
        pass

class cliente(pessoa):
    def __init__(self):
        self.cadastro = None
        self.pedidos = None
    def fazerPedido():
        #código da função
        pass
    def fazerLogin():
        #código da função
        pass

print("Exemplo de nome de funcionário")
f1 = funcionario()
f1.nome = "João"
print(f1.nome)

print("Exemplo de cpf de cliente")
c1 = cliente()
c1.cpf = "111.222.333-44"
print(c1.cpf)
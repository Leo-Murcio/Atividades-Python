class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        taxa = 2
        if super().sacar(valor + taxa):
            return True
        else:
            return False

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return True
        else:
            return False

conta_poupanca = ContaPoupanca("Leo", 300)
conta_poupanca.depositar(500)
print(f"Saldo da Conta Poupança: R$ {conta_poupanca.saldo}")
conta_poupanca.sacar(100)
print(f"Saldo após sacar da Conta Poupança: R$ {conta_poupanca.saldo}")

conta_corrente = ContaCorrente("Messi", 600, 400)
conta_corrente.depositar(150)
print(f"Saldo da Conta Corrente: R$ {conta_corrente.saldo}")
conta_corrente.sacar(350)
print(f"Saldo após sacar da Conta Corrente: R$ {conta_corrente.saldo}")
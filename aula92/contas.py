import abc

class Contas(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def deposito(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'DEPÓSITO {valor}')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')

class ContaPoupanca(Contas):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return self.saldo

        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'SAQUE NEGADO {valor}')
        return self.saldo

    
class ContaCorrente(Contas):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return self.saldo

        print('Não foi possivel sacar o valor desejado')
        print(f'Seu limite é , {-self.limite:.2f}')
        self.detalhes(f'SAQUE NEGADO {valor}')
        return self.saldo

if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.deposito(1)
    cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(50)
    cc1.sacar(50)
    cc1.deposito(1)
    cc1.sacar(2)
    
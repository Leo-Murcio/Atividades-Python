class Fabrica:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        print(f"Motor {self.tipo} ligado")

    def desligar(self):
        print(f"Motor {self.tipo} desligado")

class Maquinario:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def ligar(self):
        print(f"Maquinario {self.marca} {self.modelo} ligado")
        self.motor.ligar()

    def desligar(self):
        print(f"Maquinario {self.marca} {self.modelo} desligado")
        self.motor.desligar()

motor_do_maquinario = Fabrica("VELOCIDADE 3")
meu_maquinario = Maquinario("Marca Generica", "Padrao de Fabrica", motor_do_maquinario)

meu_maquinario.ligar()
meu_maquinario.desligar()
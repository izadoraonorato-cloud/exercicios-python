import math  # Importa a biblioteca inteira de matemálica
raiz = math.sqrt(25)
 
from datetime import date  # Importa só a ferramenta da data
hoje = date.today().year
print("Estamos no ano de {hoje}")
while True:  # O loop infinito foi iniciado
   comando = input("Digite 'sair' para desligar o motor: ")
   if comando.lower() == 'sair':
        print("Motor desligado.")
        break  # A trava de segurança foi acionada!
else:
        print("O motor continua a rodar...")
from Empresa import Empresa
from AssentoError import AssentoError
from PasengerError import PasengerError
from Passageiro import Passageiro





def main():
  while True:
    print('''O que deseja realizar?
  [1] - Cadastrar passageiro
  [2] - Remover passageiro
  [3] - Procurar passageiro
  [4] - Alterar poltrona do passageiro
  [5] - Mostrar passageiros cadastrados
  [6] - Consultar quantidade de assentos
  [7] - Mostrar assentos
  [8] - Cadastrar ônibus
  [9] - Procuara assento disponível
  [10] - Esvaziar poltronas
  [999] - Encerra o programa''')

    pid = int(input('>Inserir comando: '))
    
    if pid == 1:
      user_input = input()
    elif pid == 2:
      pass
    elif pid == 3:
      pass
    elif pid == 4:
      pass
    elif pid == 5:
      pass
    elif pid == 6:
      pass
    elif pid == 7:
      pass
    elif pid == 8:
      pass
    elif pid == 9:
      pass
    elif pid == 10:
      pass
    elif pid == 999:
      print("Programa encerrado!")
      break
    else:
      print("Comando não encontrado")

if __name__ == '__main__':
  main()
from Empresa import Empresa
from AssentoError import AssentoError
from PasengerError import PasengerError
from Passageiro import Passageiro

def check_if_pid_is_avaiable(pid:int)->bool:
  pid_avaiable_list = [1,2,3,4,5,6,7,8,9,10]
  if pid in pid_avaiable_list:
    return True
  return False

def decision_company(pid:int, company:Empresa):
  if pid == 1:
    bus_name = input("Informe o ônibus")
    passanger = input("Informe o passageiro")
    number_seat= int(input("Informe o número da cadeira"))
    company.add_passenger(bus_name, passanger, number_seat)
  elif pid == 2:
    bus_name = input("Informe o ônibus")
    number_seat = int(input("Informe o número da cadeira"))
    company.remove_passenger(bus_name, number_seat)
  elif pid == 3:
    bus_name = input("Informe o ônibus: ")
    passanger = input("Informe o nome do passageiro: ")
    company.search_passenger(bus_name, passanger)

def show_options()->str:
  return f'''O que deseja realizar?
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
  [999] - Encerra o programa'''

def main():
  while True:
    print(show_options())
    
    pid = int(input('>Inserir comando: '))
    
    if pid == 999: break

    if check_if_pid_is_avaiable(pid):
      pass
    else:
      print('Comando não encontrado')

if __name__ == '__main__':
  main()
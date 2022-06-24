from Empresa import Empresa
from AssentoError import AssentoError
from PasengerError import PasengerError
from Passageiro import Passageiro

def check_if_pid_is_avaiable(pid:int)->bool:
  pid_avaiable_list = [1,2,3,4,5,6,7,8,9,10]
  if pid in pid_avaiable_list:
    return True
  return False

def decision_company(pid:int, company:Empresa)->None:

  bus_name = input("Informe o ônibus")

  if pid == 1:
    passanger = input("Informe o passageiro")
    number_seat= int(input("Informe o número do assento"))
    company.add_passenger(bus_name, passanger, number_seat)
  elif pid == 2:
    number_seat = int(input("Informe o número do assento"))
    company.remove_passenger(bus_name, number_seat)
  elif pid == 3:
    passanger_name = input("Informe o nome do passageiro: ")
    company.search_passenger(bus_name, passanger_name)
  elif pid == 4:
    number_seat_current = int(input("Informe o número atual do assento do passageiro: "))
    number_seat_new = int(input("Informe o novo número do assento do passageiro: "))
    company.change_seat(bus_name, number_seat_current, number_seat_new)
  elif pid == 5:
    #falta método para mostrar passageiros no ônibus
    pass
  elif pid == 6:
    company.quantity_seats(bus_name)
  elif pid == 7:
    company.show_seats(bus_name)
  elif pid == 8:
    #falta método para cadastrar ônibus
    pass
  elif pid == 9:
    print(company.search_seat_available(bus_name))
  elif pid == 10:
    company.clear_bus(bus_name)

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
  [9] - Procurar assento disponível
  [10] - Esvaziar poltronas
  [999] - Encerra o programa'''

def main():
  company = Empresa()
  while True:
    print(show_options())
    
    pid = int(input('>Inserir comando: '))
    
    if pid == 999: break

    if check_if_pid_is_avaiable(pid):
      decision_company(pid, company)
    else:
      print('Comando não encontrado')

main()
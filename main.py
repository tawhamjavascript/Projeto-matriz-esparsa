from Empresa import Empresa
from AssentoError import AssentoError
from PasengerError import PasengerError
from Passageiro import Passageiro
from CommandController import CommandController

def check_if_pid_is_avaiable(pid:int)->bool:
  '''
  Checa se o pid é válido

  :param pid: recebe um int, contendo o pid do usuário
  '''
  if (pid > 10 and pid != 999) or (pid < 0):
    return False
  return True

def company_actions(command:int,command_values:tuple):
  if command == 1:
    company.add_passenger(command_values[0], command_values[1], command_values[2])
  elif command == 7:
    company.show_seats(command_values[0])
  elif command == 8:
    company.set_bus(command_values[0], command_values[1])
    

def show_options()->str:
  return f'''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
  O que deseja realizar?
  [1]   - Cadastrar passageiro
  [2]   - Remover passageiro
  [3]   - Procurar passageiro
  [4]   - Alterar poltrona do passageiro
  [5]   - Mostrar passageiros cadastrados
  [6]   - Consultar quantidade de assentos
  [7]   - Mostrar assentos
  [8]   - Cadastrar ônibus
  [9]   - Procurar assento disponível
  [10]  - Esvaziar poltronas
  [999] - Encerra o programa
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''

def main():
  global company
  company = Empresa()
  command_controller = CommandController()
#   COMPANY_ACTION = {
#   1: company.add_passenger(command_values[0], command_values[1], command_values[2]),
#   2: company.remove_passenger,
#   3: company.search_passenger,
#   4: company.change_seat,
#   5: "",
#   6: company.quantity_seats,
#   7: company.show_seats(command_values[0]),
#   8: company.set_bus(command_values[0], command_values[1]),
#   9: company.search_seat_available,
#   10: company.clear_bus
# }
  while True:
    print(show_options())
    
    pid = int(input('> Inserir comando: '))

    if check_if_pid_is_avaiable(pid):
      command_values = command_controller.get_command_values(pid)
      if pid == 1:
        company.add_passenger(command_values[0], command_values[1], command_values[2])
      if pid == 7:
        company.show_seats(command_values[0])
      if pid == 8:
        company.set_bus(command_values[0], command_values[1])
    else:
      print("Comando inválido")
    
    if pid == 999: 
      print("Programa Encerrado!")
      break

main()
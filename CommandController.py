from ChainingHashTable import ChainingHashTable
from Empresa import Empresa
from Passageiro import Passageiro

class CommandController:
  def __init__(self) -> None:
    self.__command_options = {
      1: self.__add_passenger,
      2: self.__remove_passenger,
      3: self.__search_passenger,
      4: self.__change_seat,
      5: '',
      6: self.__quantity_seats,
      7: self.__show_seats,
      8: self.__set_bus,
      9: self.__search_seat_available,
      10: self.__clear_bus
    }

  def get_command_values(self, command:int)->tuple:
    '''
    :param command: recebe um int, contendo o comando do usuário
    :return: retorna uma tupla com os parâmetros para any:Empresa
    '''
    command_values = self.__command_options[command]()
    return command_values
  
  def __request_bus_name(self)->str:
    '''
    Solicita o nome do ônibus para o usuário e retorna o nome dele
    '''
    bus_name = input('> Informe o ônibus: ')
    return bus_name

  def __add_passenger(self)->tuple:
    '''
    Solicita o nome, o rg, o número do assento do passageiro e o nome do ônibus.
    Retorna uma tupla com o nome do ônibus, um objeto do tipo Passageiro e
    o número do assento do passageiro.
    '''
    passanger_name = input('> Informe o nome do passageiro: ')
    passanger_rg = input('> Informe o rg do passageiro: ')
    passanger = Passageiro(passanger_name, passanger_rg)

    bus_name = self.__request_bus_name()
    seat_number = int(input('> Informe o número do assento: '))

    return (bus_name, passanger, seat_number)
  
  def __remove_passenger(self)->tuple:
    '''
    Solicita o nome do ônibus e o número do assento do passageiro.
    Retorna uma tupla com o nome do ônibus e o número do assento.
    '''
    bus_name = self.__request_bus_name()
    seat_number = input('> Informe o número do assento: ')

    return (bus_name, seat_number)

  def __search_passenger(self)->tuple:
    '''
    Solicita o nome do ônibus e o nome do passageiro.
    Retorna uma tupla com o nome do ônibus e o nome do passageiro
    '''
    bus_name = self.__request_bus_name()
    passanger_name = input('> Informe o nome do passageiro: ')
    return (bus_name, passanger_name)


  def __change_seat(self)->tuple:
    '''
    Solicita o nome do ônibus, o assento atual e o novo assento do passageiro.
    Retorna uma tupla com o nome do ônibus, o número do assento atual e o número do novo assento.
    '''
    bus_name = self.__request_bus_name()
    current_seat_number = int(input('> Informe o assento atual do passageiro: '))
    new_seat_number = int(input('> Informe o novo número do assento: '))
    return (bus_name, current_seat_number, new_seat_number)

  def __quantity_seats(self)->tuple:
    '''
    Solicita o nome do ônibus para informar a quantidade de assentos.
    Retorna uma tupla com o nome do ônibus
    '''
    return (self.__request_bus_name())

  def __show_seats(self)->tuple:
    '''
    Solicita o nome do ônibus para mostrar os assentos do ônibus. 
    Retorna uma tupla com o nome do ônibus
    '''
    return (self.__request_bus_name())

  def __set_bus(self)->tuple:
    bus_name = self.__request_bus_name()
    quantity_of_seats = int(input('> Informe a quantidade de assentos do ônibus: '))
    return (bus_name, quantity_of_seats)

  def __search_seat_available(self)->tuple:
    '''
    Solicita o nome do ônibus para procurar um assento disponível. Retorna uma tupla com o nome do ônibus
    '''
    return (self.__request_bus_name())

  def __clear_bus(self)->tuple:
    '''
    Solicita o nome do ônibus para esvaziar o ônibus. Retorna uma tupla com o nome do ônibus
    '''
    return (self.__request_bus_name())

from MatrizEsparsa import MatrizEsparsa
from AssentoError import AssentoError
from PasengerError import PasengerError
from Passageiro import Passageiro
from OnibusError import OnibusError

class Empresa:
    def __init__(self):
        self.__bus = {}

    def set_bus(self, nome, numero_cadeira):
        cols = numero_cadeira // 4
        """
        Adiciona um novo ônibus
        
        :param nome: recebe um str, contendo o nome da string
        :param numero_cadeira: recebe um int, contendo a quantidade de cadeiras

        """
        self.bus.update({nome: MatrizEsparsa(nome, cols)})

    def quantity_seats(self, bus_name) -> int:
        """
        Verifica a quantidade de cadeiras no ônibus

        :param bus_name: recebe um str, contendo o nome do ônibus
        :raise OnibusError: Se o ônibus não existi
        :return: um int, contendo a quantidade de cadeiras no ônibus
        """
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            bus.tamanho()

        except AssentoError:
            raise OnibusError("Onibus não existe")


    def bus_is_empty(self, bus_name) -> bool:
        """
        Verifica se o ônibus está vazio

        :param bus_name: recebe um str, contendo o nome do ônibus
        :raise OnibusError: Se o ônibus não existir
        :return: True se o ônibus está vazio ou False se não estiver
        """
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            return bus.isEmpty()
        
        except AssertionError:
            raise OnibusError("Onibus não existe")

    def bus_is_full(self, bus_name) -> bool:
        """
        Verifica se o ônibus está cheio

        :param bus_name: recebe um str, contendo o nome do ônibus
        :raise OnibusError: Se o ônibus não existir
        :return: True se o ônibus está cheio ou False se não estiver
        """
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            return self.__bus.isFull()
        
        except AssertionError:
            raise OnibusError("Onibus não existe")
       

    def search_seat_available(self, bus_name) -> int:
        """
        Verifica se o ônibus tem alguma poltrona vazia

        :param bus_name: recebe um str, contendo o nome do ônibus
        :raise OnibusError: Se o ônibus não existir
        :raise IndexError: Se o ônibus não tiver assento
        :return: Um int com o assento disponível

        """
        bus = self.__bus.get(bus_name)
        
        try:
            assert bus is not None
            return bus.searchSeatAvailable()
        
        except IndexError:
            raise AssentoError("Não há assentos disponíveis")

        except AssertionError:
            raise OnibusError("Onibus não existe")

    def search_seat_passenger(self, bus_name, numero_poltrona:int) -> str:
        """
        Verifica se na poltrona tem passageiro

        :param bus_name: recebe um str, contendo o nome do ônibus
        :param numero_poltrona: recebe um int, contendo a numeração da cadeira
        :raise AssentoError: Se o assento não existir, propagando um AssentoError
        :raise OnibusError: Se o ônibus não existir
        :return: Um str, contendo as informações do passageiro
        """
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            assert numero_poltrona > 0 and numero_poltrona <= self.__bus.tamanho(), AssentoError("Assento não existe")
            return bus.pesquisar(numero_poltrona)

        except IndexError:
            raise AssentoError("Assento não existe")

        except AssertionError:
            raise OnibusError("Onibus não existe")

    def search_passenger(self, bus_name, nome:str) -> int:
        """
        responsável por procurar um passageiro no ônibus


        :param bus_name: recebe um str, contendo o nome do ônibus
        :param nome: recebe um str, contendo o nome do passageiro
        :raise AssentoError: Se o assento não existir, propagando um AssentoError
        :raise OnibusError: Se o ônibus não existir
        :return: um int, contendo a poltrona que o passageiro está alocado

        """
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            return self.__bus.searchPassenger(nome)

        except IndexError:
            raise PasengerError("Passageiro não existe")

        except AssertionError:
            raise OnibusError("Onibus não existe")

    def get_passenger(self, bus_name, numero_poltrona:int) -> Passageiro:
        """
        Responsável por verificar se na poltrona existi passageiro

        :param bus_name: recebe um str, contendo o nome do ônibus
        :param numero_poltrona: recebe um int, contendo a numeração da cadeira
        :raise AssentoError: Se o assento não existir, propagando um AssentoError
        :raise OnibusError: Se o ônibus não existir
        :return: Um objeto passageiro
        """
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            assert numero_poltrona > 0 and numero_poltrona <= self.__bus.tamanho(), AssentoError("Assento não existe")
            return self.__bus.getPassageiro(numero_poltrona)

        except IndexError:
            raise AssentoError("Assento não existe")

        except AssertionError:
            raise OnibusError("Onibus não existe")

    def change_seat(self, bus_name, number_seat_current: int, number_seat_new: int) -> bool:
        """
        Função responsável por trocar um passageiro de um assento para o outro

        :param bus_name: recebe um str, contendo o nome do ônibus.
        :param number_seat_current: recebe um int, contendo a numeração da cadeira atual.
        :param number_seat_new: recebe um int, contendo a numeração da cadeira que deseja trocar.
        :raise AssentoError: Se o assento não existir, propagando um AssentoError
        :raise OnibusError: Se o ônibus não existir
        :return: True se a troca foi bem sucedida ou False se não foi possível
        """
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            assert number_seat_current > 0 and number_seat_current <= self.__bus.tamanho() and number_seat_new > 0 and number_seat_new <= self.__bus.tamanho(), AssentoError("Assento inexistente")
            resultado =  self.__bus.switchSeat(number_seat_current, number_seat_new)
            if resultado:
                return f"troca bem sucedida"

            else:
                return f"poltrona já está em uso"
            
        except IndexError:
            raise AssentoError("Assento não existe")

        except AssertionError:
            raise OnibusError("Onibus não existe")


    def add_passenger(self, bus_name, passenger:Passageiro, number_seat) -> bool:
        """
        Função responsável por alocar um passageiro a uma poltrona

        :param bus_name: recebe um str, contendo o nome do ônibus.
        :param passenger: Recebe um objeto Passageiro.
        :param number_seat:  recebe um int, contendo a numeração da cadeira.
        :raise AssentoError: Se o assento não existir, propagando um AssentoError
        :raise OnibusError: Se o ônibus não existir
        :return: Uma string informando se o assento está indisponível ou foi alocado com sucesso
        """
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            assert number_seat > 0 and number_seat <= self.__bus.tamanho(), AssentoError("Assento inexistente")
            resultado = self.__bus.add(passenger, number_seat)
            if resultado:
                return f"Passageiro alocado no assento {number_seat}"

            else:
                return f"Assento já está em uso"

        except IndexError:
            raise AssentoError("Assento não existe")

        except AssertionError:
            raise OnibusError("Onibus não existe")

    def remove_passenger(self, bus_name, number_seat:int) -> bool:
        """

        :param bus_name: recebe um str, contendo o nome do ônibus
        :param number_seat: recebe um int, contendo a numeração da cadeira
        :raise AssentoError: Se o assento não existir, propagando um AssentoError
        :raise OnibusError: Se o ônibus não existir
        :return: O objeto passageiro
        """
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            assert number_seat > 0 and number_seat <= self.__bus.tamanho(), AssentoError("Assento inexistente")
            return self.__bus.removerPassageiro(number_seat)

        except IndexError:
            raise AssentoError("Assento não existe")

        except AssertionError:
            raise OnibusError("Onibus não existe")

    def clear_bus(self, bus_name) -> bool:

        """
        Retira todos os passageiros do assento

        :param bus_name: recebe um str, contendo o nome do ônibus
        :raise OnibusError: Se o ônibus não existir
        """
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            bus.empty()

        except AssertionError:
            raise OnibusError("Onibus não existe")

    def show_seats(self, bus_name) -> str:
        """
        Verifica a situação dos assentos

        :param bus_name: recebe um str, contendo o nome do ônibus
        :raise OnibusError: Se o ônibus não existir
        :return: Uma str, com a situação dos assentos
        """
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            return self.__bus.showSeat()

        except AssertionError:
            raise OnibusError("Onibus não existe")

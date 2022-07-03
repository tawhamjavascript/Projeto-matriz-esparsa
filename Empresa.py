from ast import Try
from MatrizEsparsa import MatrizEsparsa
from AssentoError import AssentoError
from PasengerError import PasengerError
from Passageiro import Passageiro
from OnibusError import OnibusError

class Empresa:
    def __init__(self):
        self.__bus = {}

    def get_bus(self)->dict:
        """ Retorna um dicionário contendo todos os ônibus cadastrados"""
        return self.__bus

    def create_txt(self, bus_name):
        """ Insere uma relação dos passageiros de uma determinada viajem em um arquivo chamado passageiro.txt"""
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            infoPassengers = bus.getInfoAllPassengers()
            tamanho_infoPassengers = len(infoPassengers)
            string = ""
            if tamanho_infoPassengers == 0:
                string += f"Linha: {bus.getId()} - ônibus vazio"
            else:                    
                string += f"Linha: {bus.getId()}\n"
                string += "Poltrona;passageiro;rg\n"
                for poltrona, passageiro in infoPassengers.items():
                    string += f"{poltrona};{passageiro[0]};{passageiro[1]}\n"
                    
            with open('passageiros.txt', 'w', encoding="utf-8") as file:
                file.write(string)
        except AssertionError:
            raise OnibusError("Ônibus não exite")


    def set_bus(self, nome, numero_cadeira):
        cols = numero_cadeira // 4
        """
        Adiciona um novo ônibus
        
        :param nome: recebe um str, contendo o nome da string
        :param numero_cadeira: recebe um int, contendo a quantidade de cadeiras

        """
        self.__bus.update({nome: MatrizEsparsa(nome, cols)})

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
            return bus.tamanho()

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
            return bus.isFull()
        
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
            return bus.search(numero_poltrona)

        except IndexError:
            raise AssentoError("Assento não existe")

        except PasengerError as error:
            raise PasengerError(error)

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
            return bus.searchPassenger(nome)

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

            return bus.getPassenger(numero_poltrona)

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
            resultado = bus.switchSeat(number_seat_current, number_seat_new)
            return resultado
            
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
            resultado = bus.add(passenger, number_seat)
            return resultado

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
            return bus.remove(number_seat)

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
            return bus.showSeat()

        except AssertionError:
            raise OnibusError("Onibus não existe")

if __name__ == '__main__':
    empresa = Empresa()
    taw = Passageiro('taw', 123)
    ric = Passageiro('ric', 321)
    empresa.set_bus("jp", 40)
    empresa.add_passenger("jp", taw, 2)
    empresa.set_bus("cg", 40)
    empresa.add_passenger("cg", ric, 2)

    teste = empresa.get_bus()
    print(teste['jp'].getInfoAllPassengers())
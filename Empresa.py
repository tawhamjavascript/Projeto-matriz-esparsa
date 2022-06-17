from MatrizEsparsa import MatrizEsparsa
from AssentoError import AssentoError
from PasengerError import PasengerError
from Passageiro import Passageiro
from OnibusError import OnibusError

class Empresa:
    def __init__(self):
        self.__bus = {}

    def set_bus(self, nome, rows, cols):
        self.bus.update({nome: MatrizEsparsa(rows, cols)})

    def quantity_seats(self, bus_name) -> int:
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            bus.tamanho()

        except AssentoError:
            raise OnibusError("Onibus não existe")


    def bus_is_empty(self, bus_name) -> bool:
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            return bus.isEmpty()
        
        except AssertionError:
            raise OnibusError("Onibus não existe")

    def bus_is_full(self, bus_name) -> bool:
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            return self.__bus.isFull()
        
        except AssertionError:
            raise OnibusError("Onibus não existe")
       

    def search_seat_available(self, bus_name) -> int:
        bus = self.__bus.get(bus_name)
        
        try:
            assert bus is not None
            return bus.searchSeatAvailable()
        
        except IndexError:
            raise AssentoError("Não há assentos disponíveis")

        except AssertionError:
            raise OnibusError("Onibus não existe")

    def search_seat_passenger(self, bus_name, numero_poltrona:int) -> str:
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
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            return self.__bus.searchPassenger(nome)

        except IndexError:
            raise PasengerError("Passageiro não existe")

        except AssertionError:
            raise OnibusError("Onibus não existe")

    def get_passenger(self, bus_name, numero_poltrona:int) -> Passageiro:
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            assert numero_poltrona > 0 and numero_poltrona <= self.__bus.tamanho(), AssentoError("Assento não existe")
            return self.__bus.getPassageiro(numero_poltrona)

        except IndexError:
            raise AssentoError("Assento não existe")

        except AssertionError:
            raise OnibusError("Onibus não existe")

    def change_seat(self, bus_name, number_seat_current:int, number_seat_new:int) -> bool:
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
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            bus.empty()

        except AssertionError:
            raise OnibusError("Onibus não existe")

    def show_seats(self, bus_name) -> None:
        bus = self.__bus.get(bus_name)
        try:
            assert bus is not None
            return self.__bus.showSeat()

        except AssertionError:
            raise OnibusError("Onibus não existe")
    






       
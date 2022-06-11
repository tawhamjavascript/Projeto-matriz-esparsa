from MatrizEsparsa import MatrizEsparsa
from AssentoError import AssentoError
from PasengerError import PasengerError
from Passageiro import Passageiro

class Empresa:
    def __init__(self):
        self.__bus = None

    def set_bus(self, nome, rows, cols):
        self.__bus = MatrizEsparsa(nome, rows, cols)

    def quantidade_assentos(self) -> int:
        return self.__bus.tamanho()

    def bus_is_empty(self) -> bool:
        return self.__bus.estaVazia()

    def bus_is_full(self) -> bool:
        return self.__bus.estaCheio()

    def search_seat_available(self) -> int:
        try:
            return self.__bus.procurarAssentoDisponivel()
        
        except IndexError:
            raise AssentoError("Não há assentos disponíveis")

    def search_seat_passenger(self, numero_poltrona:int) -> str:
        try:
            assert numero_poltrona > 0 and numero_poltrona <= self.__bus.tamanho()
            return self.__bus.pesquisar(numero_poltrona)

        except IndexError:
            raise AssentoError("Assento não existe")

        except AssertionError:
            raise AssentoError("Assento inexistente")

    def search_passenger(self, nome:str) -> int:
        try:
            return self.__bus.pesquisaPassageiro(nome)

        except IndexError:
            raise PasengerError("Passageiro não existe")

    def get_passenger(self, numero_poltrona:int) -> Passageiro:
        try:
            assert numero_poltrona > 0 and numero_poltrona <= self.__bus.tamanho()
            return self.__bus.getPassageiro(numero_poltrona)

        except IndexError:
            raise AssentoError("Assento não existe")

    def change_seat(self, number_seat_current:int, number_seat_new:int) -> bool:
        try:
            assert number_seat_current > 0 and number_seat_current <= self.__bus.tamanho() and number_seat_new > 0 and number_seat_new <= self.__bus.tamanho()
            resultado =  self.__bus.trocarAssento(number_seat_current, number_seat_new)
            if resultado:
                return f"troca bem sucedida"

            else:
                return f"poltrona já está em uso"
            
        except IndexError:
            raise AssentoError("Assento não existe")

        except AssertionError:
            raise AssentoError("Assento inexistente")


    def add_passenger(self, passenger:Passageiro, number_seat) -> bool:
        try:
            assert number_seat > 0 and number_seat <= self.__bus.tamanho()
            resultado = self.__bus.adicionar(passenger, number_seat)
            if resultado:
                return f"Passageiro alocado no assento {number_seat}"

            else:
                return f"Assento já está em uso"

        except IndexError:
            raise AssentoError("Assento não existe")

        except AssertionError:
            raise AssentoError("Assento inexistente")

    def remove_passenger(self, number_seat:int) -> bool:
        try:
            assert number_seat > 0 and number_seat <= self.__bus.tamanho()
            return self.__bus.removerPassageiro(number_seat)

        except IndexError:
            raise AssentoError("Assento não existe")

        except AssertionError:
            raise AssentoError("Assento inexistente")

    def clear_bus(self) -> bool:
        self.__bus.esvaziar()

    def show_seats(self) -> None:
        return self.__bus.mostrarAssentos()
    






       
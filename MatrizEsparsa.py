from Passageiro import Passageiro
from PasengerError import PasengerError

class MatrizEsparsa:
    def __init__(self, id: str, colunas: int):
        '''A numeracao das poltronas é definida da seguinte forma:
                      Poltronas
           Fileira 1: 01 02    03 04
           Fileira 2: 05 06    07 08
           ....
        '''
        self.__id = id  # pegar a linha do ônibus
        self.__matriz = [[None for y in range(colunas)] for i in range(4)]  # cria uma matriz
        self.__colunas = colunas  # guarda a quantidade de colunas
        self.__linhas = 4  # guarda a quantidade de fileiras
        self.__ocupacao = 0     # guarda a quantidade de cadeiras ocupadas
        self.__cadeiras_maximas = self.__colunas * self.__linhas    # guarda a quantidade de cadeiras máximas

    def tamanho(self) -> int:
        """ Retorna a quantidade de cadeiras máximas"""
        return self.__cadeiras_maximas

    def isEmpty(self) -> bool:
        """ Verifica se a matriz está vazia """
        return self.__ocupacao == 0 
        

    def isFull(self) -> bool:
        """ Verifica se a matriz está cheia"""
        return self.__ocupacao == self.__cadeiras_maximas

    def searchSeatAvailable(self)->int:
        '''Retorna um assento vazio disponível, se houver.
           Se não houver assento disponível, lançar uma exceção'''
        id_poltrona = 0
        try:
            for i in range(len(self.__matriz)):
                for j in range(len(self.__matriz[i])):
                    id_poltrona += 1
                    if self.__matriz[i][j] == None:
                        return id_poltrona
            
            assert id_poltrona == self.__cadeiras_maximas
                        
        except AssertionError:
            raise IndexError("Não há assentos disponíveis")


    def search(self, numero_poltrona:int)->str:
        '''Retorna os dados do passageiro alocado em um
           determinado assento'''
        try:
            assert numero_poltrona > 0
            posicao = self.searchSeat(numero_poltrona)
            passageiro = self.__matriz[posicao[0]][posicao[1]]
            if passageiro is not None:
                return str(passageiro)

            else:
                raise PasengerError('Passageiro não existe')

            
        except IndexError:
            raise IndexError("Assento não existe")

        except AssertionError:
            raise IndexError("Assento não existe")


    def searchSeat(self, numero_poltrona: int) -> tuple:
        """
        Verifica se o assento existe na matriz, se existir retorna a posição dele na matriz

        :param numero_poltrona: recebe um numero inteiro

        :raise IndexError: caso o assento não esteja na matriz
        :return: retorna uma tupla contendo a posição da matriz e do array

        """
        position_in_the_matriz = (numero_poltrona - 1) // self.__colunas
        try:
            assert position_in_the_matriz < self.__linhas
            posicao_assento = (numero_poltrona - 1) % self.__colunas
            return (position_in_the_matriz, posicao_assento)

        except AssertionError:
            raise IndexError("Assento não existe")

    def searchPassenger(self, nome: str )->int:
        '''
        Verifica se o passageiro está no ônibus
        :param nome: recebe uma string contendo o nome do passageiro
        :raise IndexError: caso o passageiro não seja encontrado

        '''
        id_poltrona = 0
        try:
            for i in range(len(self.__matriz)):
                for j in range(len(self.__matriz[i])):
                    id_poltrona += 1
                    if self.__matriz[i][j] is None:
                        continue

                    elif nome == self.__matriz[i][j].get_nome():
                        return id_poltrona

            assert id_poltrona != self.__cadeiras_maximas
        except AssertionError:        
            raise IndexError("Passageiro não encontrado")

    def getPassenger(self, num_poltrona: int) -> str:
        """
        Verifica se na poltrona existe passageiro

        :param num_poltrona: recebe um inteiro, contendo a poltrona
        :raise IndexError: Caso o assento não exista na matriz
        :return: O objeto passageiro
        """
        try:
            assert num_poltrona > 0
            posicao = self.searchSeat(num_poltrona)
            return str(self.__matriz[posicao[0]][posicao[1]])
              
        except IndexError:
            raise IndexError("Assento não existe")

        except AssertionError:
            raise IndexError("Assento não existe")

    def switchSeat(self, poltrona_atual:int, nova_poltrona:int)->bool:
        '''
        Troca o passageiro de uma poltrona para outra

        :param poltrona_atual: recebe um int, contendo a poltrona
        :param nova_poltrona: recebe um int, contendo a poltrona
        :raise IndexError: Caso o assento não exista na matriz
        :return: True se for possível a troca de passageiro ou False se não for possível a troca
        '''
        try:
            assert poltrona_atual > 0 and nova_poltrona > 0
            posicao_poltrona_atual = self.searchSeat(poltrona_atual)
            posicao_nova_poltrona = self.searchSeat(nova_poltrona)
            if self.__matriz[posicao_nova_poltrona[0]][posicao_nova_poltrona[1]] is None:
                self.__matriz[posicao_nova_poltrona[0]][posicao_nova_poltrona[1]] = self.__matriz[posicao_poltrona_atual[0]][posicao_poltrona_atual[1]]
                self.__matriz[posicao_poltrona_atual[0]][posicao_poltrona_atual[1]] = None
                return True

            return False

        except IndexError:
            raise IndexError("Assento não existe")

        except AssertionError:
            raise IndexError("Assento não existe")



    def add(self, passageiro, numero_poltrona:int)->bool:
        '''
        Adiciona um passageiro a poltrona

        :param passageiro: Recebe o objeto Passageiro
        :param numero_poltrona: recebe um int, com a numeração da poltrona
        :raise IndexError: Caso a poltrona não exista
        :return: True se ocorrer a inserção, caso contrário False

        '''
        try:
            assert numero_poltrona > 0
            posicao = self.searchSeat(numero_poltrona)
            if self.__matriz[posicao[0]][posicao[1]] is None:
                self.__matriz[posicao[0]][posicao[1]] = passageiro
                self.__ocupacao += 1
              
                return True
            
            return False

        except IndexError:
            raise IndexError("Assento não existe")

        except AssertionError:
            raise IndexError("Assento não existe")
        

    def remove(self, numero_poltrona:int) -> None:
        """
        Remove um passageiro do assento

        :param numero_poltrona: recebe um int, contendo o número da cadeira
        :raise IndexError: Caso o assento não exista
        :return: Um objeto do tipo Passageiro
        """
        try:
            assert numero_poltrona > 0
            posicao = self.searchSeat(numero_poltrona)
            passageiro = self.__matriz[posicao[0]][posicao[1]]
            self.__matriz[posicao[0]][posicao[1]] = None


        except IndexError: 
            raise IndexError("Assento não existe")

        except AssertionError:
            raise IndexError("Assento não existe")

    def empty(self) -> None:
        """
        Esvazia a matriz esparsa
        """
        for i in range(len(self.__matriz)):
            for j in range(len(self.__matriz[i])):
                self.__matriz[i][j] = None

    def showSeat(self):
        """Mostra o status de ocupacao de todos os assentos"""
        return self.__str__()

    def __str__(self):
        """
        Método que representa o ônibus na horizontal
        :return: Uma string, contendo a representação do ônibus na horizontal
        """
        string = ""
        cadeira = 0
        posicao_matriz = 0
        posicao_array = 0
        for i in range(4):
            cadeira = i + 1
            for j in range(self.__colunas):
                if cadeira == (i + 1):
                    posicao_matriz, posicao_array = self.searchSeat(cadeira)

                else:
                    posicao_matriz, posicao_array = self.searchSeat(cadeira)

                string += f"|{cadeira}|"
                cadeira += 4
                valor = self.__matriz[posicao_matriz][posicao_array]
                string += f" [{valor.get_nome()[0:3] if valor is not None else '   '}] "

            string += '\n'

        return string

if __name__ == '__main__':
    matrizesparsa = MatrizEsparsa("Bayeux - tambay", 4, 12)
    lista = ["Dente", "Graves", "Disputa", "Punho", "Varinha", "Menina", "Amor", "Ataques", "Macaco", "Caribe", "Rural", "Aranha", "Inocente", "Amanhecer", "Ombreiras", "Escape", "Capacho", "Folha", "Animais"]
    for i in range(len(lista)):
        matrizesparsa.add(lista[i], i + 1)

    print(f" tamanho do ônibus {matrizesparsa.tamanho() } ")
    print(f" tamanho do ônibus {matrizesparsa.isEmpty() } ")
    print(f" procurar cadeira disponível {matrizesparsa.searchSeatAvailable() } ")
    print(f"Passageiro na poltrona {matrizesparsa.getPassenger(7) } ")
    print(matrizesparsa)



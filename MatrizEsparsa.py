from cgi import print_directory
from Passageiro import Passageiro

class MatrizEsparsa:
    def __init__(self, id:str, linhas:int, colunas:int):
        '''A numeracao das poltronas é definida da seguinte forma:
                      Poltronas
           Fileira 1: 01 02    03 04
           Fileira 2: 05 06    07 08
           ....
        '''
        self.__id = id
        self.__matriz = [ [None] * colunas ] * linhas
        self.__colunas = colunas
        self.__linhas = linhas
        self.__ocupacao = 0
        self.__cadeiras_maximas = self.__colunas * self.__linhas
  
    
    def tamanho(self) -> int:
        '''Retorna a quantidade de células da matriz'''
        return self.__cadeiras_maximas

    def estaVazia(self) -> bool:
        return self.__ocupacao == 0 
        

    def estaCheio(self) -> bool:
        return self.__ocupacao == self.__cadeiras_maximas

    def procurarAssentoDisponivel(self)->int:
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


    def pesquisar(self, numero_poltrona:int)->Passageiro:
        '''Retorna os dados do passageiro alocado em um
           determinado assento'''
        try:
            posicao = self.pesquisar_assento(numero_poltrona)
            passageiro = str(self.__matriz[posicao[0]][posicao[1]])
            return passageiro
            
        except IndexError:
            raise IndexError("Assento não existe")

    def pesquisar_assento(self, numero_poltrona:int)->tuple:
        position_in_the_matriz = (numero_poltrona - 1) // self.__colunas
        try:
            assert position_in_the_matriz < self.__linhas
            assentos_fileira = self.__matriz[position_in_the_matriz]
            posicao_assento = assentos_fileira[(numero_poltrona - 1) % self.__colunas]
            return (assentos_fileira, posicao_assento)

        except AssertionError:
            raise IndexError("Assento não existe")


    def pesquisaPassageiro(self, nome:str )->int:
        '''Retorna o número da poltrona em que um determinado
           passageiro está ocupando'''
        id_poltrona = 0
        try:
            for i in range(self.__matriz):
                for j in range(self.__matriz[i]):
                    id_poltrona =+ 1
                    if nome == self.__matriz[i][j].get_nome():
                        return id_poltrona
            assert id_poltrona == self.__cadeiras_maximas
        except AssertionError:        
            raise IndexError("Passageiro não encontrado")

    def getPassageiro(self, num_poltrona: int)->Passageiro:
        try:
            posicao = self.pesquisar_assento(num_poltrona)
            return self.__matriz[posicao[0]][posicao[1]]
              
        except IndexError:
            raise IndexError("Assento não existe")

    def trocarPoltrona(self, poltrona_atual:int, nova_poltrona:int)->bool:
        '''Troca o passageiro de uma poltrona para outra'''
        try:
            posicao_poltrona_atual = self.pesquisar_assento(poltrona_atual)
            posicao_nova_poltrona = self.pesquisar_assento(nova_poltrona)
            if self.__matriz[posicao_nova_poltrona[0]][posicao_nova_poltrona[1]] is None:
                self.__matriz[posicao_nova_poltrona[0]][posicao_nova_poltrona[1]] = self.__matriz[posicao_poltrona_atual[0]][posicao_poltrona_atual[1]]
                self.__matriz[posicao_poltrona_atual[0]][posicao_poltrona_atual[1]] = None
                return True

            return False

        except IndexError:
            print("Assento não existe")


    def adicionar(self, passageiro: Passageiro, numero_poltrona:int)->bool:
        '''Retorna True se a inserção foi feita com sucesso, ou 
           False caso contrário'''
        try:
            posicao = self.pesquisar_assento(numero_poltrona)
            if self.__matriz[posicao[0]][posicao[1]] is None:
                self.__matriz[posicao[0]][posicao[1]] = passageiro
                return True
            
            return False

        except IndexError:
            raise IndexError("Assento não existe")
        

    def remover(self, numero_poltrona:int)->Passageiro:
        try:
            posicao = self.perquisar_assento(numero_poltrona)
            self.__matriz[posicao[0]][posicao[1]] = None

        except IndexError: 
            raise IndexError("Assento não existe")

    def esvaziar(self):
        '''Esvazia a matriz esparsa'''
        for i in range(len(self.__matriz)):
            for j in range(len(self.__matriz[i])):
                self.__matriz[i][j] = None

    def mostrarAssentos(self):
        '''Mostra o status de ocupacao de todos os assentos'''
        cadeiras = ""
        for i in range(self.__linhas):
            
            for j in range(self.__colunas):
                if self.__matriz[i][j] is None:
                    cadeiras += f"fileira {i + 1} - coluna {j + 1} Vazia, "

                else:
                    cadeiras += f"fileira {i + 1} - coluna{j + 1} Ocupada, "

            cadeiras += "\n"

        return cadeiras
                

    def __str__(self):
        return f'{self.__id}, {self.tamanho()} assentos.'



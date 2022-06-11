matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
colunas = 4
linhas = 3


def pesquisar(numero_poltrona:int):
        '''Retorna os dados do passageiro alocado em um
           determinado assento'''
        position_in_the_matriz = (numero_poltrona - 1) // colunas
        try:
            assert position_in_the_matriz < linhas
            assentos_fileira = matriz[position_in_the_matriz]
            resultado = assentos_fileira[(numero_poltrona - 1) % colunas]
            print(resultado)

        except AssertionError:
            print("Assento não existe")

pesquisar(4)



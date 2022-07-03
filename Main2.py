from Empresa import Empresa
from OnibusError import OnibusError
from PasengerError import PasengerError
from AssentoError import AssentoError
from Passageiro import Passageiro

empresa = Empresa()


comandos = {
    1: "Adicionar passageiro",
    2: "remover passageiro",
    3: "Procurar passageiro",
    4: "Trocar passageiro",
    5: "Quantidade assentos",
    6: "Mostrar assentos",
    7: "cadastrar ônibus",
    8: "Assento disponível",
    9: "Esvaziar ônibus",
    10: "Assento tem passageiro",
    999: "Exit"
}

while True:
    print(f'''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
  O que deseja realizar?
  [1]   - Cadastrar passageiro
  [2]   - Remover passageiro
  [3]   - Procurar passageiro
  [4]   - Alterar poltrona do passageiro
  [5]   - Consultar quantidade de assentos
  [6]   - Mostrar assentos
  [7]   - Cadastrar ônibus
  [8]   - Procurar assento disponível
  [9]  - Esvaziar poltronas
  [10] - Ver passageiro de uma poltrona
  [999] - Encerra o programa
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
    try:
        comando = int(input('> Inserir comando: '))
        assert comandos.get(comando) is not None
        if comandos[comando] == "cadastrar ônibus":
            bus_name = input('> Informe o nome do ônibus: ').lower()
            assentos = int(input("> informe a quantidade de assentos: "))
            empresa.set_bus(bus_name, assentos)
            print("ônibus cadastrado")

        elif comandos[comando] == "Adicionar passageiro":
            bus_name = input('> Informe o ônibus: ').lower()
            nome_passageiro = input("Informe o nome do passageiro: ").lower()
            rg = int(input("Informe o rg do passageiro: "))
            assento = int(input("Informe o assento"))
            try:
                resultado = empresa.add_passenger(bus_name, Passageiro(nome_passageiro, rg), assento)
                if resultado:
                    print("Cliente cadastrado com sucesso")

                else:
                    print("Assento em uso")

            except AssentoError as error:
                print(error)

            except OnibusError as error:
                print(error)

        elif comandos[comando] == "Trocar passageiro":
            bus_name = input('> Informe o ônibus: ').lower()
            assento_atual = int(input("> Informe o assento atual do passageiro: "))
            novo_assento = int(input("> Informe o assento da troca: "))
            try:
                resultado = empresa.change_seat(bus_name, assento_atual, novo_assento)
                if resultado:
                    print("Assento trocado com sucesso")

                else:
                    print("Assento já está em uso")

            except AssentoError as error:
                print(error)

            except OnibusError as error:
                print(error)

        elif comandos[comando] == "Procurar passageiro":
            bus_name = input('> Informe o ônibus: ').lower()
            nome = input('> Informe o nome do passageiro: ').lower()
            try:
                print(f"Assento {empresa.search_passenger(bus_name, nome)}")

            except PasengerError as error:
                print(error)

            except OnibusError as error:
                print(error)

        elif comandos[comando] == "Quantidade assentos":
            bus_name = input('> Informe o ônibus: ').lower()
            try:
                print(f"O ônibus possui {empresa.quantity_seats(bus_name)} cadeiras")

            except OnibusError as error:
                print(error)

        elif comandos[comando] == "Mostrar assentos":
            bus_name = input("> Informe o ônibus: ").lower()
            try:
                print(empresa.show_seats(bus_name))

            except OnibusError as error:
                print(error)

        elif comandos[comando] == "Assento disponível":
            bus_name = input("> Informe o ônibus: ").lower()
            try:
                print(f"O assento disponível é o {empresa.search_seat_available(bus_name)}")

            except OnibusError as error:
                print(error)

            except AssentoError as error:
                print(error)

        elif comandos[comando] == "Esvaziar ônibus":
            bus_name = input("> Informe o ônibus: ").lower()
            try:
                empresa.clear_bus(bus_name)
                print("ônibus esvaziado com sucesso")

            except OnibusError as error:
                print(error)

        elif comandos[comando] == "Assento tem passageiro":
            bus_name = input("> Informe o ônibus: ").lower()
            assento = int(input("Informe o assento: "))
            try:
                print(f"O passageiro {empresa.search_seat_passenger(bus_name, assento)}")

            except PasengerError as error:
                print(error)

            except OnibusError as error:
                print(error)

            except AssentoError as error:
                print(error)

        elif comandos[comando] == "remover passageiro":
            bus_name = input("> Informe o ônibus: ").lower()
            assento = int(input("Informe o assento: "))
            try:
                print(f"{empresa.search_seat_passenger(bus_name, assento)}")
                print("Deseja excluir esse cliente? S - sim, N - não")
                confirmacao = input("Digite sua resposta: ").lower()
                if confirmacao == "s":
                    empresa.remove_passenger(bus_name, assento)
                    print("Cliente removido com sucesso")

            except PasengerError as error:
                print(error)

            except OnibusError as error:
                print(error)

            except AssentoError as error:
                print(error)

        elif comando == "Exit":
            break

    except AssertionError:
        print("Comando não existe")

    except ValueError:
        print("Comando inexistente - digite novamente")






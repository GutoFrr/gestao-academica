from os import system

menu = [
    {"id": "1", "name": "Estudante"},
    {"id": "2", "name": "Disciplina"},
    {"id": "3", "name": "Professor"},
    {"id": "4", "name": "Turma"},
    {"id": "5", "name": "Matrícula"},
    {"id": "6", "name": "Sair"},
]

operations_menu = [
    {"id": "1", "name": "Incluir"},
    {"id": "2", "name": "Listar"},
    {"id": "3", "name": "Excluir"},
    {"id": "4", "name": "Alterar"},
    {"id": "5", "name": "Voltar ao menu principal"},
]


def display_menu(menu_list, message):
    print(message)
    for item in menu_list:
        print(f"{ item['id'] }. { item['name'] }")


def get_selected_menu_item(input, list):
    return next(filter(lambda item: item["id"] == input, list), None)


def main():
    while True:
        display_menu(menu, "Bem-vindo!")
        menu_input = input("Selecione a área que deseja acessar: ")

        if menu_input == "6":
            break

        elif get_selected_menu_item(menu_input, menu):
            system("cls")
            selected_item = menu[int(menu_input) - 1]

            while True:
                display_menu(operations_menu,
                             f"Menu de operações - {selected_item['name']}")
                
                operation_input = input("Selecione uma operação: ")

                if operation_input == "5":
                    system("cls")
                    break

                elif get_selected_menu_item(operation_input, operations_menu):
                    selected_operation = operations_menu[int(operation_input) - 1]
                    system("cls")
                    print(f"Você selecionou: {selected_operation["name"]}")
                    print("")
                    
                else:
                    system("cls")
                    print("Opção inválida! Tente novamente.")
                    continue


        else:
            print("Opção inválida! Tente novamente.")
            continue


main()

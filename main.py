from os import system

students = []
disciplines = []
teachers = []
classes = []
enrollments = []

menu = [
    {"id": "1", "name": "Estudante", "active": True, "list": students},
    {"id": "2", "name": "Disciplina", "active": False, "list": disciplines},
    {"id": "3", "name": "Professor", "active": False, "list": teachers},
    {"id": "4", "name": "Turma", "active": False, "list": classes},
    {"id": "5", "name": "Matrícula", "active": False, "list": enrollments},
    {"id": "6", "name": "Sair", "active": True},
]

operations_menu = [
    {"id": "1", "name": "Incluir", "active": True},
    {"id": "2", "name": "Listar", "active": True},
    {"id": "3", "name": "Excluir", "active": False},
    {"id": "4", "name": "Alterar", "active": False},
    {"id": "5", "name": "Voltar ao menu principal", "active": True},
]

def main():
    while True:
        display_menu(menu, "Bem-vindo!")
        menu_input = input("Selecione a área que deseja acessar: ")

        if menu_input == "6":
            break

        elif get_selected_menu_item(menu_input, menu):
            selected_item = menu[int(menu_input) - 1]
            display_operations(selected_item)

        else:
            system("cls")
            print("Opção inválida! Tente novamente.")
            print()

def display_menu(menu_list, message):
    print(message)
    for item in menu_list:
        print(f"{ item['id'] }. { item['name'] }")


def get_selected_menu_item(input, list):
    return next(filter(lambda item: item["id"] == input, list), None)

def display_operations(selected_item):
    system("cls")

    while True:
        if bool(selected_item["active"]) is False:
            print(f'"{selected_item["name"]}" está em desenvolvimento!')
            print()
            break

        display_menu(operations_menu,
                        f"Menu de operações - {selected_item['name']}")
        
        
        operation_input = input("Selecione uma operação: ")

        if operation_input == "5":
            system("cls")
            break

        elif get_selected_menu_item(operation_input, operations_menu):
            selected_operation = operations_menu[int(operation_input) - 1]
            system("cls")

            while True:
                if bool(selected_operation["active"] is False):
                    print(f'"{selected_operation["name"]}" está em desenvolvimento!')
                    print()
                    break

                else:
                    while True:
                        print(f"{selected_operation["name"]}")

                        if (selected_operation["id"] == "1"):
                            new_item = input("Informe o nome do estudante: ")
                            add_item_to_list(selected_item["list"], new_item)
        
                        elif (selected_operation["id"] == "2"):
                            display_operation_list(selected_item["list"])
                            
                        print()
                        break

                    stop = input('Pressione ENTER para continuar...')
                    system("cls")
                    break

        else:
            system("cls")
            print("Opção inválida! Tente novamente.")
            print()

def add_item_to_list(list, new_item):
    list.append(new_item)

def display_operation_list(list):
    if len(list) == 0:
        print("Não há estudantes cadastrados.")
    for item in list:
        print(f"- {item}")

main()

from os import system

students = []
disciplines = []
teachers = []
classes = []
enrollments = []


class MenuItem:
    def __init__(self, id, name, active, list):
        self.id = id
        self.name = name
        self.active = active
        self.list = list

    def add_item_to_list(self, new_item):
        self.list.items.append(new_item)

    def display_operation_list(self):
        if len(self.list.items) == 0:
            print(self.list.empty_message)
        for item in self.list.items:
            print(f"- {item}")


class OperationItem:
    def __init__(self, id, name, active):
        self.id = id
        self.name = name
        self.active = active


class OperationList:
    def __init__(self, items, input, empty_message):
        self.items = items
        self.input = input
        self.empty_message = empty_message


student_input = ["Informe o nome do estudante: ",
                 "Informe o CPF do estudante: "]

menu = [
    MenuItem("1", "Estudante", True, OperationList(
        students, student_input, "Não há estudantes cadastrados...")),
    MenuItem("2", "Disciplina", False, OperationList(
        disciplines, {"nome": "Informe o nome da disciplina: "}, "Não há disciplinas cadastradas...")),
    MenuItem("3", "Professor", False, OperationList(
        teachers, {"nome": "Informe o nome do professor: "}, "Não há professores cadastrados...")),
    MenuItem("4", "Turma", False, OperationList(
        classes, {"nome": "Informe o nome da turma: "}, "Não há turmas cadastradas...")),
    MenuItem("5", "Matrícula", False, OperationList(
        enrollments, {"nome": "Informe o nome da matrícula: "}, "Não há matrículas cadastradas...")),
    MenuItem("6", "Sair", True, OperationList),
]

operations_menu = [
    OperationItem("1", "Incluir", True),
    OperationItem("2", "Listar", True),
    OperationItem("3", "Excluir", False),
    OperationItem("4", "Alterar", False),
    OperationItem("5", "Voltar ao menu principal", True),
]


def main():
    system("cls")
    while True:
        display_menu(menu, "Bem-vindo!")
        menu_input = input("Selecione a área que deseja acessar: ")

        if menu_input == "6":
            break

        elif get_selected_menu_item(menu_input, menu):
            display_operations(menu_input)

        else:
            system("cls")
            print("Opção inválida! Tente novamente.")
            print()


def display_menu(menu_list, message):
    print(message)
    print()
    for item in menu_list:
        print(f"{ item.id }. { item.name }")
    print()


def get_selected_menu_item(input, list):
    return next(filter(lambda item: item.id == input, list), None)


def display_operations(menu_input):
    selected_item = menu[int(menu_input) - 1]
    system("cls")

    while True:
        if bool(selected_item.active) is False:
            print(f'"{selected_item.name}" está em desenvolvimento!')
            print()
            break

        display_menu(operations_menu,
                     f"***** Menu de operações - {selected_item.name} *****")

        operation_input = input("Selecione uma operação: ")

        if operation_input == "5":
            system("cls")
            break

        elif get_selected_menu_item(operation_input, operations_menu):
            selected_operation = operations_menu[int(operation_input) - 1]
            system("cls")

            while True:
                if bool(selected_operation.active is False):
                    print(f'"{selected_operation.name}" está em desenvolvimento!')
                    print()
                    break

                else:
                    while True:
                        print(f"{selected_operation.name}")
                        print()

                        if (selected_operation.id == "1"):
                            if selected_item.name == "Estudante":
                                user_name = input(
                                    selected_item.list.input[0])

                                user_cpf = input(selected_item.list.input[1])

                                new_user = {"codigo": len(
                                    students) + 1, "nome": user_name, "cpf": user_cpf}

                                selected_item.add_item_to_list(new_user)

                        elif (selected_operation.id == "2"):
                            selected_item.display_operation_list()

                        print()
                        break

                    stop = input('Pressione ENTER para continuar...')
                    system("cls")
                    break

        else:
            system("cls")
            print("Opção inválida! Tente novamente.")
            print()


main()

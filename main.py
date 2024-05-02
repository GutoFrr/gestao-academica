from os import system


class MenuItem:
    def __init__(self, id, name, active, empty_message):
        self.id = id
        self.name = name
        self.active = active
        self.list = []
        self.empty_message = empty_message

    def add_item_to_list(self, new_item):
        self.list.append(new_item)

    def display_operation_list(self):
        if len(self.list) == 0:
            print(self.empty_message)
        for item in self.list:
            print(f"- {item}")

    def remove_item(self, item):
        self.list.remove(item)

    def get_list_item(self, input):
        return next(filter(lambda item: item['codigo'] == input, self.list), None)


students = []
disciplines = []
teachers = []
classes = []
enrollments = []


class Student(MenuItem):
    def __init__(self):
        self.id = "1"
        self.name = "Estudante"
        self.active = True
        self.list = students
        self.empty_message = "Não há estudantes cadastrados..."

    def add_student(self):
        student_name = input(
            "Informe o nome do estudante: ")

        student_cpf = input(
            "Informe o CPF do estudante: ")

        new_student = {"codigo": len(
            self.list) + 1, "nome": student_name, "cpf": student_cpf}

        self.add_item_to_list(new_student)

    def remove_student(self):
        student_code = input(
            "Informe o código do estudante que deseja exculir: ")

        if student_code.isnumeric():
            selected_student = self.get_list_item(int(student_code))

            if selected_student != None:
                self.remove_item(selected_student)

                print()
                print(f"Estudante: {selected_student} removido com sucesso!")

            else:
                print()
                print("Estudante não encontrado...")
        else:
            print()
            print("O código deve ser um número.")

    def edit_student(self):
        student_code = input(
            "Informe o código do estudante que deseja editar os dados: ")

        if student_code.isnumeric():
            selected_student = self.get_list_item(int(student_code))

            if selected_student != None:
                print(f"Você selecionou o estudante: {selected_student}")
                print()

                selected_student['nome'] = input(
                    "Informe outro nome para o estudante: ")
                selected_student['cpf'] = input(
                    "Informe outro cpf para o estudante: ")
                print()

                print("Dados do estudante editados com sucesso!")
                print(selected_student)

            else:
                print()
                print("Estudante não encontrado...")
        else:
            print()
            print("O código deve ser um número.")

    def trigger_operation(self, operation):
        if operation == "1":
            self.add_student()
        elif operation == "3":
            self.remove_student()
        elif operation == "4":
            self.edit_student()


class Discipline(MenuItem):
    def __init__(self):
        self.id = "2"
        self.name = "Disciplina"
        self.active = False
        self.list = disciplines
        self.empty_message = "Não há disciplinas cadastradas..."


class Teacher(MenuItem):
    def __init__(self):
        self.id = "3"
        self.name = "Professor"
        self.active = False
        self.list = teachers
        self.empty_message = "Não há professores cadastrados..."


class Class(MenuItem):
    def __init__(self):
        self.id = "4"
        self.name = "Turma"
        self.active = False
        self.list = classes
        self.empty_message = "Não há turmas cadastradas..."


class Enrollment(MenuItem):
    def __init__(self):
        self.id = "5"
        self.name = "Matrícula"
        self.active = False
        self.list = enrollments
        self.empty_message = "Não há matrículas cadastradas..."


class Logout(MenuItem):
    def __init__(self):
        self.id = "6"
        self.name = "Sair"
        self.active = True


menu = [Student(), Discipline(), Teacher(), Class(), Enrollment(), Logout()]


class OperationItem:
    def __init__(self, id, name, active):
        self.id = id
        self.name = name
        self.active = active


operations_menu = [
    OperationItem("1", "Incluir", True),
    OperationItem("2", "Listar", True),
    OperationItem("3", "Excluir", True),
    OperationItem("4", "Alterar", True),
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
        print(f"{item.id}. {item.name}")
    print()


def get_selected_menu_item(input, list):
    return next(filter(lambda item: item.id == input, list), None)


def press_enter_to_stop():
    print()
    stop = input('Pressione ENTER para continuar...')

    system("cls")


def display_operations(menu_input):
    system("cls")
    while True:
        selected_item = menu[int(menu_input) - 1]

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

                if selected_operation.id == "2":
                    selected_item.display_operation_list()

                    press_enter_to_stop()
                    break

                if selected_item.name == "Estudante":
                    student = Student()
                    while True:
                        print(f"{selected_operation.name}")
                        print()

                        student.trigger_operation(selected_operation.id)

                        break

                    press_enter_to_stop()
                    break

        else:
            system("cls")
            print("Opção inválida! Tente novamente.")
            print()


main()

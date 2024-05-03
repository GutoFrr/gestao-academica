from os import system
import json


lists = {
    "students": [],
    "disciplines": [],
    "teachers": [],
    "classes": [],
    "enrollments": [],
}


class MenuItem:
    def __init__(self, id, name, label, active, empty_message):
        self.id = id
        self.name = name
        self.label = label
        self.active = active
        self.list = lists[self.name]
        self.empty_message = empty_message

    def add_item_to_list(self, new_item):
        self.list.append(new_item)

    def display_operation_list(self):
        if len(lists[self.name]) == 0:
            print(self.empty_message)
        for item in lists[self.name]:
            print(f"- {item}")

    def remove_item(self, item):
        self.list.remove(item)

    def get_list_item(self, code):
        if str(code).isnumeric():
            return next(filter(lambda item: item['codigo'] == int(code), self.list), None)

        else:
            print()
            print("O código deve ser um número.")

    def get_alternative_list_item(self, code, list):
        if str(code).isnumeric():
            return next(filter(lambda item: item['codigo'] == int(code), list), None)

        else:
            print()
            print("O código deve ser um número.")

    def save_in_json(self):
        with open('data.json', 'w') as file:
            json.dump(lists, file)


class Student(MenuItem):
    def __init__(self):
        self.id = "1"
        self.name = "students"
        self.label = "Estudante"
        self.active = True
        self.list = lists["students"]
        self.empty_message = "Não há estudantes cadastrados..."

    def add_student(self):
        student_name = input(
            "Informe o nome do estudante: ")

        student_cpf = input(
            "Informe o CPF do estudante: ")

        new_student = {"codigo": len(
            self.list) + 1, "nome": student_name, "cpf": student_cpf}

        self.add_item_to_list(new_student)

        print()
        print("Novo estudante adicionado com sucesso!")

    def remove_student(self):
        student_code = input(
            "Informe o código do estudante que deseja exculir: ")

        selected_student = self.get_list_item(student_code)

        if selected_student != None:
            self.remove_item(selected_student)

            print()
            print(f"Estudante: {selected_student} removido com sucesso!")

        else:
            print()
            print("Estudante não encontrado...")

    def edit_student(self):
        student_code = input(
            "Informe o código do estudante que deseja editar os dados: ")

        selected_student = self.get_list_item(student_code)

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

    def trigger_operation(self, operation):
        if operation == "1":
            self.add_student()
        elif operation == "3":
            self.remove_student()
        elif operation == "4":
            self.edit_student()

        self.save_in_json()


class Teacher(MenuItem):
    def __init__(self):
        self.id = "2"
        self.name = "teachers"
        self.label = "Professor"
        self.active = True
        self.list = lists["teachers"]
        self.empty_message = "Não há professores cadastrados..."

    def add_teacher(self):
        teacher_name = input(
            "Informe o nome do professor: ")

        teacher_cpf = input(
            "Informe o CPF do professor: ")

        new_teacher = {"codigo": len(
            self.list) + 1, "nome": teacher_name, "cpf": teacher_cpf}

        self.add_item_to_list(new_teacher)

        print()
        print("Novo professor adicionado com sucesso!")

    def remove_teacher(self):
        teacher_code = input(
            "Informe o código do professor que deseja exculir: ")

        selected_teacher = self.get_list_item(teacher_code)

        if selected_teacher != None:
            self.remove_item(selected_teacher)

            print()
            print(f"Professor: {selected_teacher} removido com sucesso!")

        else:
            print()
            print("Professor não encontrado...")

    def edit_teacher(self):
        teacher_code = input(
            "Informe o código do professor que deseja editar os dados: ")

        selected_teacher = self.get_list_item(teacher_code)

        if selected_teacher != None:
            print(f"Você selecionou o professor: {selected_teacher}")
            print()

            selected_teacher['nome'] = input(
                "Informe outro nome para o professor: ")
            selected_teacher['cpf'] = input(
                "Informe outro cpf para o professor: ")
            print()

            print("Dados do professor editados com sucesso!")
            print(selected_teacher)

        else:
            print()
            print("Professor não encontrado...")

    def trigger_operation(self, operation):
        if operation == "1":
            self.add_teacher()
        elif operation == "3":
            self.remove_teacher()
        elif operation == "4":
            self.edit_teacher()

        self.save_in_json()


class Discipline(MenuItem):
    def __init__(self):
        self.id = "3"
        self.name = "disciplines"
        self.label = "Disciplina"
        self.active = True
        self.list = lists["disciplines"]
        self.empty_message = "Não há disciplinas cadastradas..."

    def add_discipline(self):
        discipline_name = input(
            "Informe o nome da disciplina: ")

        new_discipline = {"codigo": len(self.list) + 1,
                          "nome": discipline_name}

        self.add_item_to_list(new_discipline)

        print()
        print("Nova disciplina adicionada com sucesso!")

    def remove_discipline(self):
        discipline_code = input(
            "Informe o código da disciplina que deseja exculir: ")

        selected_discipline = self.get_list_item(discipline_code)

        if selected_discipline != None:
            self.remove_item(selected_discipline)

            print()
            print(f"Disciplina: {selected_discipline} removida com sucesso!")

        else:
            print()
            print("Disciplina não encontrada...")

    def edit_discipline(self):
        discipline_code = input(
            "Informe o código da disciplina que deseja editar: ")

        selected_discipline = self.get_list_item(discipline_code)

        if selected_discipline != None:
            print(f"Você selecionou a disciplina: {selected_discipline}")
            print()

            selected_discipline['nome'] = input(
                "Informe outro nome para o professor: ")

            print()

            print("Dados da disciplina editados com sucesso!")
            print(selected_discipline)

        else:
            print()
            print("Disciplina não encontrada...")

    def trigger_operation(self, operation):
        if operation == "1":
            self.add_discipline()
        elif operation == "3":
            self.remove_discipline()
        elif operation == "4":
            self.edit_discipline()

        self.save_in_json()


class Class(MenuItem):
    def __init__(self):
        self.id = "4"
        self.name = "classes"
        self.label = "Turma"
        self.active = True
        self.list = lists["classes"]
        self.empty_message = "Não há turmas cadastradas..."

    def add_class(self):
        teacher_code = input("Informe o código do professor desta turma: ")
        selected_teacher = self.get_alternative_list_item(
            teacher_code, lists["teachers"])
        if selected_teacher == None:
            print(f"Professor com código '{teacher_code}' não encontrado...")
            return

        discipline_code = input(
            "Informe o código da disciplina desta turma: ")
        selected_discipline = self.get_alternative_list_item(
            discipline_code, lists["disciplines"])
        if selected_discipline == None:
            print(f"Disciplina com código '{
                  discipline_code}' não encontrada...")
            return

        new_class = {"codigo": len(self.list) + 1,
                     "codigo_professor": selected_teacher["codigo"],
                     "codigo_disciplina": selected_discipline["codigo"],
                     }

        self.add_item_to_list(new_class)

        print()
        print("Nova turma adicionada com sucesso!")

    def remove_class(self):
        class_code = input(
            "Informe o código da turma que deseja exculir: ")

        selected_class = self.get_list_item(class_code)

        if selected_class != None:
            self.remove_item(selected_class)

            print()
            print(f"Turma: {selected_class} removida com sucesso!")

        else:
            print()
            print("Turma não encontrada...")

    def edit_class(self):
        class_code = input(
            "Informe o código da turma que deseja editar: ")

        selected_class = self.get_list_item(class_code)

        if selected_class != None:
            print(f"Você selecionou a turma: {selected_class}")
            print()

            teacher_code = input(
                "Informe o código de um professor desta turma: ")
            selected_teacher = self.get_alternative_list_item(
                teacher_code, lists["teachers"])
            if selected_teacher == None:
                print(f"Professor com código '{
                      teacher_code}' não encontrado...")
                return

            discipline_code = input(
                "Informe o código de uma disciplina desta turma: ")
            selected_discipline = self.get_alternative_list_item(
                discipline_code, lists["disciplines"])

            if selected_discipline == None:
                print(f"Disciplina com código '{
                      discipline_code}' não encontrada...")
                return

            selected_class["codigo_professor"] = selected_teacher["codigo"]
            selected_class["codigo_disciplina"] = selected_discipline["codigo"]

            print()

            print("Dados da turma editados com sucesso!")
            print(selected_class)

        else:
            print()
            print("Turma não encontrada...")

    def trigger_operation(self, operation):
        if operation == "1":
            self.add_class()
        elif operation == "3":
            self.remove_class()
        elif operation == "4":
            self.edit_class()

        self.save_in_json()


class Enrollment(MenuItem):
    def __init__(self):
        self.id = "5"
        self.name = "enrollments"
        self.label = "Matrícula"
        self.active = True
        self.list = lists["enrollments"]
        self.empty_message = "Não há matrículas cadastradas..."

    def add_enrollment(self):
        student_code = input(
            "Informe o código do estudante para esta matrícula: ")
        selected_student = self.get_alternative_list_item(
            student_code, lists["students"])
        if selected_student == None:
            print(f"Estudante com código '{student_code}' não encontrado...")
            return

        class_code = input(
            "Informe o código da turma para esta matrícula: ")
        selected_class = self.get_alternative_list_item(
            class_code, lists["classes"])
        if selected_class == None:
            print(f"Turma com código '{class_code}' não encontrada...")
            return

        new_enrollment = {"codigo": len(self.list) + 1,
                          "codigo_estudante": selected_student["codigo"],
                          "codigo_turma": selected_class["codigo"],
                          }

        self.add_item_to_list(new_enrollment)

        print()
        print("Nova matrícula adicionada com sucesso!")

    def remove_enrollment(self):
        enrollment_code = input(
            "Informe o código da matrícula que deseja exculir: ")

        selected_enrollment = self.get_list_item(enrollment_code)

        if selected_enrollment != None:
            self.remove_item(selected_enrollment)

            print()
            print(f"Matrícula: {selected_enrollment} removida com sucesso!")

        else:
            print()
            print("Matrícula não encontrada...")

    def edit_enrollment(self):
        enrollment_code = input(
            "Informe o código da matrícula que deseja editar: ")

        selected_enrollment = self.get_list_item(enrollment_code)

        if selected_enrollment != None:
            print(f"Você selecionou a matrícula: {selected_enrollment}")
            print()

            student_code = input(
                "Informe o código de um estudante para esta matrícula: ")
            selected_student = self.get_alternative_list_item(
                student_code, lists["students"])
            if selected_student == None:
                print(f"Estudante com código '{
                      student_code}' não encontrado...")
                return

            class_code = input(
                "Informe o código de uma turma para esta matrícula: ")
            selected_class = self.get_alternative_list_item(
                class_code, lists["classes"])
            if selected_class == None:
                print(f"Turma com código '{class_code}' não encontrada...")
                return

            selected_enrollment["codigo_estudante"] = selected_student["codigo"]
            selected_enrollment["codigo_turma"] = selected_class["codigo"]

            print()
            print("Dados da matrícula editados com sucesso!")
            print(selected_enrollment)

        else:
            print()
            print("Matrícula não encontrada...")

    def trigger_operation(self, operation):
        if operation == "1":
            self.add_enrollment()
        elif operation == "3":
            self.remove_enrollment()
        elif operation == "4":
            self.edit_enrollment()

        self.save_in_json()


class Logout(MenuItem):
    def __init__(self):
        self.id = "6"
        self.name = "logout"
        self.label = "Sair"
        self.active = True
        self.list = []
        self.empty_message = ""


student = Student()
teacher = Teacher()
discipline = Discipline()
menu_class = Class()
enrollment = Enrollment()
logout = Logout()

menu = [student, teacher, discipline, menu_class, enrollment, logout]


class OperationItem:
    def __init__(self, id, name, label, active):
        self.id = id
        self.name = name
        self.label = label
        self.active = active


operations_menu = [
    OperationItem("1", "add", "Incluir", True),
    OperationItem("2", "list", "Listar", True),
    OperationItem("3", "delete", "Excluir", True),
    OperationItem("4", "update", "Alterar", True),
    OperationItem("5", "logout", "Voltar ao menu principal", True),
]


def main():
    system("cls")
    load_json_data()
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
        print(f"{item.id}. {item.label}")
    print()


def get_selected_menu_item(input, list):
    return next(filter(lambda item: item.id == input, list), None)


def press_enter_to_stop():
    print()
    stop = input('Pressione ENTER para continuar...')

    system("cls")


def load_json_data():
    try:
        with open('data.json', 'r') as file:
            json_data = json.load(file)
            for key, value in dict(json_data).items():
                lists[key] = value
    except FileNotFoundError:
        return


def display_operations(menu_input):
    system("cls")
    while True:
        selected_menu = get_selected_menu_item(menu_input, menu)

        if bool(selected_menu.active) is False:
            print(f'"{selected_menu.label}" está em desenvolvimento!')
            print()
            break

        display_menu(operations_menu,
                     f"***** Menu de operações - {selected_menu.label} *****")

        operation_input = input("Selecione uma operação: ")

        if operation_input == "5":
            system("cls")
            break

        elif get_selected_menu_item(operation_input, operations_menu):
            selected_operation = operations_menu[int(operation_input) - 1]
            system("cls")

            while True:
                if bool(selected_operation.active is False):
                    print(
                        f'"{selected_operation.label}" está em desenvolvimento!')
                    print()
                    break

                print(f"{selected_menu.label} - {selected_operation.label}")
                print()

                if selected_operation.id == "2":
                    selected_menu.display_operation_list()

                else:
                    if selected_menu.label == "Estudante":
                        student = Student()
                        student.trigger_operation(selected_operation.id)

                    elif selected_menu.label == "Professor":
                        teacher = Teacher()
                        teacher.trigger_operation(selected_operation.id)

                    elif selected_menu.label == "Disciplina":
                        discipline = Discipline()
                        discipline.trigger_operation(selected_operation.id)

                    elif selected_menu.label == "Turma":
                        new_class = Class()
                        new_class.trigger_operation(selected_operation.id)

                    elif selected_menu.label == "Matrícula":
                        enrollment = Enrollment()
                        enrollment.trigger_operation(selected_operation.id)

                press_enter_to_stop()
                break

        else:
            system("cls")
            print("Opção inválida! Tente novamente.")
            print()


main()

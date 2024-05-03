from os import system
import json

from lists import lists
from menu_item import MenuItem
from student import Student
from teacher import Teacher
from discipline import Discipline
from menu_class import Class
from enrollment import Enrollment

class Logout(MenuItem):
    def __init__(self):
        self.id = "6"
        self.name = "logout"
        self.label = "Sair"
        self.active = True
        self.list = []
        self.empty_message = ""


menu = [Student(), Teacher(), Discipline(), Class(), Enrollment(), Logout()]


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

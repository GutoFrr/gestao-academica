from menu_item import MenuItem
from lists import lists

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

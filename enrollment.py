from menu_item import MenuItem
from lists import lists


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

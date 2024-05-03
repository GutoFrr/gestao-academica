from menu_item import MenuItem
from lists import lists


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

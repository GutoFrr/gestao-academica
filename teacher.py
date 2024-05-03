from menu_item import MenuItem
from lists import lists


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

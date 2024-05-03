from menu_item import MenuItem
from lists import lists


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

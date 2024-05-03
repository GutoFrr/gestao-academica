import json
from lists import lists

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
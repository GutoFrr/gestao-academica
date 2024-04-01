menu = [
  { "id": "1", "name": "Estudante" },
  { "id": "2", "name": "Disciplina" },
  { "id": "3", "name": "Professor" },
  { "id": "4", "name": "Turma" },
  { "id": "5", "name": "Matrícula" },
]

def initialize():
  print("Bem-vindo!")
  for item in menu:
    print(f"{ item['id'] }. { item['name'] }")


def main():
  initialize()
  selected_menu_item = input("Selecione a área que deseja acessar: ")
  
  if next(filter(lambda item: item["id"] == selected_menu_item, menu), None):
    print(f"{menu[int(selected_menu_item) - 1]['name']}")
  else:
    print("Opção inválida! Tente novamente.")
  
main()
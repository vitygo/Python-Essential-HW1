class Editor:
    def view_document(self):
        print("Перегляд документа")

    def edit_document(self):
        print("Редагування документів недоступне")

class ProEditor(Editor):
    def edit_document(self):
        print("Редагування документа доступне")

def main():
    license_key = input("Введіть ліцензійний ключ: ").strip()
    
    if license_key == "PROKEY123":
        editor = ProEditor()
    else:
        editor = Editor()
    
    editor.view_document()
    editor.edit_document()


main()

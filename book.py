from pprint import pprint

class Book():
    def __init__(self):
        self.cook_book = {}
        self.string_list = None

    def read_write(self, file: str, mode: str, context: str = None):
        with open(file, mode) as f:
          match mode:
            case 'r':   self.string_list = [line.strip() for line in f ]
            case 'w':
                if context != None:
                    f.write(context)
                    print(f'Файл {file} удачно презаписан')
                else:
                    print(f'{file} остался без изменений. Передайте что-нибудь в переменную context')
            case 'a':
                if context != None:
                    f.write('\n' + context)
                    print(f'В файл {file} добавлена новая запись')
                else:
                    print(f'{file} остался без изменений. Передайте что-нибудь в переменную context')
            case _:   raise ValueError("Другие режимы пока не предусмотренны. Необходимо передать 'r', 'w', 'a' ")

    def 




book = Book()
book.read_write("recipes.txt", "r", '12345')

pprint(book.string_list)

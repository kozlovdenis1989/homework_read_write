from pprint import pprint


class Book():
    def __init__(self):
        self.cook_book = {}
        self.string_list = []

    # Функция для чтения и записи(перезаписи) файла. Данные при чтении сохраняются в переменную string_list
    # в виде списка строк, знаки преноса удаляются.
    # Данные при записи(перезаписи) сохраняются в файл.
    # Реализованы только три режима.
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

    # Функция преобразования списка из переменной string_list в словарь со списками словарей.
    def conv_to_dict(self):
        start = 0
        new_list = []

        for index in range(len(self.string_list)):
            stop = index
            if self.string_list[index] == '':
                new_list.append(self.string_list[start : stop])
                start = stop + 1

        for ingredients_list  in new_list:
            dish = ingredients_list[0]
            dish_ingredient = []

            for ingredients in ingredients_list[2:]:
                ingredient = ingredients.split('|')
                dish_ingredient.append({'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})

            self.cook_book[dish] = dish_ingredient





book = Book()
book.read_write("recipes.txt", "r", '')

book.conv_to_dict()
pprint(book.cook_book)



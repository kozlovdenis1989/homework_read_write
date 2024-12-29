from pprint import pprint



class Book():
    def __init__(self, file: str = None):
        self.file = file
        self.string_list = self.read_write(self.file)
        self.cook_book = {}

    def read_write(self, file: str = None, mode: str = 'r', content: str = None):
        '''
        Метод для чтения и записи(перезаписи) файла. Данные при чтении сохраняются в переменную string_list
        в виде списка строк, знаки преноса удаляются. Вызывается при инициализации класса.
        Данные при записи(перезаписи) сохраняются в файл.
        Реализованы только три режима.

        :param file: path(str)
        :param mode: str; 'r', 'a', 'w'; необязательный параметр, по умолчанию 'r'
        :param content: str, необязательный параметр, по умолчанию None
        :return: list
        '''
        if file == None:
            return []
        with open(file, mode) as f:
          match mode:
            case 'r':
                self.string_list = [line.strip() for line in f ] + ['']
                return self.string_list
            case 'w':
                if content != None:
                    f.write(content)
                    print(f'Файл {file} успешно записан')
                else:
                    print(f'{file} остался без изменений. Передайте что-нибудь в переменную context')
            case 'a':
                if content != None:
                    f.write(content)
                    print(f'В файл {file} добавлена новая запись')
                else:
                    print(f'{file} остался без изменений. Передайте что-нибудь в переменную context')
            case _:   raise ValueError("Другие режимы пока не предусмотренны. Необходимо передать 'r', 'w', 'a' ")


    def conv_to_dict(self, string_list: list):
        '''
        Метод преобразования списка из переменной string_list. Возвращает словарь со списками словарей, также записывает
        это значение в переменную cook_book. При изменении файла методом read_write,
        необходимо вызвать тот же метод в режиме mode = 'r', для обновления
        string_list.

        :param string_list: list(str); Список из файла
        :return: dict
        '''
        start = 0
        new_list = []
        cook_book = {}

        for index in range(len(string_list)):
            stop = index
            if string_list[index] == '':
                new_list.append(string_list[start : stop])
                start = stop + 1

        for ingredients_list  in new_list:
            dish = ingredients_list[0]
            dish_ingredient = []

            for ingredients in ingredients_list[2:]:
                ingredient = ingredients.split('|')
                dish_ingredient.append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})

            cook_book[dish] = dish_ingredient

        self.cook_book = cook_book
        return self.cook_book


    def get_shop_list_by_dishes(self, dishes: list, person_count: int):
        '''
        Метод подсчета всех ингредиентов, блюд, переданных в переменной dishes, на всех персон person count.
        Все значения dishes должны быть в переменной cook_book, иначе получим ошибку.
        Возвращает словарь со всеми ингредиентами на указанное количество персон.

        :param dishes: list(str)
        :param person_count: int
        :return: dict
        '''
        ingredients = {}

        for dish in dishes:
            if dish not in self.cook_book:
                raise  ValueError(f'В cook_book отсутствует {dish}')
            else:
                for ingredient in self.cook_book[dish]:
                    if ingredient['ingredient_name'] not in ingredients:
                        ingredients[ingredient['ingredient_name']] = {
                            'quantity': ingredient['quantity'] * person_count,
                                                          'measure': ingredient['measure']}
                    else:
                        ingredients[ingredient['ingredient_name']] = {
                            'quantity': ingredients[ingredient['ingredient_name']]['quantity'] + ingredient['quantity'] * person_count,
                                                          'measure': ingredient['measure']}

        return ingredients


# Контент для добавления
content = '\nКапучино\n3\nКофе | 10 | г\nВода | 20 | мл\nМолоко | 40 | мл\n'

# Создаем экземпляр, "recipes.txt" необязательный параметр. Чтение происходит автоматически
# и записывается в переменную string_list.
book = Book()
# book.read_write("recipes.txt", "a", content)

# Метод чтения и записи. Если при создании класса Book не передавать относительный путь, то можно это сделать здесь.
book.read_write("recipes.txt", "r")

# Задание 1. Метод преобразования данных из файла в вид, описанный в задании 1. Результат записывается в cook.book.
book.conv_to_dict(book.string_list)
pprint(book.cook_book)
print()

# Задание 2. Метод подсчета общего количества ингредиентов по переданным параметрам блюд и персон.
pprint(book.get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Утка по-пекински', 'Капучино'], 2))
print()


# Задание 3. Функция создания контента из нескольких файлов с
def create_file(*args):
    '''
    Функция работы со строковой информацией из считываемых файлов. Принимает произвольное количество
    экземпляров класса Book. Возвращает строку, отсортированную в порядке возрастания колличества строк,
    в считытваемых файлах, с добавлением служебной инфонрации вида: 'file name', 'count string'.

    :param args: *args(object)
    :return: str
    '''
    content = []

    for text in args:
        content.append(text.file + '\n' + str(len(text.string_list[:-1])) + '\n' + '\n'.join(text.string_list[:-1]))

    return '\n'.join(sorted(content, key=len))


file = Book()
file.read_write('text/4.txt', "w", create_file(Book('text/1.txt'), Book('text/2.txt'), Book('text/3.txt')))







# print(Book.read_write.__doc__)
# print(Book.conv_to_dict.__doc__)
# print(Book.get_shop_list_by_dishes.__doc__)
# print(create_file.__doc__)
def read_recipes(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        dish_name = ''
        for line in file:
            line = line.strip()
            if not line or line.isdigit():
                continue
            if '|' not in line:
                dish_name = line
                cook_book[dish_name] = []
            else:
                ingredient_name, quantity, measure = line.split(" | ")
                cook_book[dish_name].append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
    return cook_book


def print_recipes(cook_book):
    for dish, ingredients in cook_book.items():
        print(f'{dish}:')
        for ingredient in ingredients:
            print(ingredient)
        print()


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
    return shop_list


def merge_and_sort_files(file_paths, output_file):
    # Список для хранения информации о файлах
    files_info = []

    # Проходимся по каждому файлу
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Читаем весь файл построчно
            content = file.readlines()

            # Подсчитываем количество строк
            num_lines = len(content)

        # Добавляем информацию о файле в список
        files_info.append({
            'path': file_path,
            'num_lines': num_lines,
            'content': content
        })

    # Сортируем файлы по количеству строк
    sorted_files = sorted(files_info, key=lambda x: x['num_lines'])

    # Записываем результат в выходной файл
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_data in sorted_files:
            # Пишем имя файла
            outfile.write(f"{file_data['path']}\n")
            # Пишем количество строк
            outfile.write(f"{file_data['num_lines']}\n")
            # Пишем содержимое файла с отступами
            for line in file_data['content']:
                outfile.write(line)
            # Делаем пустую строку между файлами
            outfile.write("\n")


def main():
    cook_book = read_recipes('recipes.txt')
    print('Задача №-1\n')
    print_recipes(cook_book)
    print('Задача №-2\n')
    result = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)
    for ingredient, info in result.items():
        print(f'{ingredient}: {info}')
    print('Задача №-3\n')
    file_paths = ['1.txt', '2.txt', '3.txt']
    merge_and_sort_files(file_paths, 'result.txt')


if __name__ == '__main__':
    main()


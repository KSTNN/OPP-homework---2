# задача номер 1
print('Задача №-1\n')
cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as file:
    dish_name = ''
    
    for line in file:
        line = line.strip()
        
        if not line:
            continue
        if line.isdigit():
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

# Вывод каждого блюда с ингредиентами в формате словаря с указанием количества ингредиентов
for dish, ingredients in cook_book.items():
    print(f'{dish}:')
    for ingredient in ingredients:
        print(ingredient)
    print()  # Добавляем пустую строку для разделения блюд


# задача номер 2
print('Задача №-2\n')
def get_shop_list_by_dishes(dishes, person_count):
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

# Пример вызова функции
result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
for ingredient, info in result.items():
    print(f'{ingredient}: {info}')

print('-------------------------')

# Задача №3:
with open('1.txt', 'r', encoding='utf-8') as file_1:
    line_1 = {}
    count_1 = 0
    for line in file_1.readlines():
        count_1 += 1
        line_1['1.txt'] = count_1
with open('1.txt', 'r', encoding='utf-8') as file_1:
    text_1 = file_1.read()

with open('2.txt', 'r', encoding='utf-8') as file_2:
    line_2 = {}
    count_2 = 0
    for line in file_2.readlines():
        count_2 += 1
        line_2['2.txt'] = count_2
with open('2.txt', 'r', encoding='utf-8') as file_2:
    text_2 = file_2.read()

with open('3.txt', 'r', encoding='utf-8') as file_3:
    line_3 = {}
    count_3 = 0
    for line in file_3.readlines():
        count_3 += 1
        line_3['3.txt'] = count_3
with open('3.txt', 'r', encoding='utf-8') as file_3:
    text_3 = file_3.read()

join = sorted(list(line_1.items()) + list(line_2.items()) + list(line_3.items()), key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as file_result:
    for line in join:
        file_result.write(f'{line[0]}\n {line[1]}\n {text_2 if line[0] == "2.txt" else text_1 if line[0] == "1.txt" else text_3}\n')




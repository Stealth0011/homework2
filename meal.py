# f = open('meal.txt','r')
# data = f.read()
# print(data, type(data))
# f.close()
# with open('cook_book.txt', encoding="utf-8") as f:
#     data = f.read()
#     print(data)
# from cook_book import mean

# class get_shop_list_by_dishes:
#     def __init__(self, dishes, person_count):
#         self.dishes = meal_name
#         self.person_count = person_count
#         self.count = []

# import json
# data = json.load(open(cook_book.json, 'r', encoding='utf-8'))
# print(data)

def my_cook_book():
    with open('cook_book.txt', encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
    return cook_book
# ⭐ 6.4.2 在字典中存储列表
"""
有时候，需要将列表存储在字典中，而不是将字典存储在列表中。
"""
# 存储所点pizza的信息ℹ、
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
#概述所点从pizza
print(f"You ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"{topping}")
"""
每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。 
"""
print('-------------------------------')
favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
"""
在遍历字典中的主循环中，使用了另一个for循环
"""
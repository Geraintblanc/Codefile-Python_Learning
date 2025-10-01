# 🐳 8.2.3 默认值

"""
编写函数时，可以给每个形参指定默认值。在调用函数中给形参提供
了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。
"""

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物🐈‍⬛的信息"""
    print(f"I hava a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='will')
# 🐳 8.2.2 关键字实参

"""
关键字实参是传递给函数的名称值对。因为直接在实参中将名称
和值关联起来， 所以向函数传递实参时不会混淆。
关键字实参让我们可以无须考虑函数调用的实参顺序，还清楚地
指出了函数第哦啊用中各个值的用途
"""

def describe_pet(animal_type, pet_name):
    """显示宠物🐈‍⬛信息"""
    print(f"I hava a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

"""
关键字实参的顺序无关紧要，因为Python知道各个值该赋给哪个形参，上面的
两个函数实际上是等效的
"""
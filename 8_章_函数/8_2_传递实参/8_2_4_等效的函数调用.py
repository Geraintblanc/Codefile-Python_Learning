# 8.2.4 💡等效的函数调用

"""
鉴于可以混合使用位置实参、关键字实参和默认值，通常有多种的函数调用
方式。
"""

def describe_pet(pet_name, animal_type='dog'):
    "显示宠物的信息"
    print(f"I have a {animal_type}.")
    print(f"MY {animal_type.title()}'s name is {pet_name.title()}.")
# 一只名为Willie的小狗 🐶
describe_pet('willie')
describe_pet(pet_name='willie')

print('-------一只名为Harry的仓鼠🐹-----------')
# 一只名为Harry的小猫
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='harry', pet_name='harry')

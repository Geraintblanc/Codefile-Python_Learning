# 🐳 8.2 传递实参

"""
函数定义中可能包含多个形参，因此函数调用中也可能包含
多个实参。
向函数传递实参的方式很多（主要是以下三种）：
    1️⃣ 位置实参： 这要求实参顺序与形参的顺序相同；
    2️⃣ 关键字实参： 其中每个实参都由变量名和值组成；
    3️⃣ 列表和字典
"""

# 📖 8.2.1 位置实参

"""
⚠️：
    调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个
    形参。
    为此； 最简单的关联方式时基于实参顺序。 这种关联方式称为位置实参。
"""
def describe_pet(animal_type, pet_name):
    """显示宠物🐈‍⬛信息"""
    print(f"I hava a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# 这里的形参和实参的顺序相同
# 刚才调用的函数中，实参'hamster'被赋给形参animal_type,而实参‘harry’附给形参pet_name

# ⭕️ a. 多次调用函数

describe_pet('hunt', 'doudou')

# ⭕️ b. 位置实参的顺序很重要

describe_pet('harry', 'hamster') # 这样输出的结果就有点搞了
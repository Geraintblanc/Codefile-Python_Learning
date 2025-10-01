# 🐮 8.2.5 避免实参错误

"""
提供的实参多于或者少于函数完成工作所需要的信息
时，将出现实参不匹配错误
"""

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

# describe_pet() 如果此时括号里缺少相关的信息，这会出现错误
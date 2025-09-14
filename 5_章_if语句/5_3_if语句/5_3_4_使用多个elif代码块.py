# ⭐ 5.3.4 使用多个elif代码块
"""
可根据需要使用任意数量的elif代码块
"""
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print (f"Your admission cost is ${price}")
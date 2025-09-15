# ⭐ 5.3.5 省略else代码块
"""
Python 并不要求if-elif 结构后面必须有else代码块。
    在有些情况下，else代码块很有用；而在其他一些情况下，使用一条elif语句来处理
    特定的情形更清晰。
"""
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}")

"""
else 是一个包罗万象的语句，只要不满足任何if或者elif中的条件测试，其中
的代码就会执行。这可能引入无效甚至恶意的数据。如果知道最终要测试的条件，应
考虑使用一个elif代码块来代替else代码块。
这样就可以肯定，仅仅当满足相应的条件时，代码才会执行。
"""


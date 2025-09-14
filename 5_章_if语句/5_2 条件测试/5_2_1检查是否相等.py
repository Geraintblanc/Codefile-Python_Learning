# 😘 5.2 条件测试
"""
每条if语句的核心都是一个值为True或False的表达式，这种表达式称为❗条件测试❗
Python 根据条件测试的值为True还是False来决定是否执行if语句中的代码。
    如果条件测试的值为True，Python就执行紧跟在if语句后面的代码；
    如果为false，Python就忽略这些代码
"""
# 🐂 5.2.1 检查是否相等
"""
大多数条件测试将一个变量的当前值同特定值进行比较。
最简单的条件测试检查变量的值是否与特定值相等；
"""
car = 'bmw'
car == 'bmw'
print(car == 'bmw') # True
print(car == 'audi')  # False

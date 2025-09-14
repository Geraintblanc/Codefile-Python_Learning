### ⑤ 第五章 ： if语句
"""
编程时警察需要检查一些列的条件，并据此决定采取什么措施 。
在python中，if语句让你能够检查程序的当前状态，并采取相应的措施。

"""
# cars.py
cars = ['audi', 'bmw', 'subaru',  'toyota']
for car in cars:
    if car == 'bmw':
        print (car.upper())
    else:
        print(car.title())

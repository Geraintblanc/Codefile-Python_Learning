# ⭐ 5.4.3 使用多个列表
"""
🐉：
我们仍然继续之前那个pizza店的代码：
    顾客的要求往往时五花八门，在pizza配料方面也是如此。如果有顾客要在比萨中添加炸薯条
    该怎么办：
        可以使用❗列表和if语句来确定能否满足顾客的要求。
    来看看在制作pizza如何拒绝怪异的配料要求。下面的示例定义了两个列表，其中第一个列表
    包含比萨店供应的配料，而第二个列表包含顾客点的配料。
"""
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                     'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}")
    print("\nFinished making your pizza! ")

# ⭐ 5.4 使用if 语句处理列表
# 😀 5.4.1 检查特殊元素
"""
我们当下要研究如何检查列表中的特殊值，并对其做合适的处理。
    我们要继续使用5.3中使用的例子，这家pizza店在制作pizza时，每添加一种配料都打印一条消息。
    通过创建一个列表，在其中包含顾客点的配料，并使用一个循环来指出添加到pizza中的配料，能够
    以极高的效率编写这样的代码：
"""
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# 然而比如green peppers用完了呢，这种可以在for循环中包含一条if语句：
print("---如果green peppers用完----------")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

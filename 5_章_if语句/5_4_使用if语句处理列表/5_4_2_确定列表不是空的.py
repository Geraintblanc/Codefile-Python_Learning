# ⭐ 5.4.2 确定列表不是空的
"""
到目前为止📍:
    我们对于处理的每个列表都做了一个简单的假设---假设他们都至少包含一个元素。
    因为马上就要让用户来提供存储在列表中的信息，所以不能再假设循环运行时列表
    不是空的。
    由此可见❗：在运行for循环前确定列表是否为空很重要。
"""
"""
我们下面的例子：
    比如在制作比萨时检查顾客点的配料列表是否为空。
    如果列表为空，就像顾客确认是否要点原为比萨；如果
    列表不为空，就像前面的示例那样制作pizza：
"""
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza？")

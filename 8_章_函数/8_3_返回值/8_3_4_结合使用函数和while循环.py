# 🐸 结合使用函数和while循环♻️

"""
下面的例子是将结合使用函数get_formatted_name()
和while循环，以更加正式的方式问候用户。
"""
"""
def get_formatted_name(first_name, last_name):
    返回整洁的姓名
    full_name = f'{first_name} {last_name}'
    return full_name

# 这是一个无限循环
while True:
    print("\nPlease enter your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}! ")
"""

print('----------第二个🥈例子----------')

"""
上面的代码存在问题： 就是没有定义退出条件；
    要是解决这个问题，要让用户能够尽可能容易的退出，因此每次提示🔔用户输入时，有应该有突出途径。
每次提及用户输入时，都使用break语句提供退出循环的简单途径。
"""
def get_formatted_name(first_name, last_name):
    """返回整洁姓名"""
    full_name = (f"{first_name} {last_name}")
    return full_name.title()
while True:
    print("\nPlease enter your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}! ")
# ⚠️： 我们第一个例子因为没有退出⏏️机制所以我直接将第一部分的代码变成了注释👀
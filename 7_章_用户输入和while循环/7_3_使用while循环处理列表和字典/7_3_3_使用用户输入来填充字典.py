# 🌽 7.3.3 使用用户输入来填充字典

# 🏁 可以使用while循环提示🔔用户输入任意多的信息

responses = {}

# 设置一个标志✅， 指出🔬调查是否继续
polling_active = True

while polling_active:
    # 提示🔔输入被调查者的姓名和回答
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday?")

    # 将回答存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查🔬
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == "no":
        polling_active = False

# 调查结果结束显示结果
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would you like to climb {response}.")


# 🐮 👏： 7.3 使用while循环处理列表和字典

"""
我们到目前的7.3为止，我们每次都只处理了一项用户信息：
    💻：获取用户的输入，再将输入打印出来或者做出回答
    💻：循环再次运行时，获悉另一个输入值并做出响应
⚠️：
    注意： 然而要记录📝大量的用户和信息，需要再while循环中使用列表和字典

for循环♻️是一种遍历列表的有效方式，但是不应该在for循环中修改列表，否则将导致
python难以跟踪其中的元素
"""

# 🐮 7.3.1 在列表之间移动元素

# 以下是个例子，在验证用户的同时将其从未验证用户列表中提取出来，再将其中加入另一个
# 已经验证余户列表中

# 首先创建一个待验证用户列表
# 和一个用于存储已经验证用户的空列表

unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# 验证每个用户，知道没有未验证用户为止
# 将每个经过验证的用户都移到已经验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# 显示所有已经验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

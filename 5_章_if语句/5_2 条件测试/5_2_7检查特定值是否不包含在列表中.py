# ⭐ 5.2.7 检查特定值是否不包含在列表中
"""
❗：关键词： ❗： not in
    还有些时候，确定特定到达值未包含在列表中很重要。
    这种情况下，可使用关键字 not in
"""
# 例子： 有一个列表，其中包含被禁止在论坛上发表评论的用户
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
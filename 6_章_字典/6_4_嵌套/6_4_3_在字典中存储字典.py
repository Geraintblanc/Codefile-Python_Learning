# ⭐ 6.4.3 在字典中存储字典
"""
可在字典中嵌套字典，但这样做时，代码可能很快就复杂起来。
例如：
    如果有多个网站用户，每个都有独特的用户名，可在字典中
    将用户名作为键，然后将每位用户的信息存储在一个字典中，
    并将该字典作为于用户相关联的值。
"""
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first':'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
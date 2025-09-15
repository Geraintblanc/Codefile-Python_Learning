# ⭐ 6.4.1 字典列表
"""
什么是嵌套：
    😵将一系列字典存储在列表中，或将列表作为值存储在字典中，这就是嵌套
6.4.1 字典列表
字典alien_0包含一个外星人的各种信息，但是无法存储第二个外星人的信息，更
别说屏幕上全部外星人的信息了
"""
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
"""
结果如下：
    {'color': 'green', 'points': 5}
    {'color': 'yellow', 'points': 10}
    {'color': 'red', 'points': 15}
但是：
    更符合现实情形的是，外星人不止三个，且每个外星人都是使用代码生成的。
    ❗：range()
    我们可以使用range()生成了三十个外星人：
"""
print('\n---------一个详细的案例-----------------')
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人👽
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
    aliens.append(new_alien)
# 显示前5个外星人👽
for alien in aliens[:5]:
    print(alien)
print(f"Total number of aliens: {len(aliens)}") # 打印列表长度，以证明确实创建了30个外星人
"""
这些外星人都有相同的特征，但是在python看来，每个外星人👽都是独立的，这让我们
能够独立的修改每个外星人。
例子：
    可能随着游戏的进行，有些外星人会变色且加快速度，必要时，可使用for循环和if语句来修改
    某些外星人的颜色。
    例如：
    要将前三个外星人👽修改成黄色、速度为中等且值 10 分， 可这样做：
"""
aliens = []
# 创建30个绿色的外星人👽
print('-------------------------------------')
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['speed'] == 'medium'
        alien['points'] = 10
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
#### 上面的代码是修改前三个外星人👽


# ⭐ 6.2.4 修改字典中的值
"""
要修改字典中的值，可依次指定字典名、用方括号括起的键，以及与该键相关联的
新值。
"""
# 例如，假设随着游戏的进行，需要将一个外星人从绿色改成黄色
alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}.") #The alien is green.

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.") #The alien is now yellow.

print('--------一个更加有趣的例子-----------')
"""
我们来看一个个更有趣的例子，对一个能够以不同速度移动的外星人进行位置跟踪。为此
我们将存储该外星人的当前速度，并据此确定外星人将向右移动多远
"""
alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print(f"Original position:{alien_0['x_position']}")

# 向右移动外星人
# 根据当前速度确定将外星人👽向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] =='medium':
    x_increment = 2
else:
    #这个外星人的一度速度肯定很快
    x_increment = 3
    # 新位置为就位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

"""
以下是运行后的结果：
Original position:0
New position: 2
"""
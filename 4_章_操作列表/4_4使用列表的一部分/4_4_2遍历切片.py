# 🐸 4.4.2 遍历切片
# 如果要遍历列表的部分元素，可以在for循环中使用切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


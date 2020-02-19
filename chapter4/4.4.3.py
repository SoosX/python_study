players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
# part two
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)
# 关于切片地复制和单纯的换名字，上下对比
myfoods = ['pizza', 'falafel']
friendfoods = myfoods[:]
myfoods.append('ice cream')
friendfoods.append('carrot cake')
print(myfoods)
print(friendfoods)
# 作业
like = list(likes for likes in range(0, 12))
print(like)
print("The first three items in the list are:")
print(like[0:3])
print("Four items from the middle of the list are:")
print(like[4:8])
print("The last three items in the list are:")
print(like[-3:])
for food in myfoods:
    print(food)

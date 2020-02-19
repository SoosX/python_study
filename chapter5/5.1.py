cars = ['audi','bmw','subaru','toyata']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#part two

required_topping = ['mushromms']
if required_topping != 'anchvies':
    print("hold the anchvies!")

#part three

answer = 17
if answer != 42:
    print("Taht is not the correat answer.Please try again!")

#part four
#关于and 和 or 的运用
#还有in 检查某个值在不在列表内
#关于not in 如下

banned_user =['andrew','carolina','david']
user = 'marie'
if user not in banned_user:
    print(user.title()+",you can post a response if you wish.")
#布尔表达式

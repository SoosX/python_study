roll=['Soos','wulu','king']
print("there are three people I invite")
print(roll)
print("but Soos can not come today")
roll[0]="wtj"
print("so I invite another one,there are they finally")
print(roll)
print("then I found I have a bigger table,so Iinvite more three,so the people will come turns to those guys")
roll.append('one')
roll.append('two')
roll.insert(0,'three')
print(roll)
roll.pop()
print(roll)
roll.pop()
print(roll)
roll.pop()
print(roll)
del roll[1:]
print(roll)

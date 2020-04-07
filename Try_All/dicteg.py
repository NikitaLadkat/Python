alien_0 = {'color': 'green', 'points': 5}
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5

print(alien_0)



set = {'color1':'purple' , 'color2':'pink' , 'color3':'blue'}
print(set)


set['color1'] = 'black'
set['color2'] = 'white'

print(set)

del set['color1']
print(set)


for var,color in set.items():
    print(var+ ":" +color)

print(len(set))
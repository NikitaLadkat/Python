
#Create List that contain -  int , Float , String and list
rainfall = [ 10, 20.10 ,'Nikita' , [1]]
print(rainfall)

#Simple Algo Programs - Find Average
student_grades = [9.1, 8.8, 7.5]
s = sum(student_grades)
l = len(student_grades)
max_value = s/l
print(max_value)

#create a tuple and assign a tuple to it. It should contain three tuples as items.
color_codes =((1,2,3),(2,4,5),(6,7,8))
print(color_codes)


#Create a dictionary in which each day phase should contain at least 3 temp in float in tuple.
day_temperatures ={
    'morning' : (10.0 , 20.0, 28.90) ,
    'noon' : (11.0 , 21.0, 23.90) ,
    'evening' : (10.12 , 23.0, 23.90)
}
print(day_temperatures)


#man-made Dict Eng-German
language ={
    "Sun" : "sonne" ,
    "mouth" : "Mund" ,
    "cycle" : "Fahrrad"
}
print(language["cycle"])

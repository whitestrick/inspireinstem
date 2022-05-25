# a dictionary is a collection of key value pairs
#syntax:dictionary ={'key':'value'}
colours ={'colour':'red'}
vehicle ={'type':'toyota','plate_number':'GTR250'}
#print(type(colours)) #we use the type method to identify the data type
#accessing values in a dictionary

print(vehicle['type']) # you can acces the value of an element inside a dictionary
print(vehicle["plate_number"])

person = {'name':'ivy','phone_no':'0722442266','adress':'22422-langly','gender':'heshe'}
person['age'] = '21' #fomart for adding
person['fav_color'] = ' vanta black'
#print(type(person))
print(person['name'],person['phone_no'],person['adress'],person['gender'])
print(person)
del person['phone_no'] 
#print(person)
#looping over dictionaries
for key,value in person.items():
    print(f"{key} : {value}")
    
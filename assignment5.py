#!/usr/bin/python

#a list of vehicles
vehicles =['bmw','audi','toyota','mercedes','jeep']

for vehicle in vehicles:
    print(vehicle.title())
    
for vehicle in vehicles:
    if (vehicle == "jeep"):
     print(vehicle.upper())

print(vehicles[4].upper())
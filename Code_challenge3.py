# This program calculates the cost of shipping an item based on various factors such as weight, distance, and whether the item is fragile, express, or international.

Sender_name = input("Sender name: ")
Type = input("Type of item: ") 
fragile = bool(input("is it fragile? (yes/no): ") == "yes")
weight = eval(input("weight: ")) 
distance = eval(input("distance: "))
express = bool(input("is it express? (yes/no): ") == "yes")
international = bool(input("is it international? (yes/no): ") == "yes")

base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2.0 and distance <= 100 and not express and not international:
    total = 0.00

elif express and international: 
    total = (base_cost * 1.40) + 50.00

elif express or international and weight >= 20.00: 
    total = (base_cost * 1.20) + 25.00

elif weight >= 30.0 or distance >= 1000.0:
    total = base_cost + 30.00

else: 
    total = base_cost
print("total cost: ", total, " PHP")
print("Weight:", weight, " kg")
print("Distance:", distance, " km")
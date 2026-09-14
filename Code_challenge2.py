a = 1000
b = 500
c = 200
d = 100
e = 50
f = 20
g = 10
h = 5
i = 1

amount = eval(input("\nEnter the Amount of Money to DEPOSIT ---->> ")) 

print(" =================================== BANK ============================= ")
print("\n\tAMOUNT TO DEPOSIT -->","Php",amount)
print()

total = amount // a
amount = amount % a

total2 = amount // b
amount = amount % b

total3 = amount // c
amount = amount % c

total4 = amount // d
amount = amount % d

total5 = amount // e
amount = amount % e

total6 = amount // f
amount = amount % f

total7 = amount // g
amount = amount % g

total8 = amount // h
amount = amount % h

total9 = amount // i
amount = amount % i


print("\t\t  Php1000:",total)
print("\t\t   Php500:",total2)
print("\t\t   Php200:",total3)
print("\t\t   Php100:",total4)
print("\t\t    Php50:",total5)
print("\t\t    Php20:",total6)
print("\t\t    Php10:",total7)
print("\t\t     Php5:",total8)
print("\t\t     Php1:",total9)

print()

print(" ================================= END OF RECIEPT ======================= ")
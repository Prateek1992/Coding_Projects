parrot = "Norwegien Blue"
print(parrot)

"""
ind = [3,4,9,3,6,8]
for i in ind :
    print(parrot[i])
    i+=1
"""

"""
print(parrot[3:6])
print(parrot[:9])
print(parrot[10:])
print(parrot[:6] + parrot[6:])
print(parrot[:])
"""
print(parrot[-4:]) #backword indexing and slicing
print(parrot[0:6:2]) #step slicing in steps of 2, upto not including 6
number = "1234;4567:6789 5748,7639"
separators = number[4::5]
print(separators)
for sep in separators:
    values =number.split(sep)
    print('This is the split with', sep,'->', values)

values2=""
for char in number:
    if char not in separators:
        values2 = values2 + char
    else:
        values2 = values2 +" "

#values2 ="".join(char if char not in separators else " " for char in number).split()
print(values2.split())
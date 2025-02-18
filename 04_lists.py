 ### Lists ###

my_list = list()
my_other_list = []


print(len(my_list))

my_list = [21,52,21,30,14,51,12]

print(my_list)
print(len(my_list))

my_other_list = [21,1.77,"Alex","Rodríguez"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("Alex"))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

age, height, name, surname = my_other_list[2], my_other_list[1], my_other_list[0],my_other_list[3]

print(name)
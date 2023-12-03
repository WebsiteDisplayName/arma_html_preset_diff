# existing_op_falling_water.html
# new_op_falling_water.html

File1 = open("existing_op_falling_water"+".txt","r")
File2 = open("new_op_falling_water"+".txt","r")
List1 = File1.readlines()
List2 = File2.readlines()

print("In List1, but not List2")
DF = [print(x) for x in List1 if x not in List2]
print("\n\n")

print("In List2, but not in List1")
DF = [print(x) for x in List2 if x not in List1]
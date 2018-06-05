print("Hello World in Python")
days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print("-----------------paragraph---------------")
paragraph= """This is a paragraph. It is made up of multiple line and sentences"""
print(paragraph)
counter= 100
miles= 1000.0
print("-----------------String---------------")
name= "Luis"
print(name[0])
print("-----------------Lista---------------")
list= ["abc", 789, 2.45, "Jhon", 70.2]
print("Lista: " + str(list))
print("-----------------Tupla---------------")
tuple= ("abc", 789, 2.45, "Jhon", 70.2)
print(tuple)
print("-----------------dictionaries---------------")
dict= {}
dict["One"]= "This is one"
dict[2] = "This is two"
print(dict["One"])
print("-----------------Operators---------------")
a=10
b=20
print("a+b = " + str(a+b))
print("a-b = " + str(a-b))
print("a*b = " + str(a*b))
print("b/a = " + str(b/a))
print("b%a = " + str(b%a))
print("a**b = " + str(a**b))
var = 100
print("-----------------IF---------------")
if var <200:
    print("Expression value is less than 200")
    if var == 150:
        print("Which is 150")
    elif var == 100:
        print("Which is 100")
    elif var == 50:
        print("Which is 50")
    elif var <50:
        print("Expression value is less than 50")
else:
    print("Could not find true expression")
count = 0

print("-----------------While---------------")
while count < 5:
    print(str(count) + " is less that 5")
    count+=1
else:
    print(str(count) + " is not less that 5")
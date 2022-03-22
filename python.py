#print("Hello World!")


#Bool
a = True
b = False


#Numbers
c = 10 #integer
d = 1.23 #float
#print(d)
#print(type(d))


#Strings
e = "John"
f = 'Boba'
#print(e)
#print(len(e))


#Lists
fruit = ['apple','banana','watermelon']
#print(fruit[1])
#fruit.append('tomato')
#print(fruit)


#Dictionaries
g={"fname":"Jack","lname":"Mallow"}
#print(g)
#print(g["fname"])


#Conditionals
x = 10
y = 10
# if x < y:
#     print("{} is less than {}".format(x, y))
# elif x == y:
#     print("{} is equal to {}".format(x, y))
# else:
#     print("{} is more than {}".format(x, y))


#Loops
users = [{"name":"Bubba"},{"name":"John"},{"name":"Blake"},{"name":"Jeff"}]

# for index in range(len(users)):
#     print(index)
#     print(users[index]["name"])

# for x in users:
#     print(x["name"])
#     print(x)

# i = 6

# while i>0:
#     print(i)
#     i-=1

#continue - using in 
#pass - using in functions as none
#break - breaks out of the functions


#Functions

def _function_name(j,k):
    return(j + k)

print(_function_name(10, 45))

#adding "_" in the name of the function to define user-made function

for i in range(2,5):
    print(i)


# - same as previous functions, but then var is defined in the function's value
def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times(4)

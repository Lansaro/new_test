#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# RESULT: prints 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# RESULT: returns Error (number_of_days_in_a_week_silicon_or_triangle_sides() function is not defined)


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# RESULT: prints 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# RESULT: prints 5


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# RESULT: prints 5 but not "x" as values is not returned/stored to assign it to x var


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# RESULT: prints 3 and then 5 and then shows error


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# RESULT: print 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# RESULT: prints 100 first, then prints 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# RESULT1: prints 7
# RESULT2: prints 14
# RESULT3: prints 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# RESULT: prints 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# RESULT: prints 500 (line 91), then prints 500 (line 95), reassigned and prints 300 (line 96), prints 500 again (line 97)


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# RESULT: b = 500 (prints 500), b = 500 (prints 500), b = 300 (prints 300 inside function), b = 500 (prints 500)


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# RESULT: b = 500 (prints 500), b = 500 (prints 500), b = 300 (prints 300 inside function), b = 300 (prints 300)


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# RESULT: prints 1, then calls bar() and prints 3, then prints 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# RESULT: prints 1 (line 140), prints 3 (line 145), prints 5 (line 141), prints 10 (line 148)
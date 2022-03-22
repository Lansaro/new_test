def list_countdown(x):
    _list=[]
    # for(var= x=5; x>-1; -1){} - in JS
    for num in range(x,-1,-1):
        _list.append(num)
    return _list

# print(list_countdown(5))

#range(x) x = stop
#range(y,x) y = start, x = stop
#range(y,x,z) y = start, x = stop, z = step


def print_and_return(_list):
    print(_list[0])
    return _list[1]

# print(print_and_return([1,2]))


# --- FUNCTIONS 2 ---

# print('ABC')
# print(1+2)

def add_nums(a,b):
    return a+b

# x=add_nums(2, 5)
# print(add_nums(3, 2))
# print(x)


def multiply_nums(a, b):
    return a*b

# total = multiply_nums(5, 10)
# print(total)

# ---

def multiply_nums(a=5, b=10):
    return a*b

# total = multiply_nums()
# print(total)

# ---

def multiply_nums(a=5, b=10):
    return a*b

# total = multiply_nums(b=50, a=3)
# print(total)




# --- OOP (Object Oriented Programming)


import math

#x = int(input("Please give a value for x: "))
#y = int(input("Please give a value for y: "))
#x = 2
#y = 5
#print(x**y)
#print(math.log(x,2))


"""
QUESTION (a)

This scheme of dividing problems into different subproblems is called using a
recursive algorithm
"""

"""
QUESTION (b)

The base case of this recursive algorithm is
"""

"""
QUESTION (c)
"""

def fast_power(x,y):

    if y == 0:
        return 1
    if y == 1:
        return x
    if y % 2 == 0:
        return fast_power(x, y//2) * fast_power(x, y//2)
    else:
        return fast_power(x, y//2) * fast_power(x, y//2) * x


def power_tester():
    for x in range(0,500):
        for y in range(0, 500):
            power = x**y
            fst_power = fast_power(x, y)
            if power != fst_power:
                print("FAIL")
                return
    print("SUCCESS")

#power_tester()

"""
QUESTION (d)
"""

power_dict = {}

def dynamic_fast_power(x,y):

    tup = (x, y)

    if tup in power_dict:
        return power_dict[tup]
    if y == 0:
        return 1
    if y % 2 == 0:
        power_dict[tup] = dynamic_fast_power(x, y//2) * dynamic_fast_power(x, y//2)
        return power_dict[tup]
    else:
        power_dict[tup] = dynamic_fast_power(x, y//2) * dynamic_fast_power(x, y//2) * x
        return power_dict[tup]

def dynamic_power_tester():
    for x in range(0,500):
        for y in range(0, 500):
            power_dict = {}
            power = x**y
            fst_power = dynamic_fast_power(x, y)
            if power != fst_power:
                print("FAIL")
                return
    print("SUCCESS")

#dynamic_power_tester()

"""
QUESTION (e)
"""

bottom_up_dict = {}

def bottom_up_fast_power(x,y):
    tup = (x, y)
    bottom_up_dict[(x, 0)] = 1
    bottom_up_dict[(x, 1)] = x

    for y_val in range(2, y+1):
        if y_val % 2 == 0:
            bottom_up_dict[(x, y_val)] = bottom_up_dict[(x, y_val//2)] * bottom_up_dict[(x, y_val//2)]
        else:
            bottom_up_dict[(x, y_val)] = x * bottom_up_dict[(x, y_val//2)] * bottom_up_dict[(x, y_val//2)]
    return bottom_up_dict[tup]



def bottom_up_power_tester():
    for x in range(0,100):
        for y in range(0, 100):
            bottom_up_dict = {}
            power = x**y
            fst_power = bottom_up_fast_power(x, y)
            if power != fst_power:
                print("FAIL")
                return
    print("SUCCESS")

bottom_up_power_tester()

#print(bottom_up_fast_power(2, 5))

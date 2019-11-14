from math import sqrt
def get_sum(number_1, number_2):
    sum_number = number_1 + number_2
    return sum_number

def get_f(number_1, number_2):
    sum_number = get_sum(number_1, number_2)
    result = sum_number * sum_number
    return result

def get_delta(a,b,c):
    delta = b*b - 4*a*c
    return delta


def quadro(a,b,c):
    delta = get_delta(a,b,c)
    if delta <0:
        root_1 = None
        root_2 = None
    elif delta == 0:
        root_1 = -b/(2*a)
        root_2 = -b/(2*a)
    else:
        root_1 = (-b+sqrt(delta))/(2*a)
        root_2 = (-b-sqrt(delta))/(2*a)
    return root_1, root_2
# print(quadro(1, -3, 1))

def get_f(point_1=[], point_2=[]):
    x1 = point_1[0] 
    y1 = point_1[1]
    x2 = point_2[0]
    y2 = point_2[1]
    a = (y1-y2)/(x1-x2)
    b = (y1*x2 - y2*x1)/(x2-x1)
    return a, b
# print(get_f([1,2],[3,4]))

def hanoi_tower(n):
    '''algorithm to resolve hanoi_tower problem
    - n: number of disk
    - result: count number of disk movement to solve the problem
    '''
    if n == 1:
        return 1
    else: 
        result = 2 * hanoi_tower(n-1) +1
    return result

def hanoi_tower_pow(n):
    result1= pow(2, n) -1 
    return result1

def find_minimum(list_n=[]):
    if len(list_n)==1:
        return list_n[0]
    else:
        




   

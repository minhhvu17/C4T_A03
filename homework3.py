#1
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        result = n * factorial(n-1)
        return result
print(factorial(4))

#2
def fibonaci(m):
    if m == 1:
        return 0
    elif m == 2:
        return 1
    else:
        numbefore1 = fibonaci(m-1)
        numbefore2 = fibonaci(m-2)
        nums = numbefore1 + numbefore2
        return nums
print(fibonaci(10))

#3
def pascal_triangle(x):
    numsList = [1]
    if x == 1:
        return numsList
    elif x == 2:
        numsList.append(1)
        return numsList
    else:
        for a in range(1,x-1):
            numsList.append(pascal_triangle(x-1)[a] + pascal_triangle(x-1)[a-1])
        numsList.append(1)
    return numsList
print(*pascal_triangle(6), sep="   ")


#1

# low = 1
# high = 100
# loop = True
# while loop:
#     mid = (low + high) //2
#     answer = input("số {} có phải không".format(mid))

#     if answer == "c":
#         print("đáp án là {}".format(mid))
#     elif answer == "l":
#         low = mid
#     elif answer == "s":
#         high = mid






#2
# m = input("A number")
# for i in range(1, int(m)+1):
#     if i % 2 == 0:
#         print(i)

#3 
# number = int(input("A number"))
# number -= number % 2
# for i in range(int(number), 0, -2):
#     print(i)

#4
# number = int(input("A number"))
# count = 0 
# if number == 1:
#     print("Đây không là số nguyên tố")
# else:
#     for i in range (2, number):
#         if number % i != 0:
#             count +=1
#     if count == 0:
#         print("Đây là số nguyên tố")
#     elif count != 0:
#         print("Đây không là số nguyên tố ")

#5
loop = True
number = 10
while loop:
    x = input ('Insert a number: ')
    try:
        n=int(x)
        i = 10/n
        print('no prob')
        print('result:', i)
        loop = False
    except ValueError:
        print('khong phai so')
    except ZeroDivisionError:
        print('khong the chia')

    





   



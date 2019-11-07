#
# NOTE: update
# nums[1], nums[2] = nums[2], nums[1]

from random import randint
input_list = []
for i in range(10):
    input_list.append(randint(1,10))
print(input_list)
#a
# new_list = input_list[:3]
# print(new_list)
#b
# new_list = input_list[-3:]
# print(new_list)
#c
#giam dan
# input_list.sort(reverse=True)
# print(input_list)
#tang dan
# input_list.sort()
# print(input_list)
#c'
# for i in range(len(input_list)):
#     for m in range(len(input_list)):
#         if input_list[i]<input_list[m]:
#             input_list[i], input_list[m] = input_list[m], input_list[i]
# print(input_list)

# swapped = True
# while swapped:
#     swapped=False
#     for i in range(len(input_list)-1):
#         if input_list[i]>input_list[i+1]:
#             input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
#             swapped = True
# print(input_list)

# for i in range(len(input_list)):
#     lowest_value = i
#     for j in range (i+1, len(input_list)):
#         if input_list[j] < input_list[lowest_value]:
#             lowest_value = j
#     input_list[i], input_list[lowest_value] = input_list[lowest_value], input_list[i]
# print(input_list)



    

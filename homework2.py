nums = [1,3,4,16,32,8,64,4,128,2,256,31]
nums2 = [1,3,4,16,32,8,64,4,128,2,256,31]
print (nums)
i = len(nums)
h=0
for m in range(i):
    for n in range(i):
        try:
            if nums[m] * nums[n] == 256:
                if nums[m] != nums[n]:
                    if nums[m] != nums2[m]:
                        h= h+1
                    print('So', nums[m],'va', nums[n], 'o vi tri',m+h+1, 'va',n+h+1)
                    del(nums[m])   
        except IndexError:
            i=i-1
            continue
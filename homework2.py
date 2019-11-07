#gh
# NOTE: change a key to other key
# person['sex']= person.pop.('gender')

nums = [1,3,4,16,32,8,64,4,128,2,256,31]
print (nums)
i = len(nums)
for m in range(i):
    for n in range(i):
        try:
            if nums[m] * nums[n] == 256:
                if nums[m] != nums[n]:
                    print('So', nums[m],'va', nums[n], 'o vi tri', m+1, 'va', n+1)
                    del(nums[m])   
        except IndexError:
            i=i-1
            continue
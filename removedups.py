def remove_duplicates(nums):
    count=0
    l=len(nums)
    uniq=[]
    for i in nums:
        for ii in nums:
            if i==ii and i not in uniq:
                uniq.append(i)
                break
    return uniq

nums=[1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
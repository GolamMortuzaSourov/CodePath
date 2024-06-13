def sum_of_number_strings(nums):
    total=0
    for i in nums:
        total=total+int(i)
    return total

print(sum_of_number_strings(["10","20","30"]))
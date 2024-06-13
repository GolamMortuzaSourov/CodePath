def first_unique_char(my_str):
    test = list(my_str)
    count=0
    for i in range (0,len(test)):
        for ii in test:
            if test[i]==ii:
                count=count+1
        if count==1:
            return i
        count=0
    return -1

print(first_unique_char("arkjansfkjffnra"))
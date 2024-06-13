def reverse_str(mystr):
    test = list(mystr)
    l = (len(mystr))-1
    blnk=""
    for i in range(l,-1,-1):
        blnk=blnk+test[i]
    return blnk

print(reverse_str("crap"))
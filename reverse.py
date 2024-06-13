def reverse_only_letters(s):
    lst=list(s)
    final=[]
    fstring=""
    for i in range((len(lst)-1),-1,-1):
        if lst[i]!="-":
            final.append(lst[i])
    for i in range(0,len(lst)):
        if lst[i]=="-":
            final.insert(i,"-")
    for i in final:
        fstring=fstring+i
    return fstring
        
print(reverse_only_letters("a-bC-dEf-ghI"))
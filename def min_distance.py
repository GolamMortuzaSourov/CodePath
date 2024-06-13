def min_distance(words, word1, word2):
    w1index=[]
    w2index=[]
    for i in range(0,len(words)):
        if word1==words[i]:
            w1index.append(i)
        elif word2==words[i]:
            w2index.append(i)
    result=[]
    for i in w1index:
        for ii in w2index:
            result.append(abs(i-ii))
    return min(result)

words = ["the", "quick", "brown", "fox", "jumped","the"]
print(min_distance(words,"the","jumped"))
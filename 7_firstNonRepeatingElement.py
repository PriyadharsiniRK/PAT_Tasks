def firstNonRepeatingElement(list, n):

    for i in range(n):
        #print(n)
        j = 0
        while(j < n):
            #print(" before i:",i,"j:",j)
            if (i != j and list[i] == list[j]):
               # print(" after i:",i,"j:",j)
                break
            j += 1
            #print("j:",j)
        if (j == n):
            
            return list[i]
    return -1
list = [9, 4, 9, 6, 7]
n = len(list)
print("First Non repeating element in the List : ",firstNonRepeatingElement(list, n))
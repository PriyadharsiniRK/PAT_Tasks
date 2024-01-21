str="hello world"
max =0    
for char in str:
    count = 0
    for i in str:
        if i == char:
            count += 1
           # print("i:",i,"count : ",count,"\n")
        if count > max:
            max = count
            frequentChar = char
            #print("max - ",max)
print("Most frequent Character - ",frequentChar,":",max)
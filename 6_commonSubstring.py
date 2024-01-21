str1="ABCEDA"
str2="BCABC"
str = "Geeks ForGeeks is best!"
result = ""
if len(str1) > len(str2):
    str1,str2 = str2,str1
for i in range(len(str1),0,-1):
    for j in range(len(str1) -i+1):
        temp = str1[j:j+1]
        if temp in str2:
            if len(temp) > len(result):
                result=temp
print(result)
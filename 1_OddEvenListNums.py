list1=[10,501,22,37,100,999,87,351]
Evenlist=[]
Oddlist=[]
for num in list1:
   
#num = int(input("Enter a number: "))
    if (num % 2) == 0:
       # print("is Even",num)
        Evenlist.append(num)
        
    else:
       # print(" is Odd",num)
        Oddlist.append(num)
        
print("Even :",Evenlist)
print("Odd :",Oddlist)
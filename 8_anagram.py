#Declare Inputs
string1 = "garden"
string2 = "danger"
 
#Sort Elements
str1 = [string1[i] for i in range(0,len(string1))]
str1.sort()
print(str1)
str2 = [string2[i] for i in range(0,len(string2))]
str2.sort()
print(str1)
 
# the sorted strings are checked
if (str1 == str2):
    print("The strings are anagrams.")
else: 
    print("The strings aren not anagrams.")
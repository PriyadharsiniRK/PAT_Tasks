string = "geeks skeeg"
 
reverseString = ""
for i in string:
    reverseString = i + reverseString
    #print("W : ",reverseString)
 
if (string == reverseString):
    print("Yes! Palindrome")
else:
    print("No,not a Palindrome")

vowels="aeiouAEIOU"
vowelsA="aA"
vowelsE="eE"
vowelsI="iI"
vowelsO="oO"
vowelsU="uU"
string = "Guvi Geeks Network Private Limited"
countA=0
countE=0
countI=0
countO=0
countU=0
for i in string:
    if i in vowelsA :
        countA+=1
    if i in vowelsE :
        countE+=1
    if i in vowelsI :
        countI+=1
    if i in vowelsO :
        countO+=1
    if i in vowelsU :
        countU+=1
print("A =",countA)
print("E =",countE)
print("I =",countI)
print("O =",countO)
print("U =",countU)

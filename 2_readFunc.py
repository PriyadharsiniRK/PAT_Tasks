def readFunc(fileName):
   with open(fileName, "r") as textfile:
         content = textfile.read()
         print(content)
readFunc("testFile.txt")
#print("...")

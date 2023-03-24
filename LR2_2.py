fileName = (input("Enter the name of the file you want to view: "))

with open(fileName) as fN:
    lineContent = [line.rstrip() for line in fN]
    fileLineCount = len(lineContent)

print(fileName,"has",fileLineCount,"lines \n")

i = 1
while i != 0:
    userLineNumber = int(input("Enter the line number of the line you want to view: "))
    if userLineNumber > 0 and userLineNumber <= fileLineCount:
        userLineContent = lineContent[userLineNumber - 1]
        print("Line",userLineNumber,"is",userLineContent,"\n")
    elif userLineNumber == 0:
        i = 0
    else:
        print("Input is not recognized.\nPlease enter a number within the file range ( 1 to",fileLineCount,
              ") or 0 to exit the program.\n")

print("\n\nThank you for using the program.\n")

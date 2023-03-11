inputFileName = input('Enter the file name: ')

fin = open(inputFileName, "r")

fileList = list()

for line in fin:
    line = line.strip('\n')
    fileList.append(line)

cont = True
while cont:
    print('The file has' ,len(fileList), 'lines.')
    lineNo = int(input('Enter a line number [0 to exit/quit]: '))
    if lineNo == 0:
        cont = False
    else:
        print(str(lineNo)+': '+fileList[lineNo-1]+'\n')

fin.close
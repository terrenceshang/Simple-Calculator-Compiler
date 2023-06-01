import sys
import re

def main():

    input = sys.argv[1]
    errorFile = open(input[0:input.index(".")] + ".err", "w")
    evalFile = open(input[0:input.index(".")] + ".eva", "w")
    
    file = open (input, 'r')
    fileData = file.readlines()
    lines = readData(fileData)
    slst = []
    sCheck = True
    for i in range(len(lines)):
        line = lines[i].replace(" ", "")
        lCheck = lexCheck(line)
        pCheck = parseCheck(line)
        if lCheck == False:
            print("lexical error on line " + str(i+1))
            errorFile.write("lexical error on line " + str(i+1) + "\n")
        elif pCheck == False:
            print("parse error on line " + str(i+1))
            errorFile.write("parse error on line " + str(i+1) + "\n")
        else:
            slst.append(line)
    lstSError = semanticCheck(slst)
    for num in lstSError:
        print("semantic error on line " + str(num))
        errorFile.write("semantic error on line " + str(num) + "\n")
        sCheck = False

    file.close()

def semanticCheck(lines):
    leftVal = []
    output = []
    for i in range (len(lines)):
        line = lines[i] 
        left = line[0:line.index("=")]
        right = line[line.index("=")+1:].replace("(", "").replace(")", "").replace("A", " ").replace("S", " ").replace("D", " ").replace("M", " ")
        rightlst = []
        if line == "":
            continue
        else:
            if left not in leftVal:
                leftVal.append(left)
                templst = right.split(" ")
                for temp in templst:
                    check = True
                    for temp2 in temp:
                        if (temp2 == "0") or (temp2 == "1"):
                            pass
                        else:
                            check = False
                            break
                    if check == False:
                        rightlst.append(temp)
                for temp in rightlst:
                    if (temp not in leftVal):
                        output.append(i+1)
                        break
            else:
                output.append(i+1)
    return output

def lexCheck(line):    
    if re.match("^[a-z0-9ASMD()=]*$", line):
        return True
    return False

def parseCheck(line):
    if line == "":
        return True
    count = 0
    for i in line:
        if i == "=":
            count = count + 1
    
    if count == 1:
        return True
    return False

def readData(fileData):

    lstLines = []
    comment = False

    for line in fileData:
        line = line.lstrip().rstrip()

        if "/*" in line:
            comment = True
            line = line[0:line.index("/*")]
            lstLines.append(line)
        elif "*/" in line:
            comment = False
            line = line[line.index("*/")+2:]
            lstLines.append(line)
        elif ("//" in line) and (comment == False):
            line = line[0:line.index("//")]
            if line != "":
                lstLines.append(line)
        elif (comment == False):
            lstLines.append(line)

    return(lstLines)

if __name__ == "__main__":
    main() 

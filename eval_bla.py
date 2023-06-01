import sys
import re

def binDec(binary_string):
    return int(binary_string, 2)

def replacebinDec(input):
    matches = re.findall(r'[+-]?[01]+', input)

    for match in matches:
        decimal = binDec(match)
        input =input.replace(match, str(decimal), 1)
    return input

def regular(input):
    input = input.replace('A', '+').replace('S', '-').replace('M', '*').replace('D', '//')
    return input

def sortLeft(input):
    lines = input.split("\n")
    lhToks = []

    for line in lines:
        equalPos = line.rfind('=')
        lhToks.append(line[0:equalPos])
    return  lhToks

def sortRight(input):
    lines = input.split("\n")
    rhExp = []
    for line in lines:
        equalPos = line.rfind('=')
        rhExp.append(line[equalPos+1:])
    return rhExp

def readData(input):
    matches = re.findall(r'/\*[\s\S]*?\*/|//.*', input)

    for match in matches:
        input = input.replace(match, "", 1)
    input = input.strip()
    return input

def main():
    filename = sys.argv[1]
    file = open (filename, 'r')
    input = file.read()

    input = regular(replacebinDec(readData(input)))

    lines = input.split("\n")
    lstEval = {}

    for line in lines:
        equalPos = line.rfind('=')
        lhs = line[0:equalPos].strip()
        rhs = line[equalPos+1:].strip()

        for temp in lstEval:
            if temp == lhs:
                pass
            else:
                rhs = rhs.replace(temp, lstEval[temp])
        lstEval[lhs] = str(bin(eval(rhs)))

    for i in lstEval:
        if lstEval[i][0] != "-":
            lstEval[i] = lstEval[i][2:]
        else:
            lstEval[i] = "-" + lstEval[i][3:]

    file = open(filename[:-4] + '.eva', 'a')
    file.truncate(0)
    for i in lstEval:
        file.write(i+'['+lstEval[i]+']\n')
    file.close()
    
if __name__ == "__main__":
    main() 

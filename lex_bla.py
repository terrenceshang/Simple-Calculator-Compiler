import ply.lex as lex
import sys

# All tokens must be name in advance
tokens = ("COMMENT", "WHITESPACE", "ID", "BINARY_LITERAL", "A", "S" , "M", "D", "E", "L", "R")

#Token matching rules are written as regexs
t_ID = r'([a-z]|\_) ([a-z]|\_|[0-9])*'
t_WHITESPACE = r'(\ |\t | \n | \r)+'
t_COMMENT = r'(/\* (.|\n)*? \*/) | (//[^\n]*)'
t_BINARY_LITERAL = r'(\-[0-1]+) | [0-1]+ | \+[0-1]+'
t_A = r'[A]'
t_S = r'[S]'
t_M = r'[M]'
t_D = r'[D]'
t_E = r'\='
t_L = r'\('
t_R = r'\)' 

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return "Illegal character '%s'" % t.value[0]

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
        
lex.lex()

file = open (sys.argv[1], 'r')
data = file.read()
lex.input(data)

output = ""
while True:

    tok = lex.token()
    if not tok:
        break
    if tok.type == "WHITESPACE" or tok.type == "COMMENT":
        output = output + tok.type + "\n"
        #print(tok.type)
    elif tok.type == "A" or tok.type == "S" or tok.type == "D" or tok.type == "M" or tok.type == "E" or tok.type == "L" or tok.type == "R":
        output = output + tok.value + "\n"
        #print(tok.value)
    else:
        output = output + tok.type + "," + tok.value + "\n"
        #print(tok.type + "," + tok.value)
        
        
file1 = open(sys.argv[1][0:-4]+".tkn", 'w')    
file1.write(output)

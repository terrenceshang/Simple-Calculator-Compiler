import ply.yacc as yacc
from lex_bla import tokens
import sys

def p_program(p):
    """
    program : statement
            | program statement
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
    
def p_statement(p):
    """
    statement : ID E expression
    """
    p[0] = (p[2], 'ID,' +p[1], p[3])
        
def p_expression(p):
    '''
        expression : expression A term
                   | expression S term
                   | term
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_term(p):
    '''
        term : term M factor
             | term D factor
             | factor
    '''
    if len(p) == 2:
        p[0] = p[1]    
    else:   
        p[0] = (p[2], p[1], p[3])
    
def p_factor(p):
    '''
        factor : L expression R
               | BINARY_LITERAL
               
    '''
    if (len(p) == 2):
        p[0] = ("BINARY_LITERAL," + p[1])
    else:
        p[0] = p[2]

def p_factor_ID(p):
    """
    factor : ID
    """
    p[0] = ("ID,"+p[1])

# Error rule for syntax errors
def p_error(p):
    parser.errok()

def depth_first_traverse(input, level = 1):
    if isinstance(input, tuple):
        wFile.write('\t' * level + input[0] + "\n")
        for next in input[1:]:            
            depth_first_traverse(next, level + 1)
    else:
        wFile.write('\t' * level + input + "\n")


parser = yacc.yacc()
data = sys.argv[1]
file = open (sys.argv[1], 'r')
sInput = file.read()

data = data[0:data.index('.')] + ".ast"
wFile = open(data, "w")
outcome = parser.parse(sInput)

if outcome is not None:
    print("Program" + '\n')
    wFile.write("Program" + '\n')
    for i in outcome:
        depth_first_traverse(i)

wFile.close()

# Simple-Calculator-Compiler

This project consist of 4 files that makes up a compiler. This them being:
- lex: This program check the tokens from input and see if the tokens are in the correct format
- parse: This program checks if the tokens are in the correct order
- Error: This program checks if there are any logical errors from the input
- eval: This program returns the output of the input program if the input passes lex, parse and error.

**Tools**
I used Python with PLY (www.dabeaz.com/ply) when designing this compiler.

Here are the detailed description of the programs:

I created a program which does lexical analysis and a program which does syntactic analysis for a made-up programming language called bla, for binary language.Bla works with binary numbers and uses uppercase characters for its basic arithmetic operators: A for addition, S for subtraction, M for multiplication and D for integer division.

The lexical analyser (lexer) program should check a specified *.bla input program file and convert it into the correct tokens, outputting the tokens to the screen and also into a corresponding *.tkn file.The syntactic analyser (parser) program should check a specified *.bla input program file conforms to the specified grammar and generate an appropriate abstract syntax tree which is output to the screen and to a corresponding *.ast file.

**Input, Output and Testing**

The input *.bla source code file should be specified as a command line parameter when your programs are 
run, e.g.

    lex_bla.py my_program.bla
    
    parse_bla.py my_program.bla
 
The lexical analyser (lexer) lex_bla.py should check the file for tokens based on the definitions below and 
print each token on a new line to the screen and also in a corresponding token file, my_program.tkn. The 
details of how each token should be printed are specified below.
The syntactic analyser (parser) parse_bla.py should check the tokens conform to the grammar defined 
below and construct and output the abstract syntax tree as flat text using depth-first traversal, visiting the 
root, then children from left to right onto the screen and also in a corresponding file, my_program.ast.

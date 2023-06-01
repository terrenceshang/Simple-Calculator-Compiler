# Simple-Calculator-Compiler

This project consist of 4 files that makes up a compiler. This them being:
- lex: This program check the tokens from input and see if the tokens are in the correct format
- parse: This program checks if the tokens are in the correct order
- Error: This program checks if there are any logical errors from the input
- eval: This program returns the output of the input program if the input passes lex, parse and error.

**Tools**
I used Python with PLY (www.dabeaz.com/ply) when designing this compiler.

Here are the detailed description of the programs:

**I will first explain lexical Analysis and Syntactic Analysis**

I created a program which does lexical analysis and a program which does syntactic analysis for a made-up programming language called bla, for binary language.Bla works with binary numbers and uses uppercase characters for its basic arithmetic operators: A for addition, S for subtraction, M for multiplication and D for integer division.

The lexical analyser (lexer) program should check a specified *.bla input program file and convert it into the correct tokens, outputting the tokens to the screen and also into a corresponding *.tkn file.The syntactic analyser (parser) program should check a specified *.bla input program file conforms to the specified grammar and generate an appropriate abstract syntax tree which is output to the screen and to a corresponding *.ast file.

**Input, Output and Testing**

The input *.bla source code file should be specified as a command line parameter when your programs are 
run, e.g.

    lex_bla.py my_program.bla
    
    parse_bla.py my_program.bla
 
The lexical analyser (lexer) lex_bla.py should check the file for tokens based on the definitions below and print each token on a new line to the screen and also in a corresponding token file, my_program.tkn. The details of how each token should be printed are specified below.

The syntactic analyser (parser) parse_bla.py should check the tokens conform to the grammar defined below and construct and output the abstract syntax tree as flat text using depth-first traversal, visiting the root, then children from left to right onto the screen and also in a corresponding file, my_program.ast.

**Tokens**

* Identifiers

An identifier is a sequence of lowercase letters, digits and underscores, starting with either a lowercaseletter or an underscore. Identifiers are also case sensitive.

Output: ID,_VALUE_

Example: If the string 'my_num' is encountered 'ID,my_num' should be the token that is output.

* Numeric Literals

All numeric literals should be binary integers. Numeric literals consist of a binary integer part (with an optional preceding sign, + or -). The integer part is a sequence of one or more binary digits.

Output: BINARY_LITERAL,_VALUE_

Example: If the string '-1011' is encountered 'BINARY_LITERAL,-1011' should be the token that is output.

* Operators

An operator can be one of the following operators: A S M D = ( )

Output: Each operator should be its own token.

Example: If the string '(' is encountered '(' should be the token that is output.

* Whitespace

Whitespace is a sequence of non-printable characters. Non-printable characters includes:space (' '), tab ('\t'), newline ('\n'), carriage return ('\r')...

Output: WHITESPACE

Example: If the tab character '\t' is encountered 'WHITESPACE' should be the token that is output.

* Comments

There are two forms of comments: One starts with /*, ends with */; another begins with // and goes to the end of the line (the end of line character should not be included in this token, rather it should be handled by the whitespace token.)

Output: COMMENT

Example: If the string '// a comment' is encountered 'COMMENT' should be the token to be output.

**Grammar**

The slang grammar uses the notation N*, for a non-terminal N, meaning zero or more repetitions of N. Bold symbols are keywords and should form their own tokens, and other tokens are in italics.

Program → Statement* // this asterisk indicates closure

Statement → identifier = Expression

Expression → Expression A Term

 → Expression S Term
 
 → Term
 
Term → Term M Factor

 → Term D Factor
 
 → Factor
 
Factor → ( Expression )

 → binary
 
 → identifier
 
 
 
 
 
 **Now I will be explaining about the Semantic analyzer**
 
The semantic analysis and error reporting program should analyse the abstract syntax tree generated from a bla input file, do simple semantic analysis using a basic Symbol Table stored in a simple data structure, and then report on any errors which should be output to the screen and also to a corresponding *.err file. Errors from previous stages, lexical analysis and syntactic analysis, should also be output to the screen and written to the *.err file.

The evaluation program should evaluate each statement in a bla input file and output each assigned 
variable with its value in square brackets to the screen and also to a corresponding *.eva file

**Input, Output and Testing**

The input *.bla source code file should be specified as a command line parameter when your 
semantic analysis and error checking program errors_bla.py is run, e.g.

    errors_bla.py my_program.bla

The semantic analysis program should follow on from parsing and check the program for basic 
semantic errors (specified below) and then report the first error identified - whether lexical, 
parse(syntactic) or semantic - outputting it to the screen and also in a corresponding file, 
my_program.err.

The input *.bla source code file should be specified as a command line parameter when your evaluation program eval_bla.py is run, e.g.

    eval_bla.py my_program.bla
   
The evaluation program should evaluate each statement in a bla input file and output each assigned 
variable with its value in square brackets to the screen and also to a corresponding *.eva file.
Download the eval_bla_samples.zip file containing *.bla code input files and their corresponding 
output *.eva files, indicating what the output should look like and can be used to test your program.

Semantic Analysis

Bla has the following two properties, it is:

- “dynamically typed”, in the sense that variables do not have to be explicitly created with a particular type, e.g. int val. Once a variable is assigned a value it is considered to be created.
- “functional”, in the sense that variables should not be mutable. So a variable can only legally be assigned a value/expression once. If a variable is assigned another value/expression later on, it should be considered a semantic error, having been already defined.

So your semantic analysis should perform two checks:

1. If a variable(identifier) is created/defined on the left hand side of an assignment, it should check if it has already been defined, in which case it should generate an appropriate semantic error. 
2. If a variable(identifier) is used in the right hand side of an assignment it should check if it has been defined already, and if not it should generate an appropriate semantic error.

So semantic analysis should be traverse the AST and maintain a simple Symbol Table, which can be a simple data structure.

**Error Reporting**

If one of the semantic errors specified above, or another error from a previous stage, lexical analysis 
or parsing(syntactic analysis), occurs then this should be output to the screen and to a corresponding 
*.err file. It should indicate the type of error (lexical, parse or semantic) and on which line number it 
occurred, e.g. 

    lexical error on line 2
    
To simplify the problem we’ll assume the program file has no empty lines.

**Evaluation**

Evaluation should evaluate using the accepted mathematical operations as defined in bla where A
represents addition, S represents subtraction, M represents multiplication and D represents division 
(Note: This is integer division.). A bla statement has a variable which is assigned to, and this variable 
needs to be output along with its binary value in square brackets after the statement has been 
evaluated, e.g.

    num1[11101]

Also note, that when outputting negative numbers, do not output the twos complement 
representation, but the negative followed by the absolute value, so -5 should be output as -101

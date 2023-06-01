# Simple-Calculator-Compiler

This project consist of 4 files that makes up a compiler. This them being:
- lex: This program check the tokens from input and see if the tokens are in the correct format
- parse: This program checks if the tokens are in the correct order
- Error: This program checks if there are any logical errors from the input
- eval: This program returns the output of the input program if the input passes lex, parse and error.

**Tools**
I used Python with PLY (www.dabeaz.com/ply) when designing this compiler.

Here are the detailed description of the programs:

**Lexical Analyzer**
This program does lexical analysis on files containing messages/posts which you may find in a typical instant messaging or social media application. The messages are saved in *.msg files and contain words, numbers, whitespace, punctuation, hashtags, name references and illegal characters.
This program's task is to create a lexical analyser (lexer) program called lex_msg.py which checks a specified *.msg input message file and converts it into the correct tokens, outputting the tokens to the screen and also into a corresponding *.tkn file.

**Input, Output and Testing**
The input *.msg message file should be specified as a command line parameter when your programs are run, e.g.
 lex_msg.py my_message.msg

**Tokens
Words**
A word is a sequence of uppercase or lowercase alpha characters.
Output: WORD
Example: If the string 'Hello' is encountered 'WORD,Hello' should be the token that is output.
**Numbers**
A number is a non-negative integer, so a sequence of digits.
Output: NUMBER
Example: If the string '789' is encountered 'NUMBER,789' should be the token that is output.
**Whitespace**
Whitespace is a sequence of one or more non-printable characters, which in this case will just be space (' ') or tab ('\t')
Output: WHITESPACE
Example: If the space character ' ' is encountered 'WHITESPACE, ' should be the token that is output.
**Punctuation**
Punctuation can be a single one of the following characters: full-stop (.), comma (,), semi-colon (;), exclamation mark (!) or question mark (?).
Output: PUNCTUATION
Example: If the character '!' is encountered 'PUNCTUATION,!' should be the token that is output.
**Hashtags**
Hashtags are a sequence of characters which start with a hash character (#) followed by any sequence of alphanumeric characters.
Output: HASHTAG
Example: If the string ‘#Made2order’ is encountered ‘HASHTAG,#Made2order’ should be the token 
that is output.
**Name References**
Name references are a sequence of characters which start with an at character (@) followed by any sequence of alpha characters.
Output: NAME
Example: If the string ‘@Mary’ is encountered ‘NAME,@Mary’ should be the token that is output.
**Illegal Characters**
Any other character which does not form part of any token specified above should be classified as illegal.
Output: ILLEGAL
Example: If the character ‘$’ is encountered ‘ILLEGAL,$’ should be the token that is output.

**Syntatic Analyzer**

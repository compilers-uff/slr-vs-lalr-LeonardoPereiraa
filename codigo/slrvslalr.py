# Yacc example
 
import ply.yacc as yacc
 
# Get the token map from the lexer.  This is required.
from toks import tokens

def p_expression_igual(p):
    'S : L igual R'
    ##p[0] = p[1] + p[3]
 
def p_expression_R(p):
    'S : R'
    ##p[0] = p[1]
 
def p_term_multe(p):
    'L : multe R'
    ##p[0] = p[1]
 

def p_term_ident(p):
    'L : ident'
    ##p[0] = p[1]
 
def p_term_L(p):
    'R : L'

# Error rule for syntax errors
def p_error(p):
    if p != None :
        print("erro sintático na entrada " + p.value )
    else :
        print("erro sintático na entrada ")
# Build the parser
parser = yacc.yacc(method="LALR")
#parser = yacc.yacc(method="SLR")
print(parser)

try:
    s = input('entrada para ser analizada > ')
    result = parser.parse(s)
except EOFError:
   print("erro")




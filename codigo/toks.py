
import ply.lex as lex
 

tokens = ( 
    'igual',
    'multe',
    'ident',
 )

t_igual = r'\='
t_multe = r'\*'
t_ident = r'id'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
    print("palavra invalido '%s'" % t.value[0])
    t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()


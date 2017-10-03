import ply.lex as lex
import sys

operators = (
    #Simbolos (Operadores)
    'PLUS',
    'INCREASE',
    'MINUS',
    'DECREASE',
    'TIMES',
    'POW',
    'MODULUS',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'NOTEQUAL',
    'ISEQUAL',
    'DISTINT',
    'COMP',

    #Simbolos (Asignaciones)
    'ASSIGN',
    'PLUS_ASSIGN',
    'MINUS_ASSIGN',
    'MULTIPLY_ASSIGN',
    'DIVIDE_ASSIGN',
    'MOD_ASSIGN',
    'POW_ASSIGN',

    #Simbolos (Compuertas logicas)
    'BIT_NOT',
    'BIT_AND',
    'BIT_OR',
    'BIT_XOR',
    'BIT_COMPLEMENT',
    'BIT_LEFT_SHIFT',
    'BIT_RIGHT_SHIFT',
)

identifiers = (
    #Otros
    'SCALAR_ID',
    'ARRAY_ID',
    'HASH_ID'
)

datatypes = (
    'STRING',
    'INTEGER',
    'HEX',
    'RANGE'
)

reserved = {
    # Palabras reservadas (Estructuras de control)
    'if':'IF',
    'elsif':'ELSIF',
    'else':'ELSE',
    'while':'WHILE',
    'until':'UNTIL',
    'for':'FOR',
    'foreach':'FOREACH',
    'last':'LAST',
    'next':'NEXT',
    'continue':'CONTINUE',
    'return':'RETURN',
    'lt' : 'LESS_STRING',
    'gt' : 'GREATER_STRING',
    'le' : 'LESSEQUAL_STRING',
    'ge' : 'GREATEREQUAL_STRING',
    'eq' : 'ISEQUAL_STRING',
    'ne' : 'NOTEQUAL_STRING',
    'cmp' : 'COMP_STRING',

    #Palabras reservadas (Declaraciones)
    'my':'MY',
    'sub':'SUB',

    #Palabras reservadas (Prefijos)
    'undef':'UNDEF',
    'unless':'UNLESS',
    'use':'USE',
    'package':'PACKAGE',
    'struct' : 'STRUCT',
    'Class' : 'CLASS',
    'new' : 'NEW',
}

# Lista de tokens
tokens = operators + identifiers + datatypes + tuple(reserved.values()) + (
    #Simbolos de sintaxis
    'ARROW',
    'GROSSARROW',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'DOUBLECOLON',
    'QUESTION',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
    'UNDERSCORE',
    'NAME',
    'SUBROUTINE_ID'
)

def t_KEYWORD(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value not in reserved:
        t.type = 'SUBROUTINE_ID'
        return t
    t.type = reserved.get(t.value,'STRING')
    return t

#Reglas (Estructuras de control)
def t_IF(t):
    r'if'
    return t

def t_ELSIF(t):
    r'elsif'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_UNTIL(t):
    r'until'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_LAST(t):
    r'last'
    return t

def t_NEXT(t):
    r'next'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

#Reglas (Declaraciones)
def t_MY(t):
    r'my'
    return t

def t_SUB(t):
    r'sub'
    return t

#Reglas (Prefijos)
def t_UNDEF(t):
    r'undef'
    return t

def t_UNLESS(t):
    r'unless'
    return t

def t_PACKAGE(t):
    r'package'
    return t

def t_DO(t):
    r'do'
    return t

#Reglas (Operadores)
t_PLUS   = r'\+'

def t_INCREASE(t):
    r'\+\+'
    return t

t_MINUS  = r'-'

def t_DECREASE(t):
    r'--'
    return t

t_TIMES  = r'\*'

def t_POW(t):
    r'\*\*'
    return t

t_DIVIDE = r'/'
t_LESS   = r'<'

t_MODULUS = r'%'

def t_LESSEQUAL(t):
    r'<='
    return t

t_GREATER = r'>'

def t_GREATEREQUAL(t):
    r'>='
    return t

t_ASSIGN  = r'='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_MULTIPLY_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='
t_POW_ASSIGN = r'\*\*='

def t_NOTEQUAL(t):
    r'!='
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_COMP(t):
    r'<=>'
    return t

t_BIT_NOT = r'!'
t_BIT_AND = r'&'
t_BIT_OR = r'\|'
t_BIT_XOR = r'\^'
t_BIT_COMPLEMENT = r'~'
t_BIT_LEFT_SHIFT = r'<<'
t_BIT_RIGHT_SHIFT = r'>>'

#Reglas (Sintaxis)
def t_ARROW(t):
    r'\->'
    return t

def t_GROSSARROW(t):
    r'\=>'
    return t

t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'

def t_DOUBLECOLON(t):
    r'::'
    return t

t_QUESTION = r'\?'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'

t_UNDERSCORE = r'\_'

def t_RETURN(t):
	r'return'
	return t

def t_SCALAR_ID(t):
    r'\$[a-zA-Z0-9_#!<?@]+'
    return t

def t_ARRAY_ID(t):
    r'@[a-zA-Z0-9_#!<?]+'
    return t

def t_HASH_ID(t):
    r'%[a-zA-Z][a-zA-Z0-9_#!<?@]*'
    return t

t_STRING = r'(\'[^\']*\')|(\"[^\"]*\")'
t_HEX = r'0[xX][0-9a-fA-F]+'
t_INTEGER = r'0|([1-9][0-9]*)'
t_RANGE = r'\.\.(\.)?'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'\#(.)*\n'
    t.lexer.lineno += 1

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

#Funcion main
if __name__ == '__main__':
	if (len(sys.argv) > 1):#Si se escribe un fichero por la linea de comandos. Ejemplo: python perl-lexer.py archivo.pl
		source = sys.argv[1]
	else:#Si no se escribe el fichero en la linea de comandos, el archivo por defecto es...
		source = 'test.pl'
	f = open(source, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()

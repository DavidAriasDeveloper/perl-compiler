import ply.lex as lex
import sys

operators = (
    #Simbolos (Operadores)
    'PLUS',
    'MINUS',
    'TIMES',
    'MODULUS',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'NOTEQUAL',
    'ISEQUAL',
    'COMP',

    #Simbolos (Asignaciones)
    'ASSIGN',
    'PLUS_ASSIGN',
    'MINUS_ASSIGN',
    'MULTIPLY_ASSIGN',
    'DIVIDE_ASSIGN',
    'MOD_ASSIGN',
    'POW_ASSIGN',
)

identifiers = (
    #Otros
    'DOLLAR',
    'AT',
    'PERCENT'
)

datatypes = (
    'STRING',
    'INTEGER',
    'FLOAT',
    'HEX',
)

reserved = {
    # Palabras reservadas (Estructuras de control)
    'if':'IF',
    'print':'PRINT',
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
    'use':'USE',
    'package':'PACKAGE',
}

# Lista de tokens
tokens = operators + identifiers + datatypes + tuple(reserved.values()) + (
    #Simbolos de sintaxis
    'GROSSARROW',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'AMPERSANT',
    'ID'
)

def t_KEYWORD(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value not in reserved:
        t.type = 'ID'
        return t
    t.type = reserved.get(t.value,'STRING')
    return t

#Reglas (Estructuras de control)
def t_IF(t):
    r'if'
    return t

def t_PRINT(t):
    f'print'
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

def t_PACKAGE(t):
    r'package'
    return t

def t_DO(t):
    r'do'
    return t

#Reglas (Operadores)
t_PLUS   = r'\+'

t_MINUS  = r'-'

t_TIMES  = r'\*'

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


t_AMPERSANT = r'\&'


def t_RETURN(t):
	r'return'
	return t

t_DOLLAR = r'\$'
t_AT = r'@'
t_PERCENT = r'%'

def ID(t):
    r'[a-zA-Z0-9_#!<?]+'
    return t

t_STRING = r'(\'[^\']*\')|(\"[^\"]*\")'
t_HEX = r'0[xX][0-9a-fA-F]+'
t_INTEGER = r'[-+]?([1-9][0-9]*)'
t_FLOAT = r'[-+]?([0-9]*\.[0-9]+|[0-9]+)'

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

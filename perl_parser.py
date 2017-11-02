# -*- coding: utf-8 -*-
import ply.yacc as yacc
from perl_lexer import tokens
import perl_lexer
import sys


VERBOSE = 1

precedence = (
	('left','OR'),
	('left','AND'),
	('left','NOT'),
	('left','LESS','LESSEQUAL','GREATER','GREATEREQUAL','ISEQUAL','NOTEQUAL'),
	('left','LESS_STRING','LESSEQUAL_STRING','GREATER_STRING','GREATEREQUAL_STRING','ISEQUAL_STRING','NOTEQUAL_STRING'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	('right', 'UMINUS')
)

def p_program(p):
	"""
	program : declaration_list
	"""
	pass

def p_program_declaration_list(p):
	"""
	declaration_list : declaration_list declaration
	"""
	pass

def p_program_declaration(p):
	"""
	declaration_list : declaration
	"""
	pass

def p_declaration_import(p):
	"""
	declaration : USE ID SEMICOLON
                | PACKAGE ID SEMICOLON
	"""
	pass

def p_declaration_function(p):
	"""
	declaration : SUB ID LPAREN param_list RPAREN LBLOCK statement_list RBLOCK
	"""
	pass

def p_declaration_var(p):
	"""
	declaration : MY var_type SEMICOLON
				| MY var_type assign_type expression SEMICOLON
				| MY LPAREN param_list RPAREN SEMICOLON
				| MY LPAREN param_list RPAREN assign_type expression SEMICOLON
	"""
	pass

def p_param_list(p):
	"""
	param_list : var_type comma_var_type
			   | empty
	"""
	pass

def p_comma_var_type(p):
	"""
	comma_var_type : comma_var_type COMMA var_type
				   | COMMA var_type
				   | empty
	"""

def p_var_type(p):
	"""
	var_type : DOLLAR ID
			 | AT ID
			 | PERCENT ID
	"""
	pass

def p_assign_type(p):
	"""
	assign_type : ASSIGN
                | PLUS_ASSIGN
                | MINUS_ASSIGN
				| MULTIPLY_ASSIGN
				| DIVIDE_ASSIGN
				| MOD_ASSIGN
				| POW_ASSIGN
	"""
	pass

def p_statement_list(p):
	"""
	statement_list : statement_list statement SEMICOLON
	"""
	pass

def p_statement_list_statement(p):
	"""
	statement_list : statement SEMICOLON
	"""
	pass

def p_statement_list_empty(p):
	"""
	statement_list : empty
	"""
	pass

def p_statement_if(p):
	"""
	statement : IF LPAREN relop RPAREN LBLOCK statement_list RBLOCK
	"""
	pass

def p_statement_if_else(p):
	"""
	statement : IF LPAREN relop RPAREN LBLOCK statement_list RBLOCK ELSE LBLOCK statement_list RBLOCK
	"""
	pass

def p_statement_print(p):
	"""
	statement : PRINT STRING
	"""
	pass

def p_statement_while(p):
	"""
	statement : WHILE LPAREN relop RPAREN LBLOCK statement_list RBLOCK
	"""
	pass

def p_expression_list(p):
	"""
	expression_list : expression_listitems comma_expression
	"""
	pass

def p_expression_list_comma_expression(p):
	"""
	expression_list : comma_expression
	"""
	pass

def p_expression_list_empty(p):
	"""
	expression_list : empty
	"""
	pass

def p_expression_listitems(p):
	"""
	expression_listitems : expression_listitems comma_expression
	"""
	pass

def p_expression_listitems_expr(p):
	"""
	expression_listitems : expression
	"""
	pass

def p_comma_expression(p):
	"""
	comma_expression : COMMA expression
	"""
	pass

def p_expression(p):
	"""
	expression : expression PLUS expression
			   | expression MINUS expression
			   | expression TIMES expression
			   | expression DIVIDE expression
			   | expression MODULUS expression
	"""
	pass

def p_datatype_expression(p):
	"""
	expression : INTEGER
			   | HEX
			   | FLOAT
			   | STRING
	"""
	pass

def p_on_paren_expression(p):
	"""
	expression : LPAREN expression RPAREN
	"""
	pass

def p_call_expression(p):
	"""
	expression : ID LPAREN expression_list RPAREN %prec UMINUS
	"""

def p_var_type_expression(p):
	"""
	expression : var_type
	"""

def p_expression_uminus_minus(p):
	"""
	expression : MINUS expression %prec UMINUS
	"""
	pass

def p_expression_uminus_plus(p):
	"""
	expression : PLUS expression %prec UMINUS
	"""
	pass

def p_relop(p):
	"""
	relop : relop_number
			|	relop_string
	"""
	pass

def p_relop_number(p):
	"""
	relop_number :	ISEQUAL
				|	NOTEQUAL
				|	GREATER
				|	GREATEREQUAL
				|	LESS
				|	LESSEQUAL
				|	COMP
	"""
	pass

def p_relop_string(p):
	"""
	relop_string :	ISEQUAL_STRING
				|	NOTEQUAL_STRING
				|	GREATER_STRING
				|	GREATEREQUAL_STRING
				|	LESS_STRING
				|	LESSEQUAL_STRING
				|	COMP_STRING
	"""
	pass

def p_empty(p):
	'empty :'
	pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':
    if(len(sys.argv)>1):
        source = sys.argv[1]
    else:
        source = 'test.gr'

    f = open(source, 'r')
    data = f.read()
    print(data)
    parser.parse(data,tracking=True)
    print("Tu parser reconoció correctamente todo")

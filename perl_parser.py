import ply.yacc as yacc
from perl_lexer import tokens
import perl_lexer
import sys

VERBOSE = 1

def p_program(p):
	'program : declaration_list'
	pass

def p_declaration_list_1(p):
	'declaration_list : declaration_list  declaration'
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	pass

def p_declaration(p):
	'''declaration : var_declaration
				  | fun_declaration
                  | import'''
	pass

def p_import(p):
    '''import : USE ID SEMICOLON
                | PACKAGE ID SEMICOLON'''
    pass

'''
    Las declaraciones pueden ser:
    my $var;
    my $var = 5;
    my($var);
    my($var)=5;
    my($var1,$var2);
    my($var1,$var2) = (1,2)
    my($var1,$var2) = ID(32)
    my($var1,$var2) = ID(32,13,1231)

'''

def p_var_declaration(p):
	'''var_declaration : MY var_type SEMICOLON
						| MY var_type assign_type data_type SEMICOLON
						| MY var_type assign_type array_items SEMICOLON
						| MY var_type assign_type hash_items SEMICOLON
						| MY LPAREN var_type RPAREN SEMICOLON
						| MY LPAREN var_type RPAREN assign_type data_type SEMICOLON
						| MY LPAREN var_type RPAREN assign_type array_items SEMICOLON
						| MY LPAREN var_type RPAREN assign_type hash_items SEMICOLON
                        | MY LPAREN param_list RPAREN SEMICOLON
						| MY LPAREN param_list RPAREN assign_type data_type SEMICOLON
						| MY LPAREN param_list RPAREN assign_type array_items SEMICOLON
						| MY LPAREN param_list RPAREN assign_type hash_items SEMICOLON'''
	pass

def p_var_type(p):
    '''var_type : DOLLAR ID
                | AT ID
                | PERCENT ID'''
    pass

def p_assign_type(p):
    '''assign_type : ASSIGN
                | PLUS_ASSIGN
                | MINUS_ASSIGN
				| MULTIPLY_ASSIGN
				| DIVIDE_ASSIGN
				| MOD_ASSIGN
				| POW_ASSIGN'''
    pass

def p_data_type(p):
	'''data_type : 	INTEGER
				|	HEX
				|	FLOAT
				|	STRING'''
	pass

def p_array_items(p):
	'''array_items :	LPAREN param_list RPAREN'''
	pass

def p_hash_items(p):
	'''hash_items :		LPAREN hash_list RPAREN'''
	pass

def p_fun_declaration(p):
	'fun_declaration : SUB ID LPAREN params RPAREN compount_stmt'
	pass

def p_params_1(p):
	'params : param_list'
	pass

def p_params_2(p):
	'params : VOID'
	pass

def p_param_list_1(p):
	'param_list : param_list COMMA param'
	pass

def p_param_list_2(p):
	'param_list : param'
	pass

def p_hash_list_1(p):
	'hash_list : hash_list GROSSARROW param'
	pass

def p_hash_list_2(p):
	'hash_list : param'
	pass

def p_param_1(p):
	'param : datatype'
	pass

def p_param_2(p):
	'param : var_type'
	pass

def p_param_3(p):
	'param : ID LBRACKET INTEGER RBRACKET'
	pass



def p_compount_stmt(p):
	'compount_stmt : LBLOCK local_declarations statement_list RBLOCK'
	pass

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	pass

def p_local_declarations_2(p):
	'local_declarations : empty'
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : empty'
	pass

def p_statement(p):
	'''statement : expression_stmt
				| compount_stmt
				| selection_stmt
				| iteration_stmt
				| return_stmt
	'''
	pass

def p_expression_stmt_1(p):
	'expression_stmt : expression SEMICOLON'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : SEMICOLON'
	pass

def p_selection_stmt_1(p):
	'selection_stmt : IF LPAREN expression RPAREN statement'
	pass

def p_selection_stmt_2(p):
	'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'
	pass

def p_selection_stmt_3(p):
	'selection_stmt : SWITCH LPAREN var RPAREN statement'
	pass

def p_selection_stmt_4(p):
	'selection_stmt : CASE NUMBER COLON statement BREAK SEMICOLON'
	pass

def p_selection_stmt_5(p):
	'selection_stmt : DEFAULT COLON statement BREAK SEMICOLON'
	pass

def p_iteration_stmt_1(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN statement'
	pass



def p_iteration_stmt_2(p):
	'iteration_stmt : FOR LPAREN var_declaration2 SEMICOLON expression SEMICOLON additive_expression RPAREN statement'
	pass

def p_return_stmt_1(p):
	'return_stmt : RETURN SEMICOLON'
	pass

def p_return_stmt_2(p):
	'return_stmt : RETURN expression SEMICOLON'
	pass

def p_expression_1(p):
	'expression : var EQUAL expression'
	pass

def p_expression_2(p):
	'expression : simple_expression'
	pass

def p_expression_3(p):
	'expression : var EQUAL AMPERSANT ID'
	pass

def p_var_1(p):
	'var : ID'
	pass

def p_var_2(p):
	'var : ID LBRACKET expression RBRACKET'
	pass

def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass


def p_relop(p):
	'''relop : LESS
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| DEQUAL
			| DISTINT
			| ISEQUAL
	'''
	pass

def p_additive_expression_1(p):
	'''additive_expression : additive_expression addop term

        '''
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass

def p_additive_expression_3(p):
	'additive_expression : term MINUSMINUS'
	pass

def p_additive_expression_4(p):
	'additive_expression : term PLUSPLUS'
	pass

def p_addop(p):
	'''addop : PLUS
			| MINUS
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass



def p_mulop(p):
	'''mulop : 	TIMES
				| DIVIDE
	'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	pass

def p_factor_2(p):
	'factor : var'
	pass

def p_factor_3(p):
	'factor : call'
	pass

def p_factor_4(p):
	'factor : NUMBER'
	pass



def p_call(p):
	'call : ID LPAREN args RPAREN'
	pass

def p_args(p):
	'''args : args_list
			| empty
	'''
	pass

def p_args_list_1(p):
	'args_list : args_list COMMA expression'
	pass

def p_args_list_2(p):
	'args_list : expression'
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

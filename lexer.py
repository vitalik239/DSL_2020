from enum import Enum

class LexemType(Enum):
	COMMA = 0
	SEMICOLON = 1
	SHARP = 2

	ROUND_BRACKET_OPEN = 60
	ROUND_BRACKET_CLOSE = 61
	FIGURE_BRACKET_OPEN = 62
	FIGURE_BRACKET_CLOSE = 63
	TRIANGLE_BRACKET_OPEN = 64
	TRIANGLE_BRACKET_CLOSE = 65

	QUOTE = 8

	FOR = 10
	IF = 11
	WHILE = 12
	
	INT = 20
	DOUBLE = 21
	VOID = 22
	CHAR = 23

	PLUS = 31
	MINUS = 32
	MULTIPLICATION = 33
	DIVISION = 34
	AND = 35
	OR = 36
	EQUAL = 37

	ASSIGN = 70
	ASSIGN_ADD = 71
	ASSIGN_SUBS = 72
	ASSIGN_MULT = 73

	VARIABLE = 40
	NUMBER = 41
	FUNC_CALL = 42

	INCLUDE = 50

	OTHER = 100

symbols = ['+', '=', '-', '*', '&', '|', '<', '>']

separators = {
				'(' : LexemType.ROUND_BRACKET_OPEN, 
				')' : LexemType.ROUND_BRACKET_CLOSE, 
				'{' : LexemType.FIGURE_BRACKET_OPEN,
				'}' : LexemType.FIGURE_BRACKET_CLOSE,
				';' : LexemType.SEMICOLON,
				',' : LexemType.COMMA,
				'#' : LexemType.SHARP,
				'<' : LexemType.TRIANGLE_BRACKET_OPEN,
				'>' : LexemType.TRIANGLE_BRACKET_CLOSE,
				'\"' : LexemType.QUOTE
			 }

keywords = {
			'for' : LexemType.FOR,
			'while' : LexemType.WHILE,
			'if' : LexemType.IF,
			'include' : LexemType.INCLUDE
			}

operators = {
			'+' : LexemType.PLUS,
			'==' : LexemType.EQUAL,
			'-' : LexemType.MINUS,
			'*' : LexemType.MULTIPLICATION,
			'&&' : LexemType.AND,
			'||' : LexemType.OR
			}

assign = {
		'=' : LexemType.ASSIGN,
		'+=' : LexemType.ASSIGN_ADD,
		'-=' : LexemType.ASSIGN_SUBS,
		'*=' : LexemType.ASSIGN_MULT
		}

types = {
		'int' : LexemType.INT,
		'char' : LexemType.CHAR,
		'double' : LexemType.DOUBLE,
		'void' : LexemType.VOID
		}

lexem_dict = dict(keywords)
lexem_dict.update(types) 
lexem_dict.update(assign) 
lexem_dict.update(operators)
lexem_dict.update(keywords)
lexem_dict.update(separators)

tokens = []
cur = ''

def is_variable(c):
	return c.isdigit() or c.isalpha() or c == '_' 

def close_lexem():
	global cur
	if len(cur) > 0:
		if cur in lexem_dict:
			tokens.append((cur, lexem_dict[cur]))	
		elif cur.isdigit():
			tokens.append(([cur, LexemType.NUMBER]))
		else:
			tokens.append(([cur, LexemType.OTHER]))
	cur = ''

def lexer(line):
	global cur
	global tokens

	cur = ''
	tokens = []
	for c in line:
		if c.isspace():
			close_lexem()
		elif is_variable(c):
			if len(cur) > 0 and not is_variable(cur[-1]):
				close_lexem()
			cur += c
		elif c in symbols:
			if len(cur) > 0 and not cur[-1] in symbols:
				close_lexem()
			cur += c
		else:
			close_lexem()
			cur += c
	
	close_lexem()
	return tokens

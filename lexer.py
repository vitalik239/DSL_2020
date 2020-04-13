from enum import Enum

class LexemType(Enum):
	COMMA = 0
	SEMICOLON = 1
	ASSIGN = 2
	SHARP = 3

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

	PLUS = 31
	MINUS = 32
	MULTIPLICATION = 33
	DIVISION = 34
	AND = 35
	OR = 36
	EQUAL = 37

	VARIABLE = 40
	NUMBER = 41
	FUNC_CALL = 42

	INCLUDE = 50

	OTHER = 100

separators = {'(' : LexemType.ROUND_BRACKET_OPEN, 
				')' : LexemType.ROUND_BRACKET_CLOSE, 
				'{' : LexemType.FIGURE_BRACKET_OPEN,
				'}' : LexemType.FIGURE_BRACKET_CLOSE,
				';' : LexemType.SEMICOLON,
				',' : LexemType.COMMA,
				'#' : LexemType.SHARP,
				'<' : LexemType.TRIANGLE_BRACKET_OPEN,
				'>' : LexemType.TRIANGLE_BRACKET_CLOSE,
				'\"' : LexemType.QUOTE}

keywords = {'for' : LexemType.FOR,
			'while' : LexemType.WHILE,
			'if' : LexemType.IF,
			'include' : LexemType.INCLUDE}

def lexer(line):
	tokens = []
	cur = ''
	for c in line:
		if c.isspace():
			if len(cur) > 0:
				tokens += tuple([cur, LexemType.VARIABLE])
			cur = ''
		elif c.isalpha() or c.isdigit() or c == '_':
			cur += c
		elif c in separators:
			if len(cur) > 0:
				if cur in keywords:
					tokens += tuple([cur, keywords[cur]])
				elif cur.isdigit():
					tokens += tuple([cur, LexemType.NUMBER])
				else:
					tokens += tuple([cur, LexemType.VARIABLE])
			cur = ''
			tokens += tuple([c, separators[c]])
		else:
			tokens += tuple([c, LexemType.OTHER])
			cur = ''

	return tokens

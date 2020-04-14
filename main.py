from lexer import lexer
from parser import parse
from formatter import format

def load_cpp(file_name):
	tokens = []
	with open(file_name, "r") as file:
		for line in file:
			tokens += lexer(line)
			print(line)
			for t in lexer(line):
				print(t)
			print('_' * 20)

	return tokens 


def __main__():
	tokens = load_cpp("test/test1.cpp")
	root = parse(tokens)
	print(format(root)) 

__main__()
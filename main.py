from lexer import lexer
import formatter

def load_cpp(file_name):
	tokens = []
	with open(file_name, "r") as file:
		for line in file:
			tokens += lexer(line)
			print(line)
			print(lexer(line))
	return tokens 


def __main__():
	tokens = load_cpp("test/test1.cpp")


__main__()
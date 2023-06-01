from os import system, name

def system_clear():
	if name == 'posix':
		system('clear')
	else:
		system('cls')

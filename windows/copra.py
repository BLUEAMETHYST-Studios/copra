from sys import argv, exit
from colorama import init, Fore

init(autoreset=True)

if len(argv) < 2:
    print(f"{Fore.RED}[FAIL] Not enough arguments provided!")
    exit()

try:
    with open(argv[1]) as f:
        print(f"{Fore.WHITE}[INFO] Reading ...")
        file = f.read()
except FileNotFoundError:
    print(f"{Fore.RED}[FAIL] File not found!")
    exit()


stringInstance = ["Any", False]

class Lexer():
    def __init__(self, token):
        self.token = token
    def strLexer(self):
        if stringInstance == ["Any", False] and self.token == "'":
            stringInstance = ["'", True]
        elif stringInstance == ["Any", False] and self.token == '"':
            stringInstance = ['"', True]
        elif stringInstance == ["'", True] and self.token == "'":
            stringInstance = ["Any", False]
        elif stringInstance == ['"', True] and self.token == '"':
            stringInstance = ["Any", False]
        else:
            if stringInstance[1] == True:
                return True
            elif stringInstance[1] == False:
                return False
    def intLexer(self):
        if Lexer(self.token).strLexer() == True:
            return False
        else:
            return True
    def decLexer(self):
        if Lexer(self.token).intLexer() == True:
            ...
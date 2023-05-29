from sys import argv, exit, stdout
from colorama import init, Fore
from subprocess import run
from re import findall

init(autoreset=True)

if "-log" in argv[2:]:
    run(["_copra_log_.bat", argv[1], argv[argv.index("-log") + 1]])

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

filelength = len(file) # for performance

stringInstance = ["Any", False]
index = 0
strList = []
strListasStr = []

print(f"{Fore.WHITE}[INFO] Getting strings ...")
for char in file:
    if stringInstance[1] == True:
        if stringInstance[0] == char:
            ...
        else:
            strList.append(index)
            strListasStr[len(strListasStr) - 1] = f"{strListasStr[len(strListasStr) - 1]}{char}"
    if stringInstance[1] == False:
        if char == "'" or char == '"':
            stringInstance = [char, True]
            strListasStr.append("")
    elif stringInstance[1] == True:
        if char == "'" or char == '"':
            if char == stringInstance[0]:
                stringInstance = ["Any", False]
    index += 1

chars = []

print(f"{Fore.WHITE}[INFO] Preparing ...")
for c in file:
    chars.append(c)


fullchars = chars
charswithoutstr = chars
charsstr = ""

strList.sort(reverse=True)

for sl in strList:
    charswithoutstr.pop(sl)

for ch in chars:
    charsstr = charsstr + ch

print(f"{Fore.WHITE}[INFO] Compiling keywords ...")
charsreplaced = charsstr.replace("use", "import").replace("&&", "and").replace("::", "#").replace("!!", "not").replace("elseif", "elif").replace("fn", "def").replace("cl", "class").replace("it", "self").replace("kill", "exit()").replace("true", "True").replace("false", "False").replace("none", "None").replace("catch", "except")

print(f"{Fore.WHITE}[INFO] Compiling brackets ...")

indentation = 0

lines = charsreplaced.splitlines()

#for line in lines:
#    opening_brackets = len(findall(r'{', line))
#    closing_brackets = len(findall(r'}', line))
#
#    indentation += opening_brackets
#    indentation -= closing_brackets
#    if indentation < 0:
#        print(f"{Fore.LIGHTRED_EX}[WARN] A not needed closing bracket was found.")
#
#    indentation = max(0, indentation)
#
#    charsreplaced = " " * (indentation * 4) + line

charsfinished = charsreplaced

print(f"{Fore.WHITE}[INFO] Finishing string compilation process ...")
charsfinished = charsfinished.replace("'", '"')

for string in strListasStr:
    if '"' in string:
        charsfinished = charsfinished.replace('""', f"'{string}'", 1)
    else:
        charsfinished = charsfinished.replace('""', f'"{string}"', 1)

print(f"{Fore.WHITE}[INFO] Writing to file ...")
with open("output.py", "w") as output:
    output.write(charsfinished)
    output.close()
    
print(f"{Fore.WHITE}[INFO] Compilation process {Fore.LIGHTGREEN_EX}COMPLETED{Fore.WHITE}!")
        



    
    


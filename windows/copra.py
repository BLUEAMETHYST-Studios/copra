from sys import argv, exit
from colorama import init, Fore

init(autoreset=True)

    
if "-o" in argv[2:]:
    try:
        filename = argv[argv.index("-o") + 1]
    except IndexError:
        print(f"{Fore.RED}[FAIL] No output filename (or path) provided.")
        exit()
else:
    filename = "output.py"
    print(f"{Fore.WHITE}[INFO] File name will be output.py, because no output file was set")

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


charsreplaced_lines = charsreplaced.splitlines()
charsfinished_lines = []
indentation = 0

for line in charsreplaced_lines:
    stripped_line = line.strip()
    
    if stripped_line == "}":
        indentation -= 1
        if indentation < 0:
            # print(f"{Fore.LIGHTRED_EX}[WARN] A not needed closing bracket was found.") ( bugged right now :-( )
            indentation = 0
        continue
    
    indented_line = " " * (indentation * 4) + stripped_line
    
    if stripped_line == "{":
        indentation += 1

    charsfinished_lines.append(indented_line)
    
charsfinished = "\n".join(charsfinished_lines)

charsfinished = charsreplaced

charsfinished = charsfinished.replace("}", "").replace("{", "")

print(f"{Fore.WHITE}[INFO] Finishing string compilation process ...")
charsfinished = charsfinished.replace("'", '"')

for string in strListasStr:
    if '"' in string:
        charsfinished = charsfinished.replace('""', f"'{string}'", 1)
    else:
        charsfinished = charsfinished.replace('""', f'"{string}"', 1)

print(f"{Fore.WHITE}[INFO] Removing empty lines ...")

charsfinishedlines = charsfinished.splitlines()

index = 0

for line in charsfinishedlines:
    if line.isspace() or line == "":
        charsfinishedlines.pop(index)
    index += 1

charsfinished = ""

for finalline in charsfinishedlines:
    finalline = finalline + "\n"
    charsfinished = charsfinished + finalline

print(f"{Fore.WHITE}[INFO] Writing to file ...")

try:
    with open(f"{filename}", "w") as output:
        output.write(charsfinished)
        output.close()
except FileExistsError:
    print(f"{Fore.RED}[FAIL] File with name {filename}")
    
print(f"{Fore.WHITE}[INFO] Compilation process {Fore.LIGHTGREEN_EX}COMPLETED{Fore.WHITE}!")
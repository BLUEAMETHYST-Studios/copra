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

charsreplaced = charsstr
tempstr = charsstr

for multitoken in tempstr.split(" "):
    if not "$" in multitoken:
        if "use" in multitoken:
            tempstr = tempstr.replace("use", "import", 1)
        elif multitoken == "!!":
            tempstr = tempstr.replace("!!", "not", 1)
        elif multitoken == "&&":
            tempstr = tempstr.replace("&&", "and", 1)
        elif multitoken.startswith("::"):
            tempstr = tempstr.replace("::", "#", 1)
        elif "elseif" in multitoken:
            tempstr = tempstr.replace("elseif", "elif", 1)
        elif "fn" in multitoken:
            tempstr = tempstr.replace("fn", "def", 1)
        elif "cl" in multitoken:
            tempstr = tempstr.replace("cl", "class", 1)
        elif multitoken.startswith("it"):
            tempstr = tempstr.replace("it", "self", 1)
        elif "kill" in multitoken:
            tempstr = tempstr.replace("kill", "exit()", 1)
        elif "true" in multitoken:
            tempstr = tempstr.replace("true", "True", 1)
        elif "false" in multitoken:
            tempstr = tempstr.replace("false", "False", 1)
        elif "none" in multitoken:
            tempstr = tempstr.replace("none", "None", 1)
        elif "catch" in multitoken:
            tempstr = tempstr.replace("catch", "except", 1)
    else:
        tempstr = tempstr.replace("$", "var_")

charsreplaced = tempstr

print(f"{Fore.WHITE}[INFO] Compiling brackets ...")

charsreplaced_lines = charsreplaced.splitlines()
fully_replaced = []
fully_replaced_str = ""
indentation = ""

def indentationcheck(line):
    if "{" and "}" in line:
        print(f"{Fore.LIGHTRED_EX}[WARN] Multiple brackets in one line can cause issues!")
    if "{" in line:
        return True
    elif "}" in line:
        return True
    else:
        return None

for line in charsreplaced_lines.strip():
    check = indentationcheck(line=line)
    if check == True:
        indentation = indentation + "    "
    elif check == False:
        indentation = indentation.replace("    ", "", 1)
    else:
        ...
    print("a" + indentation + "b")
    fully_replaced.append(indentation + line)
    
for l in fully_replaced:
    fully_replaced_str = fully_replaced_str + l + "\n"

charsfinished = fully_replaced_str.replace("}", "").replace("{", "")

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
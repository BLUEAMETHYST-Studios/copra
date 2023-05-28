from sys import argv, exit, stdout
from colorama import init, Fore
from subprocess import run

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

stringInstance = ["Any", False]
index = 0
strList = []

for char in file:
    print(f"{Fore.WHITE}[INFO] Checking character {index + 1}")
    if stringInstance[1] == True:
        if stringInstance[0] == char:
            ...
        else:
            strList.append(index)
    if stringInstance[1] == False:
        if char == "'" or char == '"':
            stringInstance = [char, True]
    elif stringInstance[1] == True:
        if char == "'" or char == '"':
            if char == stringInstance[0]:
                stringInstance = ["Any", False]
                print(f"{Fore.WHITE}[INFO] End of string in char {index + 1}")
            else:
                print(f"{Fore.WHITE}[INFO] {char} isn't ending string due to the string start being {stringInstance[0]}")    
    index += 1

chars = []
progressnum = 1

for c in file:
    print(f"{Fore.WHITE}[INFO] Preparing: {progressnum}/{len(file)}")
    chars.append(c)
    progressnum += 1

progressnum = 1

strList.sort(reverse=True)



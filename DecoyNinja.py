import random; import os; import time
import msvcrt
from colorama import init
from termcolor import colored

loopFlagExp = 0; loopFlagAssign = 0
expNum = 1; assignNum = 1

init()

print(colored('''
                    ▓█████▄ ▓█████  ▄████▄   ▒█████ ▓██   ██▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
                    ▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒▒██  ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
                    ░██   █▌▒███   ▒▓█    ▄ ▒██░  ██▒ ▒██ ██░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
                    ░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░ ░ ▐██▓░▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
                    ░▒████▓ ░▒████▒▒ ▓███▀ ░░ ████▓▒░ ░ ██▒▓░▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
                     ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░   ██▒▒▒ ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
                     ░ ▒  ▒  ░ ░  ░  ░  ▒     ░ ▒ ▒░ ▓██ ░▒░ ░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
                     ░ ░  ░    ░   ░        ░ ░ ░ ▒  ▒ ▒ ░░     ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
                       ░       ░  ░░ ░          ░ ░  ░ ░              ░  ░           ░  ░   ░        ░  ░
                     ░             ░                 ░ ░                                                 ''', 'blue'))
print(colored('''                                               DecoyNinja: The Decoy Generator''', 'red'))
print(colored('''                                         -------------------------------------------''', 'blue'))


exp = int(input("How many experiments to decoy?: "))
assign = int(input("How many assignments to decoy?: "))
Output = str(input("Enter output folder (Default = current folder):") or "./")
Output += "/"
OutputCopy = Output

start = time.time()

while (loopFlagExp < exp):
    Output += "Experiment (%d).pdf" % expNum
    if (exp != 0):
        with open(Output, '+w') as file:
            randmFill = random.randint(500000,1000000)
            choices = ['å','¼','Ü','€','´','W','','„','','ñ','”','Ó','l','D','/','‘','N','œ','¦',
                     'l','ž','£',']','ß','6','T','1','Š','ï','','õ','F','N','‰','Î','&',';','?','#','^','q',
                     '%',' ','~',':','k','2','±','¼','▐',' ','X','r','0','m','*','(','@','$','?','7','.','j','+',',']
            for i in range(0, randmFill):
                file.write(random.choice(choices))
        file.close()
        loopFlagExp += 1
        expNum += 1
        Output = OutputCopy
    else:
        break

while (loopFlagAssign < assign):
    Output += "Assignment (%d).pdf" % assignNum
    if (assign != 0):
        with open(Output, '+w') as file:
            randmFill = random.randint(600000, 1000000)
            choices = ['%',' ','[','~',':','k','0','2','±','¼','h',' ','-','Q','_','','u','.','3','L','f','╣',
                     'å','█','Ü','€','´',' ','i','ž','£',']','ß','6','T','1','Š','ï',' ','õ','m','o','‰',
                     'P','','ñ','”','Ó','l','ð','/','‘','N','œ','¦','Î','&',';','?','#','^','q','—']
            for i in range(0, randmFill):
                file.write(random.choice(choices))
        file.close()
        loopFlagAssign += 1
        assignNum += 1
        Output = OutputCopy
    else:
        break

completionTime = time.time() - start

print("\nThe task completed successfully in %f seconds." % completionTime)
print("Press any key to exit. GG;WP.")
secret = input()
os.sys.exit()

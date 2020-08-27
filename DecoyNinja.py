import random; import os; import time
from colorama import init
from termcolor import colored
import threading

loopFlagExp = 0; loopFlagAssign = 0
expNum = 1; assignNum = 1; assign = 0; exp = 0
decisionMade = False

BANNER1 = colored('''
                    ▓█████▄ ▓█████  ▄████▄   ▒█████ ▓██   ██▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
                    ▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒▒██  ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
                    ░██   █▌▒███   ▒▓█    ▄ ▒██░  ██▒ ▒██ ██░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
                    ░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░ ░ ▐██▓░▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
                    ░▒████▓ ░▒████▒▒ ▓███▀ ░░ ████▓▒░ ░ ██▒▓░▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
                     ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░   ██▒▒▒ ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
                     ░ ▒  ▒  ░ ░  ░  ░  ▒     ░ ▒ ▒░ ▓██ ░▒░ ░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
                     ░ ░  ░    ░   ░        ░ ░ ░ ▒  ▒ ▒ ░░     ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
                       ░       ░  ░░ ░          ░ ░  ░ ░              ░  ░           ░  ░   ░        ░  ░
                     ░             ░                 ░ ░                                                 ''', 'blue')
BANNER2 = colored('''                                               DecoyNinja: The Decoy Generator''', 'red')
BANNER3 = colored('''                                         -------------------------------------------''', 'blue')


def printBanner():
    init()
    print(BANNER1), print(BANNER2), print(BANNER3)


def generateExps(Output, loopFlagExp, expNum):
    while (loopFlagExp < exp):
        Output += f"Experiment {expNum}.pdf"
        if (exp != 0):
            with open(Output, "w") as file:
                randmFill = random.randint(500000, 1000000)
                choices = ['å', '¼', 'Ü', '€', '´', 'W', '', '„', ' ', 'ñ', '”', 'Ó', 'l', 'D', '/', '‘', 'N', 'œ',
                           '¦', 'l', 'ž', '£', ']', 'ß', '6', 'T', '1', 'Š', 'ï', '', 'õ', 'F', 'N', '‰', 'Î', '&', ';',
                           '?', '#', '^', 'q', '%', ' ', '~', ':', 'k', '2', '±', '¼', 'l', ' ', 'X', 'r', '0', 'm', '*',
                           '(', '@', '$', '?', '7', '.', 'j', '+', ',']
                for i in range(0, randmFill):
                    file.write(random.choice(choices))
            loopFlagExp += 1
            expNum += 1
            Output = OutputCopy
        else:
            break


def generateAssigns(Output, loopFlagAssign, assignNum):
    while (loopFlagAssign < assign):
        Output += f"Assignment {assignNum}.pdf"
        if (assign != 0):
            with open(Output, "w") as file:
                randmFill = random.randint(600000, 1000000)
                choices = ['%', ' ', '[', '~', ':', 'k', '0', '2', '±', '¼', 'h', ' ', '-', 'Q', '_', '', 'u', '.',
                           '3', 'L', 'f', '', 'å', 'j', 'Ü', '€', '´', ' ', 'i', 'ž', '£', ']', 'ß', '6', 'T', '1',
                           'Š', 'ï', ' ', 'õ', 'm', 'o', '‰', 'P', '', 'ñ', '”', 'Ó', 'l', 'ð', ' ', '‘', 'N', 'œ',
                           '¦', 'Î', '&', ';', '?', '#', '^', 'q', '—']
                for i in range(0, randmFill):
                    file.write(random.choice(choices))
            loopFlagAssign += 1
            assignNum += 1
            Output = OutputCopy
        else:
            break


########## Main ##########

if __name__ == "__main__":

    printBanner()

    while (decisionMade is False):
        try:
            assign = int(input("Enter the number of assignments to decoy (Default = 1): ") or 1)
            exp = int(input("Enter the number of experiments to decoy (Default = 1): ") or 1)
            decisionMade = True
        except:
            assign = 0
            exp = 0
            print("\nInvalid entry. Enter an integer. Try again.\n")
            continue

    Output = str(input("Enter output folder (Default = current folder):") or "./")
    Output += "/"
    OutputCopy = Output

    threadExps = threading.Thread(target=generateExps, args=[Output, loopFlagExp, expNum])
    threadAssigns = threading.Thread(target=generateAssigns, args=[Output, loopFlagAssign, assignNum])

    print("\nWorking...", end='')

    start = time.time()

    threadExps.start()
    threadAssigns.start()

    threadExps.join()
    threadAssigns.join()

    completionTime = time.time() - start

    print(f"\n\nThe task completed successfully in {completionTime} seconds.")
    print("Press any key to exit. GG;WP.")
    input()

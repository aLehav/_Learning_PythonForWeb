from secrets import randbelow
from colorama import Fore, Back, Style
import requests
print("How much money do you have to spend?")
wallet = float(input())
print("How many activities do you have time for?")
time = int(input())
print("Here's some things to do if you're bored:")
exList = []
exList.append(Fore.RED)
exList.append(Fore.YELLOW)
exList.append(Fore.GREEN)
exList.append(Fore.CYAN)
exList.append(Fore.BLUE)
exList.append(Fore.MAGENTA)
y = randbelow(len(exList))
while wallet >= 0 and time >= 0:
    r = requests.get("https://www.boredapi.com/api/activity/")
    rj = r.json()
    wallet -= rj["price"]*rj["participants"]
    wallet = round(wallet, 4)
    time -= 1
    if wallet >= 0 and time >= 0:
        print(exList[y] + rj["activity"] + "    " + Fore.WHITE + "Time: " + str(time) + "  Wallet: " + str(wallet))
    y = y + 1
    if y >= len(exList):
        y = 0
print(Style.RESET_ALL)

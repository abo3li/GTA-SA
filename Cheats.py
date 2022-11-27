import pyautogui
import time

def prs(s):
    time.sleep(3)
    pyautogui.press(list(s))

Done = True
while Done:
    print("""
    Cheats Menue:

    ---- Health ----
    1- Start Point.
    2- Full armar.
    3- Infinty blood.
    4- No Police.

    ---- Weapens ---- 
    5- Class A.
    6- Class B.
    7 Class C.
    8- Infinty Amo.

    ---- Others ----
    9- Jet.
    10- Tank.
    11- Most wanted.
    12- JetPack.
    13- Maximum Respect.
    14- 69.
    15- all cares nitrous.
    16- Sport Cars.
    17- always midnight.
    18- Always 21:00.
    19- Cloudy Weather.
    20- very sunny weather.
    21- Recruit Anyone (Rocket Launcher).
    22- Increase Car Speed.
    
    --- Press X to Exit -- 
    
    """)

    ch = input('')

    if ch == "x" or ch == "X":
        Done = False 

    if ch == "1":
        prs("HESOYAM")
        prs("BAGUVIX")
        prs("AEZAKMI")
        # prs("PROFESSIONALSKIT")
        prs("UZUMYMW")
        prs("FULLCLIP")


    if ch == "2":
        prs("HESOYAM")

    if ch == "3":
        prs("BAGUVIX")

    if ch == "4":
        prs("AEZAKMI")

    if ch == "5":
        prs("LXGIWYL")

    if ch == "6":
        prs("PROFESSIONALSKIT")

    if ch == "7":
        prs("UZUMYMW")

    if ch == "8":
        prs("FULLCLIP")

    if ch == "9":
        prs("JUMPJET")

    if ch == "10":
        prs("WPRTON")

    if ch == "11":
        prs("BRINGITON")

    if ch == "12":
        prs("ROCKETMAN")

    if ch == "13":
        prs("WORSHIPME")

    if ch == "14":
        prs("HELLOLADIES")

    if ch == "15":
        prs("SPEEDFREAK")

    if ch == "16":
        prs("EVERYONEISRICH")

    if ch == "17":
        prs("NIGHTPROWLER")

    if ch == "18":
        prs("OFVIAC")

    if ch == "19":
        prs("ALNSFMZO")

    if ch == "20":
        prs("ICIKPYH")

    if ch == "21":
        prs("ZSOXFSQ")

    if ch == "22":
        prs("LPNQMAS")

    # if ch == "s" or ch == "S":
    #     s = input("Enter series seprated by comma , : ")
    #     s.split(',')
    #     print("this is s ---> "+s)
    #     for n in s:
    #         prs(n)
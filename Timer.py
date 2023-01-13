#  This is a cooking timer for Sea of Thieves
# the text to speach is from https://wideo.co/text-to-speech/
#
# fish = 30sec undercook, 40s cooked, 80s burn
# trophy fish 80s undercook, 90s cooked, 180s burn
# meat 50s undercook, 60s cook, 120s burn
# Kraken and Meg 100s undercook, 120s cook, 240s burn

import tkinter as tk
from Fish import *
from Vails import *
from playsound import playsound
from findSeaPort import findPort

version = "0.13 (VailPatch)"
buildDate = "1/13/2023"
recycleSave = []
fishTime = 0
fishBurnTime = 0
trophyTime = 0
trophyBurnTime = 0
meatTime = 0
meatBurnTime = 0
krakenTime = 0
krakenBurnTime = 0
cookingFish = False
cookingTrophy = False
cookingMeat = False
cookingKraken = False
fishStatus = " "
trophyStatus = " "
meatStatus = " "
krakenStatus = " "


def vailHelp(main):
    vailWindow = tk.Toplevel(main)
    vailWindow.iconbitmap("fish.ico")
    sudd_button = tk.Button(vailWindow, text='Find Sudds', command=lambda: find_sudds(vailWindow, recycleSave))
    sudd_button.pack()

def howTo():
    how_window = tk.Toplevel(main)
    how_window.iconbitmap("fish.ico")
    #Time
    timerFrame = tk.Frame(how_window, pady=10)
    timerFrame.grid(row=0, column=0)
    howLabel = tk.Label(timerFrame, text="Timer (Tools Menu)")
    howLabel.config(bg="Black", fg="White")
    howLabel.pack()
    howLabel2 = tk.Label(timerFrame, bg="White", text=
    "You can have one timer going at a time, pressing any of the 4 buttons").pack()
    howLabel3 = tk.Label(timerFrame, bg="White", text=
    "will start the timer. Pressing a button while a timer is active, will stop it.").pack()
    # Fish
    fishFrame = tk.Frame(how_window, pady=15)
    fishFrame.grid(row=0, column=1)
    fishLabel = tk.Label(fishFrame, bg="Black", fg="White", text="Fish Information (Fish Menu)").pack()
    fishLabel2 = tk.Label(fishFrame, bg="White", text="Each fish type can be slected for infrmation about").pack()
    fishLabel3 = tk.Label(fishFrame, bg="White", text="where to catch and what bait to use or all fish menu").pack()
    fishLabel4 = tk.Label(fishFrame, padx=15, bg="White",
                          text="will list this information about all fish types.").pack()
    #Seaport
    seaportFrame = tk.Frame(how_window, pady=10)
    seaportFrame.grid(row=2, column=0)
    seaportLabel = tk.Label(seaportFrame, bg="Black", fg="White", text="How to use Seaport Finder (Tools Menu)").pack()
    seaportLabel2 = tk.Label(seaportFrame, bg="White", text="Enter what map square your in and a pop up will").pack()
    seaportLabel3 = tk.Label(seaportFrame, bg="White", text="tell you the closest seaport and it map square").pack()
    #Mondy
    moneyFrame = tk.Frame(how_window, pady=15)
    moneyFrame.grid(row=1, column=0)
    moneyLabel = tk.Label(moneyFrame, bg="Black", fg="White", text="Money Calculator (Tools Menu)").pack()
    moneyLabel2 = tk.Label(moneyFrame, bg="White", text="Enter how much gold you start your voyage with in 'Starting Gold'").pack()
    moneyLabel3 = tk.Label(moneyFrame, bg="White", text="Enter how much gold you end up with in 'Ending Gold'").pack()
    moneyLabel4 = tk.Label(moneyFrame, bg="White", text="Press 'Calculate' and see how much money you made!").pack()
    #Sound
    soundFrame = tk.Frame(how_window, pady=25)
    soundFrame.grid(row=1, column=1)
    soundLabel = tk.Label(soundFrame, bg="Black", fg="White", text="Sound Options (Options Menu)").pack()
    soundLabel2 = tk.Label(soundFrame, bg="White", text="In the Options menu you can turn audio alerts on or off.").pack()


def moneyUpdate(x, y):
    global moneyResult
    goldTemp = y-x
    goldTemp = "{:,}".format(goldTemp)
    moneyResult.set(goldTemp)


def moneyCalc():
    global moneyResult
    global Coin_image
    moneyResult = tk.IntVar()
    moneyResult.set(0)
    startGold = tk.IntVar()
    startGold.set(0)
    endGold = tk.IntVar()
    endGold.set(0)
    moneyResult.set(0)
    money_window = tk.Toplevel(main)
    money_window.iconbitmap("fish.ico")
    gold_start_label = tk.Label(money_window, text='Starting Gold:').grid(row=0, column=0)
    gold_start_entry = tk.Entry(money_window, textvariable=startGold).grid(row=0, column=1)
    gold_end_label = tk.Label(money_window, text='Ending Gold:').grid(row=1, column=0)
    gold_end_entry = tk.Entry(money_window, textvariable=endGold).grid(row=1, column=1)
    show_gold = tk.Label(money_window, textvariable=moneyResult)
    show_gold.grid(row=2, column=1)
    show_more_gold = tk.Label(money_window, text="Gold earned this run: ").grid(row=2, column=0)

    updateButton = tk.Button(money_window,
                             text="Calculate", image=Coin_image,
                             command=lambda: moneyUpdate(startGold.get(), endGold.get()))
    updateButton.grid(row=3, columnspan=2)


def showHelp():
    # global version

    help_window = tk.Toplevel(main)
    help_window.iconbitmap("fish.ico")
    version_label = tk.Label(help_window, text="SoT Cooking Timer Version: " + str(version))
    version_label.pack()
    date_label = tk.Label(help_window, text="Build Date: " + buildDate)
    date_label.pack()


def updateLabels():
    Fish_Label['text'] = str(fishTime)
    Fish_Burn_Label['text'] = str(fishBurnTime)
    Trophy_Label['text'] = str(trophyTime)
    Trophy_Burn_Label['text'] = str(trophyBurnTime)
    Meat_Label['text'] = str(meatTime)
    Meat_Burn_Label['text'] = str(meatBurnTime)
    Kraken_Label['text'] = str(meatTime)
    Kraken_Burn_Label['text'] = str(meatBurnTime)


def soundOn():
    sound.set(0)


def soundOff():
    sound.set(1)


def locatePort():
    vert = []
    hor = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    count = 0
    global Spyglass_image
    while len(vert) < 20:
        count += 1
        vert.append(str(count))
    portWindow = tk.Toplevel(main)
    portWindow.iconbitmap("fish.ico")
    vertVar = tk.StringVar()
    horVar = tk.StringVar()
    locationLabel = tk.Label(portWindow, text="Current location: ")
    locationLabel.grid(row=0, column=0)
    vertLocation = tk.OptionMenu(portWindow, vertVar, *vert).grid(row=0, column=1)
    horLocation = tk.OptionMenu(portWindow, horVar, *hor).grid(row=0, column=2)
    vertVar.set("1")
    horVar.set("A")
    findButton = tk.Button(portWindow, image=Spyglass_image, text="Find Seaport", command=lambda: findPort(vertVar.get(), horVar.get())).grid(row=1, columnspan=3)


def showMap():
    global worldMap
    secondWindow = tk.Toplevel(main)
    secondWindow.iconbitmap("fish.ico")
    secondLabel = tk.Canvas(secondWindow, width=800, height=700)
    wMap = secondLabel.create_image([400, 375], image=worldMap)
    secondLabel.grid(row=0, column=0)


def timer():
    global fishTime
    global fishStatus
    global cookingFish
    global trophyTime
    global cookingTrophy
    global trophyStatus
    global meatTime
    global meatStatus
    global cookingMeat
    global krakenTime
    global krakenStatus
    global cookingKraken

    if cookingFish:
        fishTime -= 1
        fishBurnTime = fishTime + 40
        Fish_Label.config(bg="Green")
        Fish_Label.config(fg="Yellow")
        if fishTime < 1:
            Fish_Label.config(bg="Red")
            Fish_Label.config(fg="Black")
            fishStatus = "Cooked"
            if fishTime == 0:
                if sound.get() == 0:
                    playsound('fish.mp3')
            if fishTime < -40:
                fishStatus = "Burned"
                Fish_Label.config(bg="Black")
                Fish_Label.config(fg="White")
            if fishTime < -300:
                cookingFish = False
                fishStatus = " "
                fishTime = 0
        Fish_Label['text'] = str(trophyTime)
        Fish_Burn_Label['text'] = str(fishBurnTime)
        if fishBurnTime < 1:
            cookingFish = False
            fishTime = 0
            fishBurnTime = 0
            Fish_Label.config(bg="Light Grey")
            Fish_Label.config(fg="Black")
            fishStatus = "Burned"
    if cookingTrophy:
        trophyTime -= 1
        trophyBurnTime = trophyTime + 90
        Trophy_Label.config(bg="Green")
        Trophy_Label.config(fg="Yellow")
        if trophyTime < 1:
            Trophy_Label.config(bg="Red")
            Trophy_Label.config(fg="Black")
            trophyStatus = "Cooked"
            if trophyTime == 0:
                if sound.get() == 0:
                    playsound('fish.mp3')
        if trophyTime < -119:
            trophyStatus = "Burning"
            Trophy_Label.config(bg="Black")
            Trophy_Label.config(fg="White")
        if trophyTime < -300:
            cookingTrophy = False
            trophyStatus = " "
            trophyTime = 0
        Trophy_Label['text'] = str(fishTime)
        Trophy_Burn_Label['text'] = str(trophyBurnTime)
        if trophyBurnTime < 1:
            cookingTrophy = False
            trophyTime = 0
            trophyBurnTime = 0
            Trophy_Label.config(bg="Light Grey")
            Trophy_Label.config(fg="Black")
            trophyStatus = "Burned"
    if cookingMeat:
        meatTime -= 1
        meatBurnTime = meatTime + 60
        Meat_Label.config(bg="Green")
        Meat_Label.config(fg="Yellow")
        if meatTime < 1:
            Meat_Label.config(bg="Red")
            Meat_Label.config(fg="Black")
            meatStatus = "Cooked"
            if meatTime == 0:
                if sound.get() == 0:
                    playsound('food.mp3')
        if meatTime < -60:
            meatStatus = "Burned"
            Meat_Label.config(bg="Black")
            Meat_Label.config(fg="White")
        if meatTime < -300:
            cookingMeat = False
            meatStatus = " "
            meatTime = 0
        Meat_Label['text'] = str(meatTime)
        Meat_Burn_Label['text'] = str(meatBurnTime)
        if meatBurnTime < 1:
            cookingMeat = False
            meatTime = 0
            meatBurnTime = 0
            Meat_Label.config(bg="Light Grey")
            Meat_Label.config(fg="Black")
            meatStatus = "Burned"
    if cookingKraken:
        krakenTime -= 1
        krakenBurnTime = krakenTime + 120
        Kraken_Label.config(bg="Green")
        Kraken_Label.config(fg="Yellow")
        if krakenTime < 1:
            Kraken_Label.config(bg="Red")
            Kraken_Label.config(fg="Black")
            krakenStatus = "Cooked"
            if krakenTime == 0:
                if sound.get() == 0:
                    playsound('food.mp3')
        if krakenTime < -120:
            krakenStatus = "Burned"
            Kraken_Label.config(bg="Black")
            Kraken_Label.config(fg="White")
        if krakenTime < -300:
            cookingKraken = False
            krakenStatus = " "
            krakenTime = 0
        Kraken_Label['text'] = str(krakenTime)
        Kraken_Burn_Label['text'] = str(krakenBurnTime)
        if krakenBurnTime < 1:
            cookingKraken = False
            krakenTime = 0
            krakenBurnTime = 0
            Kraken_Label.config(bg="Light Grey")
            Kraken_Label.config(fg="Black")
            krakenStatus = "Burned"

    Fish_Status_Label.config(text=fishStatus)
    Trophy_Status_Label.config(text=trophyStatus)
    Fish_Label['text'] = str(fishTime)
    Trophy_Label['text'] = str(trophyTime)
    Meat_Status_Label.config(text=meatStatus)
    Meat_Label['text'] = str(meatTime)
    Kraken_Status_Label.config(text=krakenStatus)
    Kraken_Label['text'] = str(krakenTime)

    main.after(1000, timer)


def setTimer(x):
    global fishTime
    global fishBurnTime
    global cookingFish
    global fishStatus
    global cookingTrophy
    global trophyTime
    global trophyStatus
    global meatTime
    global cookingMeat
    global meatStatus
    global krakenTime
    global krakenStatus
    global cookingKraken

    if x == "fish":
        if cookingFish == False:
            cookingFish = True
            cookingTrophy = False
            cookingMeat = False
            cookingKraken = False
            Fish_Label.config(bg="Green")
            Fish_Label.config(fg="Yellow")
            fishStatus = "Cooking"
            fishTime = 40
            trophyTime = 0
            trophyBurnTime = 0
            meatTime = 0
            krakenTime = 0
            Trophy_Label.config(bg="Light Grey")
            Trophy_Label.config(fg="Black")
            trophyStatus = " "
            Meat_Label.config(bg="Light Grey")
            Meat_Label.config(fg="Black")
            meatStatus = " "
            Kraken_Label.config(bg='Light Grey', fg='Black')
            krakenStatus = " "
        else:
            cookingFish = False
            Fish_Label.config(bg="Light Grey")
            Fish_Label.config(fg="Black")
            fishStatus = " "
            fishTime = 0
            fishBurnTime = 0
    elif x == 'trophy':
        if cookingTrophy == False:
            cookingTrophy = True
            cookingFish = False
            cookingMeat = False
            cookingKraken = False
            Trophy_Label.config(bg="Green")
            Trophy_Label.config(fg="Yellow")
            trophyStatus = "Cooking"
            trophyTime = 90
            fishTime = 0
            meatTime = 0
            krakenTime = 0
            Fish_Label.config(bg="Light Grey")
            Fish_Label.config(fg="Black")
            fishStatus = " "
            Meat_Label.config(bg="Light Grey")
            Meat_Label.config(fg="Black")
            meatStatus = " "
            Kraken_Label.config(bg='Light Grey', fg='Black')
            krakenStatus = " "
        else:
            cookingTrophy = False
            Trophy_Label.config(bg="Light Grey")
            Trophy_Label.config(fg="Black")
            trophyStatus = " "
            trophyTime = 0
            trophyBurnTime = 0
    elif x == 'meat':
        if cookingMeat == False:
            cookingMeat = True
            cookingTrophy = False
            cookingFish = False
            cookingKraken = False
            Meat_Label.config(bg="Green")
            Meat_Label.config(fg="Yellow")
            meatStatus = "Cooking"
            meatTime = 60
            trophyTime = 0
            fishTime = 0
            krakenTime = 0
            Fish_Label.config(bg="Light Grey")
            Fish_Label.config(fg="Black")
            fishStatus = " "
            Trophy_Label.config(bg="Light Grey")
            Trophy_Label.config(fg="Black")
            trophyStatus = " "
            Kraken_Label.config(bg='Light Grey', fg='Black')
            krakenStatus = " "
        else:
            cookingMeat = False
            Meat_Label.config(bg="Light Grey")
            Meat_Label.config(fg="Black")
            meatStatus = " "
            meatTime = 0
            meatBurnTime = 0
    elif x == 'kraken':
        if cookingKraken == False:
            cookingKraken = True
            cookingTrophy = False
            cookingFish = False
            cookingMeat = False
            Kraken_Label.config(bg="Green", fg="Yellow")
            krakenStatus = "Cooking"
            krakenTime = 120
            trophyTime = 0
            fishTime = 0
            meatTime = 0
            Fish_Label.config(bg="Light Grey")
            Fish_Label.config(fg="Black")
            fishStatus = " "
            Trophy_Label.config(bg="Light Grey")
            Trophy_Label.config(fg="Black")
            trophyStatus = " "
            Meat_Label.config(bg='Light Grey', fg='Black')
            meatStatus = " "
        else:
            cookingKraken = False
            Kraken_Label.config(bg="Light Grey")
            Kraken_Label.config(fg="Black")
            krakenStatus = " "
            krakenTime = 0
            krakenBurnTime = 0
    updateLabels()


main = tk.Tk()
main.title(f"SoT Cooking Timer {str(version)}")
main.iconbitmap("fish.ico")

worldMap = tk.PhotoImage(file="Map4.png")
fish_image = tk.PhotoImage(file="fish.png")
trophy_image = tk.PhotoImage(file="TrophyFish.png")
meat_image = tk.PhotoImage(file="meat.png")
kraken_image = tk.PhotoImage(file="LegendMeat.png")
Spyglass_image = tk.PhotoImage(file="Spyglass.png")
Coin_image = tk.PhotoImage(file="Coin.png")

Button_Label = tk.Label(main, text="Start / Stop Button")
Button_Label.config(bg="Black")
Button_Label.config(fg="White")
Button_Label.grid(row=0, column=0)
Cook_Timer_Label = tk.Label(main, text="Time till cooked")
Cook_Timer_Label.grid(row=0, column=1)
Burn_Timer_Label = tk.Label(main, text="Time till burned")
Burn_Timer_Label.config(bg="Black")
Burn_Timer_Label.config(fg="White")
Burn_Timer_Label.grid(row=0, column=2)
Food_Status_Label = tk.Label(main, text="Food Status")
Food_Status_Label.grid(row=0, column=3)

Fish_Button = tk.Button(main, image=fish_image, text="Fish", command=lambda: setTimer('fish'))
Fish_Button.grid(row=1, column=0)
Fish_Label = tk.Label(main, text=str(fishTime))
Fish_Label.config(bg="Light Grey", width=5, height=5)
Fish_Label.grid(row=1, column=1)
Fish_Status_Label = tk.Label(main, text=fishStatus)
Fish_Status_Label.grid(row=1, column=3)
Fish_Burn_Label = tk.Label(main, text=str(fishBurnTime))
Fish_Burn_Label.config(bg="Black", fg="White", width=5, height=5)
Fish_Burn_Label.grid(row=1, column=2)

Trophy_Button = tk.Button(main, image=trophy_image, text="Trophy Fish", command=lambda: setTimer('trophy'))
Trophy_Button.grid(row=2, column=0)
Trophy_Label = tk.Label(main, text=str(trophyTime))
Trophy_Label.config(bg="Light Grey", width=5, height=5)
Trophy_Label.grid(row=2, column=1)
Trophy_Status_Label = tk.Label(main, text=trophyStatus, width=8, height=8)
Trophy_Status_Label.grid(row=2, column=3)
Trophy_Burn_Label = tk.Label(main, text=str(trophyBurnTime))
Trophy_Burn_Label.config(bg="Black", fg="White", width=5, height=5)
Trophy_Burn_Label.grid(row=2, column=2)

Meat_Button = tk.Button(main, image=meat_image, text="Normal Meat", command=lambda: setTimer('meat'))
Meat_Button.grid(row=3, column=0)
Meat_Label = tk.Label(main, text=str(meatTime))
Meat_Label.config(bg="Light Grey", width=5, height=5)
Meat_Label.grid(row=3, column=1)
Meat_Status_Label = tk.Label(main, text=meatStatus, width=8, height=8)
Meat_Status_Label.grid(row=3, column=3)
Meat_Burn_Label = tk.Label(main, text=str(meatBurnTime))
Meat_Burn_Label.config(bg="Black", fg="White", width=5, height=5)
Meat_Burn_Label.grid(row=3, column=2)

Kraken_Button = tk.Button(main, image=kraken_image, text="Normal Meat", command=lambda: setTimer('kraken'))
Kraken_Button.grid(row=4, column=0)
Kraken_Label = tk.Label(main, text=str(meatTime))
Kraken_Label.config(bg="Light Grey", width=5, height=5)
Kraken_Label.grid(row=4, column=1)
Kraken_Status_Label = tk.Label(main, text=meatStatus, width=8, height=8)
Kraken_Status_Label.grid(row=4, column=3)
Kraken_Burn_Label = tk.Label(main, text=str(krakenBurnTime))
Kraken_Burn_Label.config(bg="Black", fg="White", width=5, height=5)
Kraken_Burn_Label.grid(row=4, column=2)

# Make Menu Bar
menubar = tk.Menu(main)
main.config(menu=menubar)
file_menu = tk.Menu(menubar)
# tools menu
menubar.add_cascade(label="Tools", menu=file_menu)
file_menu.add_command(label="Map", command=showMap)
file_menu.add_command(label="Seaport Finder", command=locatePort)
file_menu.add_command(label="Money calculator", command=moneyCalc)
file_menu.add_command(label="Vail Voyage helper", command=lambda: vailHelp(main))
# fish menu
fish_menu = tk.Menu(menubar)
menubar.add_cascade(label="Fish", menu=fish_menu)
fish_menu.add_command(label="Splashtail", command=lambda: splashtail(main))
fish_menu.add_command(label="Pondie", command=lambda: pondie(main))
fish_menu.add_command(label="Anchientscale", command=lambda: ancientscales(main))
fish_menu.add_command(label="Plentifin", command=lambda: plentifin(main))
fish_menu.add_command(label="Wildsplash", command=lambda: wildsplash(main))
fish_menu.add_command(label="Devilfish", command=lambda: devilfish(main))
fish_menu.add_command(label="Battlegill", command=lambda: battlegill(main))
fish_menu.add_command(label="Wrecker", command=lambda: wrecker(main))
fish_menu.add_command(label="Stormfish", command=lambda: stormfish(main))
fish_menu.add_command(label="Islehopper", command=lambda: islehopper(main))
fish_menu.add_separator()
fish_menu.add_command(label="All Fish", command=lambda: allFish(main))
# options menu
sound = tk.IntVar(main, name="sound")
sound.set(0)
option_menu = tk.Menu(menubar)
menubar.add_cascade(label="Options", menu=option_menu)
option_menu.add_radiobutton(label="Sound On", variable=sound, value=0, command=soundOn)
option_menu.add_radiobutton(label="Sound Off", variable=sound, value=1, command=soundOff)
# Help menu
help_menu = tk.Menu(menubar)
menubar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label="About", command=showHelp)
help_menu.add_command(label="How To Use", command=howTo)


main.after(0, timer)
tk.mainloop()

#  This is a cooking timer for Sea of Thieves
#
# fish = 30sec undercook, 40s cooked, 80s burn
# trophy fish 80s undercook, 90s cooked, 180s burn
# meat 50s undercook, 60s cook, 120s burn
# Kraken and Meg 100s undercook, 120s cook, 240s burn

import tkinter as tk


fishTime = 0
trophyTime = 0
meatTime = 0
krakenTime = 0
cookingFish = False
cookingTrophy = False
cookingMeat = False
cookingKraken = False
fishStatus = " "
trophyStatus = " "
meatStatus = " "
krakenStatus = " "


def showMap():
    global worldMap
    secondWindow = tk.Toplevel(main)
    # secondLabel = tk.Label(secondWindow, image=worldMap)
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
        Fish_Label.config(bg="Green")
        Fish_Label.config(fg="Yellow")
        if fishTime < 1:
            Fish_Label.config(bg="Red")
            Fish_Label.config(fg="Black")
            fishStatus = "Cooked"
            if fishTime < -40:
                fishStatus = "Burned"
                Fish_Label.config(bg="Black")
                Fish_Label.config(fg="White")
            if fishTime < -300:
                cookingFish = False
                fishStatus = " "
                fishTime = 0
        Fish_Label['text'] = str(trophyTime)
    if cookingTrophy:
        trophyTime -= 1
        Trophy_Label.config(bg="Green")
        Trophy_Label.config(fg="Yellow")
        if trophyTime < 1:
            Trophy_Label.config(bg="Red")
            Trophy_Label.config(fg="Black")
            trophyStatus = "Cooked"
        if trophyTime < -119:
            trophyStatus = "Burning"
            Trophy_Label.config(bg="Black")
            Trophy_Label.config(fg="White")
        if trophyTime < -300:
            cookingTrophy = False
            trophyStatus = " "
            trophyTime = 0
    Trophy_Label['text'] = str(fishTime)
    if cookingMeat:
        meatTime -= 1
        Meat_Label.config(bg="Green")
        Meat_Label.config(fg="Yellow")
        if meatTime < 1:
            Meat_Label.config(bg="Red")
            Meat_Label.config(fg="Black")
            meatStatus = "Cooked"
        if meatTime < -60:
            meatStatus = "Burned"
            Meat_Label.config(bg="Black")
            Meat_Label.config(fg="White")
        if meatTime < -300:
            cookingMeat = False
            meatStatus = " "
            meatTime = 0
    Meat_Label['text'] = str(meatTime)
    if cookingKraken:
        krakenTime -= 1
        Kraken_Label.config(bg="Green")
        Kraken_Label.config(fg="Yellow")
        if krakenTime < 1:
            Kraken_Label.config(bg="Red")
            Kraken_Label.config(fg="Black")
            krakenStatus = "Cooked"
        if meatTime < -120:
            krakenStatus = "Burned"
            Kraken_Label.config(bg="Black")
            Kraken_Label.config(fg="White")
        if krakenTime < -300:
            cookingKraken = False
            krakenStatus = " "
            krakenTime = 0
    Kraken_Label['text'] = str(krakenTime)

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
        cookingFish = True
        cookingTrophy = False
        cookingMeat = False
        cookingKraken = False
        Fish_Label.config(bg="Green")
        Fish_Label.config(fg="Yellow")
        fishStatus = "Cooking"
        fishTime = 40
        trophyTime = 0
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
    elif x == 'trophy':
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
    elif x == 'meat':
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
    elif x == 'kraken':
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


main = tk.Tk()
main.title("SoT Cooking Timer 0.2")
worldMap = tk.PhotoImage(file="Map4.png")

fish_image = tk.PhotoImage(file="fish.png")
trophy_image = tk.PhotoImage(file="TrophyFish.png")
meat_image = tk.PhotoImage(file="meat.png")
kraken_image = tk.PhotoImage(file="LegendMeat.png")

Fish_Button = tk.Button(main, image=fish_image, text="Fish", command=lambda: setTimer('fish'))
Fish_Button.grid(row=0, column=0)
Fish_Label = tk.Label(main, text=str(fishTime))
Fish_Label.config(bg="Light Grey", width=5, height=5)
Fish_Label.grid(row=0, column=1)
Fish_Status_Label = tk.Label(main, text=fishStatus)
Fish_Status_Label.grid(row=0, column=2)

Trophy_Button = tk.Button(main, image=trophy_image, text="Trophy Fish", command=lambda: setTimer('trophy'))
Trophy_Button.grid(row=1, column=0)
Trophy_Label = tk.Label(main, text=str(trophyTime))
Trophy_Label.config(bg="Light Grey", width=5, height=5)
Trophy_Label.grid(row=1, column=1)
Trophy_Status_Label = tk.Label(main, text=trophyStatus, width=8, height=8)
Trophy_Status_Label.grid(row=1, column=2)

Meat_Button = tk.Button(main, image=meat_image, text="Normal Meat", command=lambda: setTimer('meat'))
Meat_Button.grid(row=2, column=0)
Meat_Label = tk.Label(main, text=str(meatTime))
Meat_Label.config(bg="Light Grey", width=5, height=5)
Meat_Label.grid(row=2, column=1)
Meat_Status_Label = tk.Label(main, text=meatStatus, width=8, height=8)
Meat_Status_Label.grid(row=2, column=2)

Kraken_Button = tk.Button(main, image=kraken_image, text="Normal Meat", command=lambda: setTimer('kraken'))
Kraken_Button.grid(row=3, column=0)
Kraken_Label = tk.Label(main, text=str(meatTime))
Kraken_Label.config(bg="Light Grey", width=5, height=5)
Kraken_Label.grid(row=3, column=1)
Kraken_Status_Label = tk.Label(main, text=meatStatus, width=8, height=8)
Kraken_Status_Label.grid(row=3, column=2)


# Make Menu Bar
menubar = tk.Menu(main)
main.config(menu=menubar)
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="Tools", menu=file_menu)
file_menu.add_command(label="Map", command=showMap)

main.after(0, timer)
tk.mainloop()

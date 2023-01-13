import tkinter as tk

def allFish(main):
    allfishWindow = tk.Toplevel(main)
    allfishWindow.iconbitmap("fish.ico")
    allSplash = tk.Label(allfishWindow, text="Splashtail's can be found anywhere, no need for bait.", fg="Red",
                         font=("Arial", 18)).pack()
    allPondie = tk.Label(allfishWindow, text="Pondie's are found in fresh water ponds. No bait is needed", fg="Blue",
                         font=("Arial", 18)).pack()
    allPlentifin = tk.Label(allfishWindow,
                            text="Plentifin's are found in the Shores of Plenty. Use Earthworms for bait", fg="Red",
                            font=("Arial", 18)).pack()
    allWildsplash = tk.Label(allfishWindow, text="Wildsplash's are found in the Wilds. use Earthworms for bait",
                             fg="Blue", font=("Arial", 18)).pack()
    allAncientscale = tk.Label(allfishWindow,
                               text="Ancientscale's can be found in the ancient isles. Use Leeches for bait", fg="Red",
                               font=("Arial", 18)).pack()
    allDevilfish = tk.Label(allfishWindow, text="Devilfish are found in the Devil's Roar. use Grubs for bait",
                            fg="Blue", font=("Arial", 18)).pack()
    allBattlegill = tk.Label(allfishWindow,
                             text="Battlegill are found near skeleton ships and active skull forts. use Grubs for bait",
                             fg="Red", font=("Arial", 18)).pack()
    allWrecker = tk.Label(allfishWindow, text="Wreckers are found near shipwrecks. use Earthworms as bait.", fg="Blue",
                          font=("Arial", 18)).pack()
    allStormfish = tk.Label(allfishWindow, text="Stormfish are found in the storm. Use Leeches as bait.", fg="Red",
                            font=("Arial", 18)).pack()
    allIslehopper = tk.Label(allfishWindow, text="Islehoppers are only found close to islands. No bait is needed",
                             fg="Blue", font=("Arial", 18)).pack()
    allIslehopper2 = tk.Label(allfishWindow,
                              text="Open the Islehopers section from the fish menu for details on where to find each kind of Islehopper",
                              fg="Blue", font=("Arial", 18)).pack()


def splashtail(main):
    splashtailWindow = tk.Toplevel(main)
    splashtailWindow.iconbitmap("fish.ico")
    splashtailWindow.title('Splashtail')
    splashLabel = tk.Label(splashtailWindow, text="Splashtail's can be found anywhere, no need for bait.").pack()


def pondie(main):
    pondieWindow = tk.Toplevel(main)
    pondieWindow.iconbitmap("fish.ico")
    pondieWindow.title('Pondie')
    pondieLabel = tk.Label(pondieWindow, text="Pondie's are found in fresh water ponds. No bait is needed").pack()


def plentifin(main):
    plentifinWindow = tk.Toplevel(main)
    plentifinWindow.iconbitmap("fish.ico")
    plentifinWindow.title('Plentifin')
    plentifinLabel = tk.Label(plentifinWindow,
                              text="Plentifin's are found in the Shores of Plenty. Use Earthworms for bait").pack()


def wildsplash(main):
    wildsplashWindow = tk.Toplevel(main)
    wildsplashWindow.iconbitmap("fish.ico")
    wildsplashWindow.title('Wildsplash')
    wildsplashLabel = tk.Label(wildsplashWindow,
                               text="Wildsplash's are found in the Wilds. use Earthworms for bait").pack()


def ancientscales(main):
    ancientscaleWindow = tk.Toplevel(main)
    ancientscaleWindow.iconbitmap("fish.ico")
    ancientscaleWindow.title('Ancientscale')
    ancientscaleLabel = tk.Label(ancientscaleWindow,
                                 text="Ancientscale's can be found in the ancient isles. Use Leeches for bait").pack()


def devilfish(main):
    devilfishWindow = tk.Toplevel(main)
    devilfishWindow.iconbitmap("fish.ico")
    devilfishWindow.title('Devilfish')
    devilfishLabel = tk.Label(devilfishWindow,
                              text="Devilfish are found in the Devil's Roar. use Grubs for bait").pack()


def battlegill(main):
    battlegilWindow = tk.Toplevel(main)
    battlegilWindow.iconbitmap("fish.ico")
    battlegilWindow.title('Battlegill')
    battlegilLabel = tk.Label(battlegilWindow,
                              text="Battlegill are found near skeleton ships and active skull forts. use Grubs for bait"
                              ).pack()


def wrecker(main):
    wreckerWindow = tk.Toplevel(main)
    wreckerWindow.iconbitmap("fish.ico")
    wreckerWindow.title('Wrecker')
    wreckerLabel = tk.Label(wreckerWindow, text="Wreckers are found near shipwrecks. use Earthworms as bait.").pack()


def stormfish(main):
    stormfishWindow = tk.Toplevel(main)
    stormfishWindow.iconbitmap("fish.ico")
    stormfishWindow.title('Stormfish')
    stormfishLabel = tk.Label(stormfishWindow, text="Stormfish are found in the storm. Use Leeches as bait.").pack()


def islehopper(main):
    islehopperWindow = tk.Toplevel(main)
    islehopperWindow.iconbitmap("fish.ico")
    islehopperWindow.title('Islehopper')
    islehopperLabel = tk.Label(islehopperWindow,
                               text="Islehoppers are only found close to islands. No bait is needed").grid(row=0,
                                                                                                           column=0)
    islehopperLabel2 = tk.Label(islehopperWindow, text=" ").grid(row=1, column=0)
    islehopperLabel3 = tk.Label(islehopperWindow,
                                text="Stone Islehopper: Found at Shipwreck Bay, Shark Bait Cove, Crook's Hollow, Sailor's Bounty, Cannon Cove and Fetcher's Rest.").grid(
        row=2, column=0)
    islehopperLabel4 = tk.Label(islehopperWindow,
                                text="Moss Islehopper: Found at Ashen Reaches, Thieves' Haven, Marauder's Arch, Lone Cove, Wanderers Refuge and Ruby's Fall.").grid(
        row=3, column=0)
    islehopperLabel5 = tk.Label(islehopperWindow,
                                text="Honey Islehopper: Found at Discovery Ridge, Plunder Valley, Kraken's Fall, Sunken Grove, Crescent Isle and The Devil's Thirst.").grid(
        row=4, column=0)
    islehopperLabel6 = tk.Label(islehopperWindow,
                                text="Raven Islehopper: A rare sight at any large island. (TIP: Fish for this variant during the day at any island where Amethyst Islehoppers are found. You will only get Splashtails or Raven Islehoppers.)").grid(
        row=5, column=0)
    islehopperLabel7 = tk.Label(islehopperWindow,
                                text="Amethyst Islehopper: A night time catch found at Devil's Ridge, Smuggler's Bay, Mermaid's Hideaway, The Crooked Masts, Old Faithful Isle, Flintlock Peninsula and Snake Island.").grid(
        row=6, column=0)

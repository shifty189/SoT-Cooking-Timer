import tkinter as tk
"""
https://rarethief.com/sea-of-thieves-all-sudds-locations-in-the-legend-of-the-veil-voyage/
"""

def clearWindow(window):
    for widget in window.winfo_children():
        widget.destroy()


def skullshrineDisplay(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window, text="Old fithful island, top of the island to the east by a pile of skulls")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\skullshrine.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()


def ancientbeliefsDisplay(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window, text="East side of Old Faithful island by a shipwreck")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\ancientbeliefs.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()


def campkrakenDisplay(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window, text="in a camp on the east side of the island")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\campkraken.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()



def stonesdeepDisply(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window, text="Kraken's fall, near the center of the island by an half dug up chest")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\stonesdeep.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()


def runinsDisplay(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window,text="Mermaid’s Hideaway, abandonded camp to the south")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\ruins.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()

def highmermaidDisplay(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window,
                         text="Mermaid’s Hideaway, high on the south side by an abandoned camp")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\highmermaid.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()

def beachcampDisplay(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window,
                         text="Cannon Cove, West side of the island inside the cove (C shape)")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\beachcamp.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()

def forgottenDisplay(window, list):
    """the list argument is only for a global list to store the image file.
        This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window,
                         text="Cannon Cove, Southeast beach by some barrels")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\forgotten.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()
def silentDisplay(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window,
                         text="Lone Cove, central area near the drunks grave")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\silent.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()

def lonerockDisplay(window, list):
    """the list argument is only for a global list to store the image file.
        This is to prevent trash collection from removing the image before its used
        TODO: add image"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window,
                         text="Lone Cove, center of the island by a single large rock")
    infoLabel.pack(pady=3)
    # image = tk.PhotoImage(file="assets\\time.gif")
    # list.append(image)
    # imageLabel = tk.Label(window, image=image)
    # imageLabel.pack()


def timeDisplay(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window,
                         text="Sailor’s Bounty, Highest point of the mountian by some cooking pots")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\time.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()


def cursedskullsDisplay(window, list):
    """the list argument is only for a global list to store the image file.
            This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window,
                         text="Sailor’s Bounty, Southeast beach of the main island by a pile of skulls")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\cursedskulls.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()


def knowledgeispowerDisplay(window, list):
    """the list argument is only for a global list to store the image file.
        This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window,
                         text="Wanderer’s Refuge, North beach by stone foundations")
    infoLabel.pack(pady=3)
    # image = tk.PhotoImage(file="assets\\olsudds.gif")
    # list.append(image)
    # imageLabel = tk.Label(window, image=image)
    # imageLabel.pack()


def olSuddsDisplay(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used
    TODO: add image"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window,
                         text="Wanderer’s Refuge, South beach by a collasped building")
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\olsudds.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()


def anchientMap(window, list):
    """the list argument is only for a global list to store the image file.
        This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window,
                         text="Smuggler’s Bay, at the large camp in front of Smuggler's cave")
    infoLabel.pack(pady=3)
    # image = tk.PhotoImage(file="assets\\crescent_shape.gif")
    # list.append(image)
    # imageLabel = tk.Label(window, image=image)
    # imageLabel.pack()


def libraryDisplay(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used
    TODO: add better image"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window, text='at Smuggler’s Bay, by a shaded library to the East')
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\library.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()


def fiveBarnicleDisplay(window, list):
    """the list argument is only for a global list to store the image file.
        This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window, text='Crescent Isle, on the SouthEast side of the island by 5 pots')
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\five-barnacle.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()


def cresantShapeDisplay(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window, text='Crescent Isle, on the SouthWest side of the island on Rocks overlooking to the West')
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="assets\\crescent_shape.gif")
    list.append(image)
    imageLabel = tk.Label(window, image=image)
    imageLabel.pack()


def find_sudds(window, list):
    """the list argument is only for a global list to store the image file.
    This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    title_frame = tk.Frame(window)
    title_frame.pack()
    title_label = tk.Label(title_frame,
                           text="Select the in game text for a description of where to find Sudds",
                           foreground='Red'
                           )
    title_label.pack()
    location_frame = tk.Frame(window)
    location_frame.pack()
    fivebarnicle_text = "Five there were, and barnacled. I'm on the east beach of Crescent Isle with knowledge to share"
    five_barnicle_button = tk.Button(location_frame,
                                     text=fivebarnicle_text,
                                     command=lambda x = window: fiveBarnicleDisplay(x, list)
                                     )
    five_barnicle_button.pack(pady=5)
    cresant_shape_text = "Come to the island in the shape of a crescent, I'll be watching my friends atop the rock"
    cresant_shape_button = tk.Button(location_frame,
                                     text=cresant_shape_text,
                                     command=lambda x = window: cresantShapeDisplay(x, list))
    cresant_shape_button.pack(pady=5)
    library_text = "Libraries are sacred places, repositories of knowledge. Come and find me on Smuggler's Bay, I have Ancient knowledge to impart"
    library_button = tk.Button(location_frame,
                               text=library_text,
                               command=lambda x = window: libraryDisplay(x, list)
                               )
    library_button.pack(pady=5)
    achient_map_text = "The map is finished! The knowledge of the Ancients. Join me at Smuggler's Bay"
    achient_map_button = tk.Button(location_frame,
                                   text= achient_map_text,
                                   command=lambda x = window: anchientMap(x, list)
                                   )
    achient_map_button.pack(pady=5)
    ol_sudds_text = "Not all who wander find what they seek, but ol' Sudds did, oh yes he did. Come to the south beach of Wanderer's Refuge and I'll tell you more"
    ol_sudds_button = tk.Button(location_frame,
                                text = ol_sudds_text,
                                command=lambda x = window: olSuddsDisplay(x, list)
                                )
    ol_sudds_button.pack(pady=5)
    knowledgeispower_text = "Knowledge is powerful, too powerful in the wrong hands. Come to Wanderer's Refuge. At the ruins we will protect the knowledge of the Ancients"
    knowledgeispower_button = tk.Button(location_frame,
                                        text= knowledgeispower_text,
                                        command=lambda x = window: knowledgeispowerDisplay(x, list)
                                        )
    knowledgeispower_button.pack(pady=5)
    cursedskulls_text = "Cursed Skulls, so many curses haunt the Sea of Thieves, but why? The Coral Curse, the first? Sorry. Meet me on the south beach of Sailor's Bounty"
    cursedskulls_button = tk.Button(location_frame,
                                    text = cursedskulls_text,
                                    command=lambda x = window: cursedskullsDisplay(x, list)
                                    )
    cursedskulls_button.pack(pady=5)
    time_text = "Time, it moves so fast. Join me at the camp atop Sailor's Bounty. We'll reach back in time, we will, and find the location of a Veil Stone"
    time_button = tk.Button(location_frame,
                            text= time_text,
                            command=lambda x = window: timeDisplay(x, list)
                            )
    time_button.pack(pady=5)
    lonerock_text = "Lone Cove, lone rock, standing tall. Come and find me, I have something important to give you"
    lonerock_button = tk.Button(location_frame,
                                text= lonerock_text,
                                command=lambda x = window: lonerockDisplay(x, list)
                                )
    lonerock_button.pack(pady=5)
    silent_text = "Silent as the grave, oh yes I am. Come to Lone Cove and I'll reveal the location of the stone"
    silent_button = tk.Button(location_frame,
                              text= silent_text,
                              command=lambda x = window: silentDisplay(x, list)
                              )
    silent_button.pack()
    forgotten_text = "A castaway left on the shore, forgotten. Like the Veil Stone, forgotten until people sought its power once more. Come and find me on Cannon Cove"
    forgotten_button = tk.Button(location_frame,
                                 text= forgotten_text,
                                 command=lambda x = window: forgottenDisplay(x, list)
                                 )
    forgotten_button.pack(pady=5)
    beachcamp_text = "Meet me at the beach camp on Cannon Cove and I'll share what I know"
    beachcamp_button = tk.Button(location_frame,
                                 text=beachcamp_text,
                                 command=lambda x = window: beachcampDisplay(x, list)
                                 )
    beachcamp_button.pack(pady=5)
    highmermaid_text = "High on Mermaid's Hideaway, great vantage point. Much to tell you, too much, must get it written down. Two worlds that must never be one. Hurry"
    highmermaid_button = tk.Button(location_frame,
                                   text= highmermaid_text,
                                   command=lambda x = window: highmermaidDisplay(x, list)
                                   )
    highmermaid_button.pack(pady=5)
    runins_text = "I'll wait for you in the ruins on Mermaid's Hideaway. Make haste, this knowledge must not fall into the wrong hands"
    runins_button = tk.Button(location_frame,
                              text=runins_text,
                              command=lambda x = window: runinsDisplay(x, list)
                              )
    runins_button.pack(pady=5)
    stones_text = "The Veil Stone wasn't in the chest on the north of Kraken's Fall, should have known, should have known… The Ancients buried the stones deep, come find me and I'll tell you all."
    stones_button = tk.Button(location_frame,
                              text=stones_text,
                              command=lambda x=window: stonesdeepDisply(x, list)
                              )
    stones_button.pack(pady=5)

    campkraken_text = "No time to waste, meet at the camp on Kraken's Fall. Knowledge must be preserved, the stone must be protected."
    campkraken_button = tk.Button(location_frame,
                              text=campkraken_text,
                              command=lambda x=window: campkrakenDisplay(x, list)
                              )
    campkraken_button.pack(pady=5)

    ancientbeliefs_text = "My research has led me to many places and I have learned much about the Ancients and their beliefs. Seek me amongst the wreck of a ship to the east of Old Faithful Isle and I'll share a little with you."
    ancientbeliefs_button = tk.Button(location_frame,
                                  text=ancientbeliefs_text,
                                  command=lambda x=window: ancientbeliefsDisplay(x, list)
                                  )
    ancientbeliefs_button.pack(pady=5)

    skullshrine_text = "The location of the Veil Stone, I'm almost certain. Just need to check my hypothesis at the skull shrine atop Old Faithful Isle, meet there."
    skullshrine_button = tk.Button(location_frame,
                                      text=skullshrine_text,
                                      command=lambda x=window: skullshrineDisplay(x, list)
                                      )
    skullshrine_button.pack(pady=5)

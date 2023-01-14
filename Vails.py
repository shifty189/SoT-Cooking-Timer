import tkinter as tk
"""
https://rarethief.com/sea-of-thieves-all-sudds-locations-in-the-legend-of-the-veil-voyage/
"""

def clearWindow(window):
    for widget in window.winfo_children():
        widget.destroy()


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
    title_label = tk.Label(title_frame, text="select the in game text for a description of where to find Sudds")
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

import tkinter as tk
"""
https://rarethief.com/sea-of-thieves-all-sudds-locations-in-the-legend-of-the-veil-voyage/
"""

def clearWindow(window):
    for widget in window.winfo_children():
        widget.destroy()


def fiveBarnicleDisplay(window, list):
    """the list argument is only for a global list to store the image file.
        This is to prevent trash collection from removing the image before its used"""
    clearWindow(window)
    infoFrame = tk.Frame(window)
    infoFrame.pack()
    infoLabel = tk.Label(window, text='Crescent Isle, on the SouthEast side of the island by 5 pots')
    infoLabel.pack(pady=3)
    image = tk.PhotoImage(file="five-barnacle.gif")
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
    image = tk.PhotoImage(file="crescent_shape.gif")
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
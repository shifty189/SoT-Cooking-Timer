#Version .1
from tkinter import messagebox

def findPort(x,y):
    # print("x is: " + x + " Y is: " + y)
    portLocations = ["B7", "H10", "F17", "L15", "S10", "O4", "Y12", "U20"]
    ports = {
        "The Spoils of Plenty Store": "B7", "The North Star Seapost": "H10", "The Finest Trading Post": "F17",
        "Stephen's Spoils": "L15", "Three Paces East Seapost": "S10", "The Wild Treasures Store": "O4",
        "Brian's Bazaar": "Y12", "Roaring Traders": "U20"
    }

    key = [
        "The Spoils of Plenty Store", "The North Star Seapost", "The Finest Trading Post", "Stephen's Spoils",
        "Three Paces East Seapost", "The Wild Treasures Store", "Brian's Bazaar", "Roaring Traders"
    ]

    # key = {
    #     1: "The Spoils of Plenty Store", 2: "The North Star Seapost", 3: "The Finest Trading Post",
    #     4: "Stephen's Spoils", 5: "Three Paces East Seapost", 6: "The Wild Treasures Store", 7: "Brian's Bazaar",
    #     8: "Roaring Traders"
    # }

    def compute(x, y):
        return abs(ord(x) - ord(y))

    answer = []
    temp = []
    temp2 = []
    for loc in portLocations: #loop to find ver
        temp.append(compute(loc[0], y))
        temp2.append(abs(int(x) - int(loc[1:99])))
    for i, k in enumerate(temp):
        answer.append(int(k) + int(temp2[i]))
    # indexA = answer.index(min(answer))
    # print(key[answer.index(min(answer))] + " " + ports[key[answer.index(min(answer))]])
    # return key[answer.index(min(answer))] + " " + ports[key[answer.index(min(answer))]]
    messagebox.showinfo(title="seaport location", message= "The closest seaport is " + key[answer.index(min(answer))] +
                                    " located at: " + ports[key[answer.index(min(answer))]])
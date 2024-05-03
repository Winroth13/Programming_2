from bike import Bike
from difflib import get_close_matches as getCloseMatches

bikeList = []

mainMenuOptions = {
    "add": "addBike()",
    "remove": "removeBike()",
    "show": "showBikes()",
    "most expensive": "viewMostExpensiveBike()",
    "exit": "exit()",
}


def askForInput(question):
    print(question)
    print("")
    response = input("")
    print("")
    print("##########################")
    print("")
    return response


def storageEmpty():
    if len(bikeList) == 0:
        print("Bike storage empty.")
        return True
    else:
        return False


def mainMenu():
    print("")
    print("These are your options:")
    print("Add bike")
    print("Remove bike")
    print("Show bikes")
    print("View most expensive bike")
    print("Exit program")
    return askForInput("Choose an option by writting it's corresponding number.")


def addBike():
    model = askForInput("What's the model of the bike?")
    price = int(askForInput("What's the price of the bike?"))
    print("Bike succesfully added.")
    bikeList.append(Bike(model, price))


def removeBike():
    model = askForInput("Which model is the bike that you want to remove?")
    price = int(askForInput("WHat's the price of the bike you want to remove?"))
    for i in range(len(bikeList)):
        if bikeList[i].getModel() == model and bikeList[i].getPrice() == price:
            # I do not let use getCloseMatches (difflib.get_close_matches), since I do not
            # trust the used to not have several bikes with the same or very similar names.
            bikeList.remove(bikeList[i])
            print("Bike succefully removed.")
            return
    print("Bike not found.")


def showBikes():
    if not storageEmpty():
        print("These are the bikes in storage:")
        for i in range(len(bikeList)):
            print("")
            bikeList[i].showInfo()


def viewMostExpensiveBike():
    if not storageEmpty():
        print("Most expensive bike:")
        print("")
        for i in range(len(bikeList)):
            if i == 0:
                mostExpensiveBike = bikeList[i]
            elif bikeList[i].getPrice() > mostExpensiveBike.getPrice():
                mostExpensiveBike = bikeList[i]
        mostExpensiveBike.showInfo()


print("")
print("Welcome to the bike storage manager.")

while True:
    mainMenuChoice = mainMenu().lower()

    match = getCloseMatches(mainMenuChoice, mainMenuOptions.keys(), 1)
    if match:
        exec(mainMenuOptions[match[0]])
    else:
        print("That was not an option.")

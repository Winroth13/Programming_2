from bike import Bike

bikeList = []

print("")
print("Welcome to the bike storage manager.")
print("")

exit = "n"
while exit == "n":
    print("")
    print("These are your options:")
    print("(1) Add bike")
    print("(2) Remove bike")
    print("(3) Show bikes")
    print("(4) Show most expensive bike")
    print("Choose an option by writting it's corresponding number.")
    print("")
    response = input("")
    print("")
    print("##########################")
    print("")

    if response == "1":
        print("What's the model of the bike?")
        print("")
        model = input("")
        print("")
        print("##########################")
        print("")
        print("What's the price of the bike?")
        print("")
        price = input("")
        print("")
        print("##########################")
        print("")
        print("Bike succesfully added.")
        print("")
        bikeList.append(Bike(model, price))
    elif response == "2":
        print("Which model is the bike that you want to remove?")
        print("")
        model = input("")
        print("")
        print("##########################")
        print("")
        print("WHat's the price of the bike you want to remove?")
        print("")
        price = input("")
        print("")
        for i in range(len(bikeList)):
            bikeInfo = bikeList[i].getInfo()
            if bikeInfo[0] == model and bikeInfo[1] == price:
                break
    elif response == "3":
        print("These are the bikes in storage:")
        for i in range(len(bikeList)):
            bikeList[i].showInfo()
            print("")
        print("##########################")
    elif response == "4":
        pass
    else:
        print("")
        print("That was not an option.")
        print("")

import csv

with open("uppgift_c.csv", "r") as gameFile:
    reader = csv.reader(gameFile, delimiter=";")

    gameResults = []

    for game in reader:
        gameID, results = game[0].split(": ")

        gameNumber = int(gameID.split(" ")[1])

        numberPerColour = {"ID": gameNumber, "red": 0, "green": 0, "blue": 0}

        set = results.split(", ")

        for subset in set:
            number, colour = subset.split(" ")

            if numberPerColour[colour] < int(number):
                numberPerColour[colour] = int(number)

        gameResults.append(numberPerColour)

gameSum = 0

coloursInPouch = {"red": 12, "green": 13, "blue": 14}

for game in gameResults:
    valid = True
    for key, value in game.items():
        if key != "ID":
            if value > coloursInPouch[key]:
                valid = False
    if valid:
        gameSum += game["ID"]

print(gameSum)

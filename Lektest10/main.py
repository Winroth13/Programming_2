import pickle

try:
    with open("Lektest10/highscore.pkl", "rb") as file:
        highscore = pickle.load(file)

    print(f"Högsta poängen är {highscore}.")

    emptyFile = False
except:
    print("Det finns inga tidigare poäng.")

    emptyFile = True

print("")
print("Vad var dina poäng?")
print("")
newScore = input("")

if emptyFile or float(newScore) > float(highscore):
    with open("Lektest10/highscore.pkl", "wb") as file:
        pickle.dump(newScore, file)

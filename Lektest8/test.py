import time


class Course:
    def __init__(self, grade: str, weight: int):
        self.grade = grade
        self.weight = weight


gradeValues = {"A": 20, "B": 17.5, "C": 15, "D": 12.5, "E": 10, "F": 0}


def calculateAverage(courseList: list[Course]):
    gradeSum = 0
    totalWeight = 0

    for course in courseList:
        gradeSum += gradeValues[course.grade] * course.weight

        totalWeight += course.weight

    average = gradeSum / totalWeight

    return average


def question(question: str):
    print("")
    print(question)
    print("")
    return input("")


def askForGrade():
    grade = question("Skriv in betyget för en kurs.").upper()

    if grade in gradeValues:
        return grade
    else:
        print("")
        print("Inte ett giltigt betyg.")
        print("")
        return askForGrade()


def askForWeight():
    weight = question("Hur många poäng är den kursen?")

    try:
        return int(weight)
    except:
        print("")
        print("Inte ett giltigt antal poäng.")
        print("")
        return askForWeight()


def askForMoreCourses():
    moreCourses = question("Har du fler kurser? (Ja/Nej)").upper()

    if moreCourses == "NEJ":
        print("")
        average = calculateAverage(courseList)
        print(f"Ditt meritvärde är {average}.")
        print("")
        time.sleep(10)
        init()
    elif moreCourses == "JA":
        courseInputs()
    else:
        print("")
        print('Du ska vara med "Ja" eller "Nej".')
        print("")
        askForMoreCourses()


def courseInputs():
    global courseList

    grade = askForGrade()
    weight = askForWeight()

    courseList.append(Course(grade, weight))

    askForMoreCourses()


def init():
    global courseList

    courseList = []

    print("Räkna ut ditt meritvärde!")
    print("")
    print("Tryck på skärmen för att fortsätta.")
    input("")
    courseInputs()


init()

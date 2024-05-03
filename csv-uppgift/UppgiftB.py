import csv
from typing import List

gradeValue = {"A": 20, "B": 17.5, "C": 15, "D": 12.5, "E": 10, "F": 0}

def calculateGrade(grades: List[str]) -> float:
    sum = 0
    
    for grade in grades:
        sum += gradeValue[grade]
        
    average = sum / len(grades)
    
    return average

# Uppgift 3:
def pupilGrade(name: str) -> float:
    with open("Klasslista.csv", "r", encoding="utf-8-sig") as classFile:
        reader = csv.DictReader(classFile, delimiter=";")
        
        grades = []
        
        for row in reader:
            if row["Namn"] == name:
                for key, value in row.items():
                    if key != "Namn":
                        grades.append(value)
        
        print(f"{name} har i genomsnitt betyget: {calculateGrade(grades)}")
        return calculateGrade(grades)

pupilGrade("Erik")

# Uppgift 4:
def classGrade() -> float:
    with open("Klasslista.csv", "r", encoding="utf-8-sig") as classFile:
        reader = csv.DictReader(classFile, delimiter=";")
        
        grades = []
        
        for row in reader:
            for key, value in row.items():
                if key != "Namn":
                    grades.append(value)
        
        print(f"Klassen har i genomsnitt betyget: {calculateGrade(grades)}")
        return calculateGrade(grades)

classGrade()

# Uppgift 1-2:
with open("Klasslista.csv", "r", encoding="utf-8-sig") as classFile:
    reader = csv.DictReader(classFile, delimiter=";")

    with open("newClassFile.csv", "w", encoding="utf-8-sig") as newClassFile:
        writer = csv.DictWriter(newClassFile, delimiter=",", fieldnames=reader.fieldnames)

        writer.writeheader()

        for row in reader:
            writer.writerow(row)

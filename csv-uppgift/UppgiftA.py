import csv

with open("names.csv", "r") as namesFile:
    reader = csv.DictReader(namesFile)

    with open("newNames.csv", "w") as newNamesFile:
        writer = csv.DictWriter(
            newNamesFile, fieldnames=["number", "last_name", "email"]
        )

        writer.writeheader()

        lineNumber = 0

        for row in reader:
            if row["first_name"] != "Jane":
                lineNumber += 1
                del row["first_name"]
                row["number"] = lineNumber

                writer.writerow(row)

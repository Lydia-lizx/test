students_scores = {
     
    "Lydia": 95,
    "David": 87,
    "Alice": 92,
    "John": 78,
    "Sarah": 89
}
total = 0
for score in students_scores.values():
    total += score
average = total / len(students_scores)
print("class average:", average)

highest = max(students_scores.values())
lowest = min(students_scores.values())

print("Highest score:", highest)
print("Lowest score:", lowest)
for name, score in students_scores.items():
    if score == highest:
        print("Highest scoring student:", name)

    if score == lowest:
        print("Lowest scoring student:", name)

name = input("Enter student name: ")

score = students_scores.get(name)

if score is not None:
    print(f"{name} scored {score}")
else:
    print("Sorry, student not found!")
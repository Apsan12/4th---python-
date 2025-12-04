myDictionary = {
    "Alice" : 85,
    "Bob" : 90,
    "Charlie" : 78,
    "David" : 92
}

avgMarks = 0.0

for name, score in myDictionary.items():
    avgMarks += score
    print(f"student name: {name} student's score: {score}")

print(f"Average marks of all students is: {avgMarks / len(myDictionary)}")

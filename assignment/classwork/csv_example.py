import csv
 

# # Reading from the CSV file
# with open("students.csv", "r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(row)

# # Writing to the CSV file
# with open("students.csv", "w") as file:
#         writer = csv.writer(file)
#         writer.writerow([4, "new_student", 20])

# # Appending to the CSV file
# with open("students.csv", "a", newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([5, "another_student", 22])
  

# with open("tourist.csv", "w", newline = "") as file:
#         writer = csv.writer(file)
#         writer.writerow([4, "apsan", 21])
#         writer.writerow([4, "rohan k", 20])

# Reading from the CSV file using DictReader
with open("students.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["id", "name", "age"])
        writer.writeheader()
        writer.writerow({"id": 1, "name": "john doe", "age": 19})
        writer.writerow({"id": 2, "name": "jane doe", "age": 18})
        print("Data written successfully.")
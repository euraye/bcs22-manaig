'''Input:
 - Name
 - Q1
 - Q2
 - Q3
 - Final Exam
 - Class Participation
 -(Loop prompt) Do you want to enter new student record? (Y/N)

 Output:
 A table display of all the grades
 - Name
 - Q1
 - Q2
 - Q3
 - Final Exam
 - Class Participation
 - Final Grade (qTotal * 0.4) + (CP * 0.2) + (FE * 0.4)
 - Status (Passed / Failed) (Pass id >= 0.75 else failed)
 '''
from tabulate import tabulate

student_records = []

def userinput():
    while True:
        question = input("Do you want to enter a new student record? (Y/N): ")
        if question == "Y":
            print("Please input the following:")
            Name = input("Name: ")
            Q1 = int(input("Q1: "))
            Q2 = int(input("Q2: "))
            Q3 = int(input("Q3: "))
            FE = int(input("Final Exam: "))
            CP = int(input("Class Participation: "))
            computedgrades(Name, Q1, Q2, Q3, FE, CP)
        elif question == "N":
            print("These are the grades for this semester:")
            output()
            break
        else:
            print("Invalid input, please type again")

def computedgrades(Name, Q1, Q2, Q3, FE, CP):
    qTotal = (Q1 + Q2 + Q3) * 0.4
    final_exam = FE * 0.4
    classParticipation = CP * 0.2
    finalGrade = qTotal + classParticipation + final_exam
    result = "Passed" if finalGrade >= 75 else "Failed"
    student_records.append([Name, Q1, Q2, Q3, FE, CP, finalGrade, result])

def output():
    headers = ["Name", "Q1", "Q2", "Q3", "Final Exam", "Class Participation", "Final Grade", "Result"]
    print(tabulate(student_records, headers=headers, tablefmt="pretty"))

userinput()









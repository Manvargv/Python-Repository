#grde_calculator.py
#python

import random

def main():
    #step 1 Create an empty list to store grades 
    grades = []

    #step 1: get grades from user 
    while True:
       grade = input("Enter a grade (or -1 to finish): ")

       if grade == "-1":
         break
       else:
            grades.append(int(grade))

    # step 3: Print the list of grades
    print("\nGrades entered:", grades)

    # step 4: Remove the lowest grade
    print("\n-- Removing the lowest grade ---")
    lowest = min(grades)
    index_of_lowest = grades.index(lowest)
    grades.pop(index_of_lowest)
    print("Grades after removing lowest:", grades)

    #step 5: remove a random grade
    print("\n--- Removing a random grade ---")
    random_grade = random.choice(grades)
    grades.remove(random_grade)
    print("Grades after removing random grade:", grades)

    # step 6: edit a grade
    print("\n--- Editing a grade ---")
    for i in range(len(grades)):
       print(f"{i+1}. {grades[i]}")
    
    while True:
       choice = int(input("Enter the number of the grade you want to edit: "))
       if choice < 1 or choice > len(grades):
        print("Invalid choice. Try again. ")
    else:
        

        new_grade = int(input("Enter the new grade: "))
grades[choice - 1] = new_grade
print("Grades after editing:", grades)

    # step 7: sort and reverse the list 
print("\n--- Sorting and reversing the grades ---")
grades.sort()
grades.reverse()
print("Grades after sorting and reversing:", grades)

    #step 8: Calculate total and average 
print("\n--- Total and average of grades ---")
total = sum(grades)
average = total / len(grades)
print("Total of grades:", total)
print("Average grade:", average)

print("\nCompleted by, Manuel Vargas")
    
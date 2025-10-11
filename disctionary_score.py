import random

#key value pair of sudent names and scores
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

#finding out the highest score

highest_score =  max(student_scores.values())
print(f"The highest score is: {highest_score}")


#Amogh Thallapragada
#Mr. Sedlar
#Gradebook Project

lloyd = {"name": "Lloyd", "homework": [90.0, 97.0, 75.0, 92.0], "quizzes": [88.0, 40.0, 94.0], "tests": [75.0, 90.0]}

alice = {"name": "Alice", "homework": [98.0, 96.0, 93.0, 99.0], "quizzes": [100.0, 89.0, 95.0], "tests": [94.0, 96.0]}

tyler = {"name": "Tyler", "homework": [86.0, 72.0, 88.0, 82.0], "quizzes": [84.0, 55.0, 89.0], "tests": [70.0, 88.0]}

students = [lloyd, alice, tyler]

#for x in students:
    #print (x)

def average(num):
    total = float(sum(num))
    avg = total / len(num)
    return avg

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    totalavg = (homework * 0.1) + (quizzes * 0.3) + (tests * 0.6)
    return totalavg

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def class_average(students):
    results = []
    for y in students:
        results.append(get_average(y))
    return average(results)

print (average(lloyd["homework"]))
print (get_average(lloyd))
print (letter_grade(get_average(lloyd)))
print (class_average(students))
print (letter_grade(class_average(students)))
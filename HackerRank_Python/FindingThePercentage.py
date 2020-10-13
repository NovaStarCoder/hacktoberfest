n = int(input("Number of students' records: "))
dictionary = {}
name = ""
marks = []

for i in range(n):
    data = input("Student Name and marks: ")
    data = data.split(" ")
    for j in range(len(data)):
        if j == 0:
            name = data[j]
        else:
            marks.append(float(data[j]))
    

    dictionary.update({name:marks})
    name = ""
    marks = []

def finding_the_percentage(dic):
    mark_count = 0
    mark_sum = 0.0
    mark_average = 0.0
    search = input("Student name to search: ")
    for mark in dic.get(search):
        mark_sum += mark
        mark_count += 1
    mark_average = mark_sum / mark_count
    return mark_average

print(finding_the_percentage(dictionary))

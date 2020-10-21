def averageMarks(studentList): 
    return float(sum(studentList)/len(studentList))


if __name__ == '__main__':
    N = int(input())
    marks = {}

    for i in range(N):
        a = input()
        s = a.split()

        marks[s[0]] = averageMarks(list(map(float, s[1:])))

    query_name = input()

    print("{0:.2f}".format(marks.get(query_name)))
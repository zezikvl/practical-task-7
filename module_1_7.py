grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sort = sorted(students)
grades_middle = []

for middle in grades:
    s = sum(middle)/len(middle)
    grades_middle.append(s)

answer = dict(zip(students_sort, grades_middle))
print(answer)
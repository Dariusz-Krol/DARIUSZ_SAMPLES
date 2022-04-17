student_heights = input("Input a list of people heights in cm: ").split()
# funkcja poniżej zamienia wszystkie wpisane wysokości na INT i określa parametr n = ilość zmiennych w liście
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# pętla powyżej to operacje na liście, ktora zamienia liste z STR na liste zawierajaca zamienione ze STR INT w zamian
number_of_students = 0
for student in student_heights:
    number_of_students += 1
# print(number_of_students)
high_total =0
for high in student_heights:
    high_total += high
# print(high_total)
average = high_total / number_of_students
print(int(average))

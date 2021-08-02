student_heights = input("Input a list of student heights ").split()
total = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total += student_heights[n]
average = int(total/(n+1))
print(average)
print("Enter marks obtained in 4 Subjects: ")
maths = int(input("maths : "))
english = int(input("english : "))
science = int(input("science : "))
hindi = int(input("hindi : "))

sum = maths+english+science+hindi
print("sum of math,english,science and hindi = ", sum)

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)
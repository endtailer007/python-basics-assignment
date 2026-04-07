#Task 1
name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height(cm): "))
is_student=input("Are you a student? (Yes/No): ")
print(name,age,height,is_student)
#Task 2
print(f"Name: {name} | Age: {age} | Height: {height} | Student: {is_student}")
#Task 3
print(f"Age in months: {age*12}")
print(f"Age in days: {age*365}")
print(f"Reminder when age is divided by 7: {age%7}")
print(f"Age raised to the power of 2: {age**2}")

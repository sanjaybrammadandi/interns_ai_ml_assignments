#1. Print text
print ("hello sanjay")

#2.Variables
name = "Alice"
age = 25
print(name, age)

#3. User input
name = input("Enter your name: ")
print("Hello", name)
 
#4. Addition 
a = 5
b = 3
print(a + b)

#5. If statement
age = 18
if age >= 18:
    print("You are an adult")

#6. If–else
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#7. For loop
for i in range(5):
    print(i)

#8. While loop
count = 1
while count <= 5:
    print(count)
    count += 1

#9. List 
fruits = ["apple", "banana", "cherry"]
print(fruits)

#10. Access list elements
numbers = [10, 20, 30]
print(numbers[1])

#11. Add to a list
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

#12. Dictionary
student = {"name": "John", "age": 20}
print(student)

#13. Access dictionary value
student = {"name": "John", "age": 20}
print(student["name"])

#14. Function
def greet():
    print("Hello!")
greet()

#15. Function with parameters
def add(a, b):
    return a + b

print(add(3, 4))

#16. String length
text = "Python"
print(len(text))

#17. String uppercase
text = "python"
print(text.upper())

#18. Check membership
fruits = ["apple", "banana"]
print("apple" in fruits)

#19. Try–except
try:
    x = int("abc")
except ValueError:
    print("Conversion error")

#20. Import a module
import math
print(math.sqrt(16))


#Artificial Intelligence and Machine Learning enable computers to learn from data and make intelligent decisions without being explicitly programmed.

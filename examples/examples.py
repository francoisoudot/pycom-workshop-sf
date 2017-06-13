# Example 0 - Hello World
value = "Hello World"
print(value)

# Example 1 - For Loops
x = 0
for y in range(0,9):
     x += 1
print(x)

# Example 2 - If, Elif, Else
test = 15

if test > 10:
    print("Too High!")
elif test < 10:
    print("Too Low!")
else:
    print("Just right!")

# Example 3 - Methods/Functions
def greet(name):
    print('Hello' + name)

greet('Jack')
greet('Jill')
greet('Bob')

# Example 4 - Inputs
name = input('What is your name?\n')
print('Hi, %s.' % name)

# Example 5 - Classes
class Student:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

Sue = Student("Susan Miller", 20, "f")
print(Sue)
print(Sue.age)

# Example 6 - Lists
squares = [1, 4, 9, 16, 25]
print(squares[0])
print(squares[1])

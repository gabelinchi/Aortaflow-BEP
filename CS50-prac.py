#practice from CS50 lectures intro to python course

#grading
score = int(input("score: "))

if score >= 90:
    print ("Grade: A")
elif score >= 80:
    print ("Grade: B")
elif score >= 70:
    print ("Grade: C")
elif score >= 60:
    print ("Grade: D")
else:
    print ("Grade: F")

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    #return True if n % 2 == 0 else False
    #return (n % 2 == 0)
    if n % 2 == 0:
        return True
    else:
        return False

main()

#practice match function
name = input("Whats your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("WHo?")

#Loops

i = 3
while i != 0:
    print("meow")
    i = i - 1
    #i += 1

for _ in range(3): #_ for variable you dont care for
    print("mow")

print("maw\n" * 3, end="")

def man():
    number = get_number()
    meow(3)

def get_number():
    while True:
        n =int(input("WHats n? "))
        if n < 0:
            continue
        else:
            break

def meow(n):
    for _ in range(n):
        print("maw")

students = {"Hermione": "Gryff", 
            "Harry": "Gryff", 
            "Ron": "Gryff",
            "Draco": "Slyt"
            }

'''
for i in range(len(students)):
    print(i + 1, students[i])

'''

for student in students:
    print(student, students[student], sep=", ")

stdnts = [
    {"name": "Hermione", "house": "Gryff", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryff", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryff", "patronus": "Jack Russell"},
    {"name": "Draco", "house": "Slyth", "patronus": None}
    ]

for stdnt in stdnts:
    print(stdnt["name"], stdnt["house"], stdnt["patronus"], sep=", ")

#mario.py

def mar():
    #print_column(3)
    #print_row(4)
    print_square(3)

def print_column(height):
    print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end="")
        print()
mar()

#Exeptions
def min():
    x = get_int("Whats x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            int(input(prompt))
        except ValueError:
            print("x is not an integer")
        else:
            return x #pass
        
min()

#Libraries
import random
import statistics
import sys
import requests
import json
number = random.randint(1, 10)
statistics.mean([100, 90])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")


for arg in sys.argv[1:]:
    print("hello, my name is ", arg)

response = requests("insert hyperlink" + sys.argv1[])
print(json.dumps(response.json(),indent=2))
o = response.json()
for result in o["results"]:
    print(result["trackName"])

#Unit test
def square(n):
    return n * n

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
#pytest file
if __name__ == "__main__":
    main()
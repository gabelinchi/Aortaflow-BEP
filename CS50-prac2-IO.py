import csv
#I/O files

#method 1
def names_method1():
    names = []
    for _ in range(3):
        name.append(input("Whats ur name? "))

    for name in sorted(names):
        print(f"hallo, {name}")

def names_method2():
    name = input("Whats ur name? ")

    with open("name.txt", "a") as file: #"w" = write, "a" = append
        file.write(f"{name}\n")
        #file.close()
    
    with open("name.txt", "r") as file:
        for line in sorted(file):
            print("hallo,", line.rstrip())
    

def names_method3():
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().rsplit(",")
            #print(f"{name} is in {house}")
            
            student = {}
            student["name"] = name
            student["house"] = house
            student.append(student)
        
        for student in sorted(student, key=lambda student: student["name"], reverse=True):
            print(f"{student["name"]} is in {student["house"]}")
        
def names_method4():
    
    name = input("Whats ur name? ")
    home = input("Whats ur home? "
                 )
    with open("students.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})
    
    
    with open("students.csv") as file:
        reader = csv.reader(file)
        for name, home in reader:
            students.append({"name": name, "home": home})
        
        """
        reader = csv.DictReader(file)
        for row in reader:
            studendts.append({"name": row["name"], "home": row["home"]})
        """


        for student in sorted(student, key=lambda student: student["name"], reverse=True):
            print(f"{student["name"]} is in {student["house"]}")


import sys
from PIL import Image

def image_method1():
    images = []

    for arg in sys.argv[1:]:
        image = Image.open(arg)
        image.append(Images)
    
    images[0].save(
        "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
    )

    #to run -> python "current file" "a bunch of images" 
    # and then run costumes.gif


import re

# Regular expresions
def email():
    email = input("Whats ur email? ").strip() #.lower()

    Username, domain = email.split("@")

    if re.search(r"^[a-zA-Z0-9_]+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE): 
        
        """
        r = raw string
    
        # sytax for re.search
        . = any character exept newline
        * = 0 or more reps
        + = 1 or ''
        ? = 0 0r 1 reps
        {m} = m reps
        {m,n} = m-n reps
        ^ = matches the start of the string
        $ matches the end of the string or just before the newline at the end of the string
        [] = set of characters
        [^] = compliment the set
        A|B = either a or B
        (...) = a group
        (?:...) = non-capturing version

        w = all words -> their is a list for other exceptions

        re.IGNORECASE
        re.MULTILINE
        re.DOTALL

        re.match
        re.fullmatch
        """
        
        print("Valid")
    else:
        print("Invalid")

def name_method5():
    name = input("What ur name? ").strip()
    
    # if "," in name:
    #     last, first = name.split(", ")
    #     name = f"{first} {last}"
    # print(f"hello, {name}")
    if matches := re.search(r"^(.+), *(.+)$", name): #:= walrus operator alows to bolean and asign value

        #last, first = matches.groups()
        name = matches.group(2) + " " + matches.group(1)
    print(f"hello, {name}")

def url():
    url = input("URL: ").strip()
    
    # #url.replace  .removeprefix
    # username = url.removeprefix("https://twitter.com", "")
    

    # url = re.sub(r"(https?://)?(www\.)?twitter\.com/", "", url)
    # print(f"Username: {username}")
    
    #re.split

    if url := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_])$", url, re.IGNORECASE):
        print(f"Username:", matches.group(1))

def patterns():
    #code for hexadecimal color codes
    code = input("Hexadecimal color code: ")

    pattern = r"^#([0-9a-fA-F]){6}$"
    if match := re.search(pattern, code):
        print(f"Valid with {match.group()}")
    else:
        print("Invalid")
    

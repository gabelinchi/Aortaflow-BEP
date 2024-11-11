def les_set():
    students = [
        {"name": "Herm", "house": "gryff"},
        {"name": "Harry", "house": "gryff"},
        {"name": "ron", "house": "gryff"},
        {"name": "draco", "house": "slyth"},
        {"name": "padma", "house": "raven"},
    ]

    houses =set() # allows us to remove duplicates and tighten code
    for student in students:
        # if student["house"] not in houses:
        #     houses.append(student["house"])
        houses.add(student["houses"])

    for house in sorted(houses):
        print(house)

#use global
balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__": 
    main()

class Account:
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def man():
    account =Account()
    print("balance:", account.balance)
    account.deposit(200)
    account.withdraw(150)
    print("balance:", account.balance)

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
#cat.meow()
def mypy_expl():

    def meow(n: int) -> str:
            """
            Meow n times.
            
            :param n: Number of times to meow
            :type n: int
            :raise TypeError: if n is not an int
            :return: A string of n meows, one per line.
            :rtype: str
            """
            # for _ in range(n):
            #     print("meow")
            return "meow\n" * n

    number: int = int(input("number: "))
    meows: str = meow(number)
    print(meows, end="")
    #return meow(number)

import sys

def method():
    if len(sys.argv) == 1:
        print("meow")
    elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        n = int(sys.argv[2])
        for _ in range(n):
            print("meow")
        
    else:
        print("usage: meows.py")

#argparse handles aguments
import argparse
def prsr_prac1():
    parser = argparse.ArgumentParser(description="meow like a cat")
    parser.add_argument("-n", default=1, help="number of times to meow")
    args = parser.parse_args()

    for _ in range(args.n):
        print("meow")

"""unpacking lists 
* unpack list
** unpack dictionary
"""
def unp_prac():
    def total(galleons, sickles, knuts):
        return (galleons * 17 + sickles ) * 29 + knuts

    #coins = [100, 50, 25]
    coins = {"galleons": 100, "sickles": 50, "knuts": 25}
    print(total(**coins), "Knuts")

def unp_args_prac():
    def f(*args, **kwargs): #helps create dicts
        print("Named:", kwargs)

    f(galleons=100, sickles=50, knuts=25)

#map(function, itterable, ...) lesson
def map_prac():
    def main():
        yell(["this", "is", "CS50"])
        yell_improved(["this", "is", "CS50"])
        yell3(["this", "is", "CS50"])

    def yell(*words):
        uppercased = []
        for word in words:
            uppercased.append(word.upper())
        print(*uppercased)
    
    def yell_improved(*words):
        uppercased = map(str.upper, words)
        print(*uppercased)
    
    #list comprehension

    def yell3(*words):
        uppercased = [word.upper() for word in words]
        print(*uppercased)
    
    if __name__ == "__main__":
        main()

def map_prac2():
    students = [
        {"name": "Herm", "house": "gryff"},
        {"name": "Harry", "house": "gryff"},
        {"name": "ron", "house": "gryff"},
        {"name": "draco", "house": "slyth"},
        {"name": "padma", "house": "raven"},
    ]
    def strat_1():
        gryffs = [
            student["name"] for student in students if student["house"] == "gryff"
        ]
        for gryff in sorted(gryffs):
            print(gryff)
    
    #filter(function, itterable, ...)
    def strat_2():
        def is_gryff(s):
            return s["house"] == "gryff"
        
        gryffs = filter(is_gryff, students)

        for gryff in sorted(gryffs, key=lambda s: s["name"]):
            print(gryff["name"])

    
    def strat_3():          
        gryffs = filter(lambda s: s["house"] == "gryff", students)

        for gryff in sorted(gryffs, key=lambda s: s["name"]):
            print(gryff["name"])
    
    
    #active strat!!
    strat_2()
        
#dictionary comprehention
def dict_comp():
    students = ["Herm", "Harry", "Ron"]
    
    #active strat
    strat_4imprv()

    def strat_1():
        gryffs = []

        for student in students:
            gryffs.append({"name":student, "house": "Gryff"})

        print(gryffs)

    def strat_2():
        gryffs = [{"name": student, "house": "Gryff"} for student in students]

        print(gryffs)

    def strat_3():
        gryffs = {student: "Gryff" for student in students}

        print(gryffs)
    
    #enumerate(iterable, start=0) 
    # lets u improve 4 by taking seq of values and 
    # returns current index and current vallue
    def strat_4():
        for i in range(len(students)):
            print(i + 1, students[i])

    def strat_4imprv():
        for i, student in enumerate(students):
            print(i+1, student)
    
#generators -> yield
#u"\U0001F411"
def sleep():
    def main():
        n = int(input("whats n? "))
        for s in sheep(n):
            print(s)
    
    def sheep(n):
        def strat_1():
            flock =[]
            for i in range(n):
                flock.append(u"\U0001F411" * n)
            return flock

        def strat_2():
            for i in range(n):
                yield u"\U0001F411" * i 
                # yield will return 1 at a time
                #   better for ram

        #active strat!!
        strat_2()
    if __name__ == "__main__":
        main()

"""
recap:
-the double underscore syntax
-argV functions
-sys library
difference class and dict

"""
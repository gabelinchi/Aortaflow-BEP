class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg"

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg

def classes_method1():
#     packages = |"Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg|
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Alice", weight=5)
    ]
    for package in packages:
        print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}")

def Obj_orient_meth1():
    name, house get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

    if __name__ == "__Obj_orient_meth1__":
        Obj_orient_meth1()

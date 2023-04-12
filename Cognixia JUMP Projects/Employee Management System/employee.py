class Employee:
    name = ""
    age = ""
    birth = ""
    email = ""

    def __init__ (self, name, age, birth, email):
        self.name = name
        self.age = age
        self.birth = birth
        self.email = email

    def toString(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Age: {self.age}")
        print(f"Employe Birth Date: {self.birth}")
        print(f"Employee Email: {self.email}")
        print("\n")
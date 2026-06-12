class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self):
        return self.salary * 0.10

class Manager(Employee):
    # def __init__(self, name, salary):
    #     super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.20

class Developer(Employee):
    # def __init__(self, name, salary):
    #     super().__init__(name, salary)
        
    def calculate_bonus(self):
        return self.salary * 0.15
    
if __name__ == "__main__":
    employees = [
        Manager("Sai", 100000),
        Developer("Rahul", 100000)
    ]
    for e in employees:
     print(e.calculate_bonus())
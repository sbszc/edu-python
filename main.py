import json

class Person:
    id = 3
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id

class Employee(Person):
    salary = 3000
    def getSalary(self):
        return self.salary
    def setSalary(self, salary):
        self.salary = salary

empl = Employee()
print(1, 2, 3)
print(json.dumps(empl.__dict__))


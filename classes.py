class Person:
    name= "Bob"
    age= 16
    height= 4.9166

Bob= Person()

print(Bob.name)
print(Bob.age)
print(Bob.height)


class Place:
    continent= "South America"
    country= "Peru"
    city_or_monument= "Machu Pichu"

Machu_Pichu= Place()

print(Machu_Pichu.continent)
print(Machu_Pichu.country)
print(Machu_Pichu.city_or_monument)

class Location:
    def __init__(self, name, country, continent):
        self.name= name
        self.country= country
        self.continent= continent
    def __str__(self):
        return f"{self.name}-{ self.country}-{self.continent}"
    
Mount_Everest= Location("Mount Everest", "Nepal", "Asia")

print(Mount_Everest)
    

class User:
    def __init__(self, name, age, height):
        self.name= name
        self.age= age
        self.height= height

    def __str__ (self):
        return f"{self.name}({self.age}){ self.height}"
    

Sam= User( "Commander General", 23, 6.9166)

print(Sam.name)
print(Sam.age)
print(Sam.height)
print(Sam)

# class Employee:
#    def __init__(self, name, employee_id, position, salary):
#         self.name = name
#         self.employee_id = employee_id
#         self.position = position
#         self.salary = salary

#     #def display_info(self):
#      #      return f"Employee Name: {self.name}, ID: {self.employee_id}, Position: {self.position}, Salary: ${self.salary:.2f}"
   
# employee1=Employee("Billy Bob", 2345, "Software engineer", 10000)

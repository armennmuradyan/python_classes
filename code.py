# class Person: 
#    def __init__(self, name, surname, age):
#       # print("initializing Person")
#       self.name = name 
#       self.surname = surname 
#       self.age = age

#    def present(self):
#       return f"hi! my name is {self.name} {self.surname}. I'm {self.age} year old"


# class Student(Person):
#    def __init__(self, name, surname, age, uni):
#       # print("initializing Student")
#       super().__init__(name, surname, age)
#       self.uni = uni

#    def present(self):
#       return f"{self.uni}"


# class EconomyStudent(Student):
#    def __init__(self, name, surname, age, uni):
#       # print("initializing EconomyStudent")
#       super().__init__(name, surname, age, uni) 
#    def present(self):
#       return f"{self.uni} economy"


# class Employee(Person):
#    def __init__(self, name, surname, age, place, position):
#       # print("initializing Employee")
#       Person.__init__(self, name, surname, age)
#       self.place = place
#       self.position = position

#    def present(self):
#       return f"{self.position} at {self.place}"


# class MixStudent(Employee, Student):
#    def __init__(self, id_card, name, surname, age, place, position, uni):
#       self.id_card = id_card
#       Employee.__init__(self, name, surname, age, place, position)
#       Student.__init__(self, name, surname, age, uni)

#    def present(self):
#       return f"{self.id_card} {self.name} {self.surname} {self.age} {self.place} {self.position} {self.uni}"

# m_s = MixStudent("id_1100", "Armen", "Muradyan", 16, "Google", "developer", "YSMU")
# print(m_s.present())


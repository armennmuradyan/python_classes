# class Car: 
#    NAME = "car"
#    DESCRIPTION = "it runs"

#    def __init__(self, name, color, year):
#       self.car_name = name
#       self.color = color 
#       self.year = year
   
#    def present(self):
#       print(f"car name: {self.car_name} which color is {self.color} prod year {self.year}")
   
#    def set_horse_power(power):
#       self.hp = power
   
#    def change_color(self, color: str):
#       if type(color) == str:
#          if color and color.isalpha():
#             self.color = color
#          else:
#             raise ValueError("too short or not letter")
#       else:
#          raise ValueError("wrong value")
#       self.present_color()
#    def present_color(self):
#       print(f'Color is {self.color}')
   
      
# mercedes = Car("s600", "red", 2021)
# mercedes.change_color("white")
# # #mercedes.change_color(15)




# class Person:
#    NAME = "your name"
#    JOB = "your job"
#    EMAIL = "your email"


#    def __init__(self, name, job, email):
#       self.user_name = name
#       self.user_job = job
#       self.user_email = email
#
#    def present(self):
#       print(f"User name is {self.user_name}, Users job is {self.user_job}, users email is {self.user_email}")
#
#    def change_email(self, email: str):
#       self.email = email
#
#    def email_validator(self, email):
#       if "@" not in email:
#          raise ValueError("Wrong type of email")
#       return email
#
# user_ = Person("Armen", "programmer", "armenemail@gmail.com")
# user_.present()
# user_.email_validator('Armengmail.com')



# class Country:
#    def __init__(self, name, continent):
#       self.country_name = name
#       self.continent = continent
#
#    def present(self):
#       return f"The name of country is {self.country_name}. Continent is {self.continent}"
#
# # country_1 = Country("Armenia", "Asia")
# # print(country_1.present())
#
# class Brand:
#    def __init__(self, br_name, start_date):
#       self.br_name = br_name
#       self.start_date = start_date
#
#    def present(self):
#       return f"The name of brand is {self.br_name}. Start date is {self.start_date}"
#
# # brand_1 = Brand("Samsung", "10,14,2021")
# # print(brand_1.present())
#
# class Season:
#    def __init__(self, season_name, average_temp):
#       self.season_name = season_name
#       self.average_temp = average_temp
#
#    def present(self):
#       return f"Now it is {self.season_name}. Average temperature is {self.average_temp}"
#
# # season_1 = Season("Autumn", 20)
# # print(season_1.present())
#
# class Product(Country, Brand, Season):
#    def __init__(self, name, continent, br_name, start_date, season_name, average_temp, pr_name, pr_type, pr_price, pr_quantity):
#       self.pr_name = pr_name
#       self.pr_type = pr_type
#       self.pr_price = pr_price
#       self.pr_quantity = pr_quantity
#       Country.__init__(self, name, continent)
#       Brand.__init__(self, br_name, start_date)
#       Season.__init__(self, season_name, average_temp)
#
#    def present(self):
#       return f"The name of country is {self.country_name}. Continent is {self.continent}. The name of brand is {self.br_name}. Start date is {self.start_date}. \nNow it is {self.season_name}. Average temperature is {self.average_temp} \nProduct name is {self.pr_name}. Product type is {self.pr_type}. Product price is {self.pr_price}. Product quantity is {self.pr_quantity}"
#
#    def percent(self, discount_procent):
#       a = self.pr_price * discount_procent / 100
#       self.pr_price = self.pr_price - a
#       return self.pr_price
#    def increase_q(self):
#       user_choise = int(input("How much would you like to increase the quantity? \n"))
#       self.pr_quantity += user_choise
#       return f"The quantity changed - {self.pr_quantity}"
#    def decrease_q(self):
#       user_choise = int(input("How much would you like to increase the quantity? \n"))
#       self.pr_quantity -= user_choise
#       return f"The quantity changed - {self.pr_quantity}"
# # print(Product.__mro__)
#
#
# pr = Product("Armenia", "Asia", "Samsung", "10.14.2021", "Autumn", "20", "Samsung S21", "telephone", 500, 5)
# print(pr.percent(20))
# print(pr.increase_q())
# print(pr.decrease_q())
# # print(pr.present())


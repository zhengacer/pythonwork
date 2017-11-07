class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model		
		self.year = year
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
		
class Battery():
	
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size
	
	def describe_battery(self):
		print("This cat has a " + str(self.battery_size) + "kwh battery.")
	def get_range(self):
		if self.battery_size ==70:
				range = 240
		elif self.battery_size == 85:
			range = 270
			
		message = "This car can go approximately " + str(range)
#		message += "miles on a full charge."
		message = message + "miles on a full charge."
		print(message)
		

class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()
		
#		self.battery_size = 70
		
#	def describe_battery(self):
#		print("This car has a " + str(self.battery_size) + "kwh battery."
#		)


# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())  
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()



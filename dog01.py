class Dog():
	def _init_(self, name, age):
		self.name = name
		self.age = age
		
	def sit (self):
		print(self.name.title() + " is now sittting.")
	
	def roll_over(self):
		print(self.name.title() + " rolled over!")
		
		
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.titile() + ".")
print

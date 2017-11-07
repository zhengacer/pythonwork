class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def sit(self):
		print(self.name.title() + " is now sittting.")
	
	def roll_over(self):
		print(self.name.title() + " rolled over!")
		
		
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()


print("My dog's name is " + my_dog.name.title() + ".")

print("My dog is " + str(my_dog.age) + " years oid.")

you_dog = Dog('lucy', 3)
you_dog.sit()
you_dog.roll_over()

print("You dog's name is " + you_dog.name.title() + ".")

print("You dog is " + str(you_dog.age) + " years oid.")
 

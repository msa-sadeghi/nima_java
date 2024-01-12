class Dog:
    def __init__(self, dog_name, dog_gender, dog_age):
        self.name = dog_name
        self.gender = dog_gender
        self.age = dog_age

    def eat(self):
        if self.gender == "male":
            print(f"{self.name} Good Boy, Eat up!")
        else:
            print(f"{self.name} Good Girl, Eat up!")

    def bark(self, is_loud):
        if is_loud:
            print(f"{self.name} is WOOOOOOOFFFFFFing")

        else:
            print(f"{self.name} is WooFing")


class Beagle(Dog):
    def __init__(self, dog_name, dog_gender, dog_age, is_gun_shy):
        super().__init__(dog_name, dog_gender, dog_age)
        self.is_gun_shy = is_gun_shy

    def hunt(self):
        if not self.is_gun_shy:
            self.bark(True)
            print(self.name + " is hunting so well")

        else:
            print(self.name + " can not hunt")

beagle1 = Beagle("b1","male", 11, False)
beagle1.hunt()






# first_dog = Dog("bob", "male", 3)
# second_dog = Dog("roze", "female", 10)

# print(f"{first_dog.name} {first_dog.age}")
# print(f"{second_dog.name} {second_dog.age}")

# first_dog.eat()
# second_dog.eat()
# first_dog.bark(True)
# second_dog.bark(False)

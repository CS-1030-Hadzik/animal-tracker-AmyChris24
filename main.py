from animal import Animal
from dog import Dog

if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    animal1 = Animal("Leo", "Lion")
    # TODO: Print the Animal instance
    print(Animal)
    # TODO: Call the method to make a generic animal sound
    print(Animal.speak()) 
    # TODO: Create an instance of the Dog class
    dog1 = Dog("Buddy", "Canine", "Golden Retriever")
    # TODO: Print the Dog instance
    print(Dog)
    # TODO: Call the method to make the dog-specific sound
    print(Dog.speak())
    # TODO print out all the animals
    print("All Animals:")
    print("All Animals:")
    for animal in Animal.all_animals:
        print(animal)



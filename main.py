from animal import Animal
from dog import Dog

if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    animal = Animal("Leo", "Lion")
    # TODO: Print the Animal instance
    print(animal)
    # TODO: Call the method to make a generic animal sound
    print(animal.speak())
    # TODO: Create an instance of the Dog class
    dog = Dog("Buddy", "Canine", "Golden Retriever")
    # TODO: Print the Dog instance
    print(dog)
    # TODO: Call the method to make the dog-specific sound
    print(dog.speak())
    # TODO print out all the animals
    print("All Animals:")
    for a in Animal.all_animals:
        print(a)


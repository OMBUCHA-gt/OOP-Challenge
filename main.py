from pet import Pet

if __name__ == "__main__":
    my_pet = Pet("Buddy")

    my_pet.get_status()

    my_pet.eat()
    my_pet.play()
    my_pet.get_status()

    my_pet.sleep()
    my_pet.get_status()

    my_pet.train("Sit")
    my_pet.train("Fetch")
    my_pet.show_tricks()

    my_pet.play() # Buddy will be more tired now
    my_pet.get_status()

    my_pet.train("Roll Over")
    my_pet.show_tricks()
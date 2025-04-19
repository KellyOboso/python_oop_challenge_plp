from pet import Pet

def main():
    my_pet = Pet("Max")
    
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.get_status()
    
    my_pet.train("roll over")
    my_pet.train("play dead")
    my_pet.show_tricks()

if _name_ == "_main_":
    main()

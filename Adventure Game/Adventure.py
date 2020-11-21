question = input("Would you like to play? (yes/no) ")

if question.lower().strip() == "yes":
    health = 150
    question = input("You are a warrior! Do you want to continue? (yes/no) ").lower().strip()
    if question == "yes":
        print("You now have 150 health. If your health reaches zero: Game Over!")
    else:
        print("Invalid choice, you lost!")
    question = input("You encounter a monster, would you like to run/fight. ")
    if question == "fight":
        health -= 50
        print(f"In your fight with the monster you lost 50 health. health = {health}")
    question = input("On your journey to your hometown u meet a peasant. Would you help him? (yes/no) ")
    if question == "yes":
        health -= 50
        print(
            f"The peasant is a witch and when he offers you to eat \n"
            f" than he poisons you and than you kill him. your health {health}")
    question = input("You encounter your longly dead son would you like to speak to him. (yes/no) ")
    if question == "yes":
        health -= 100

    else:
        print("Congratulation you've reached your destination! You won the game ")

    if health <= 0:
        print("Game Over! your health reaches zero")


else:
    print("That's too bad!")

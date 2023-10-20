import random

# Get user input
print("1. Rock  2. Paper  3. Scissors")
value = input()

# Validate input
if value.isnumeric():
    player = int(value)
    if player > 0 and player < 4:
        # Input was valid. Generate bot value
        bot = random.randrange(1,3)
        #print("player: "+str(player)+"\nbot: "+str(bot))

        #convert player's number to a string
        match player:
            case 1:
                playerStr = "Rock"
            case 2:
                playerStr = "Paper"
            case 3:
                playerStr = "Scissors"

        #convert bot's number to a string
        match bot:
            case 1:
                botStr = "Rock"
            case 2:
                botStr = "Paper"
            case 3:
                botStr = "Scissors"

        # Check who won...
        if player == bot:
            print("I chose "+botStr+" and you chose "+playerStr)
            print("It's a tie!")
        elif player < bot:
            print("I chose "+botStr+" and you chose "+playerStr)
            print("I won!")
        else:
            print("I chose "+botStr+" and you chose "+playerStr)
            print("You win!")